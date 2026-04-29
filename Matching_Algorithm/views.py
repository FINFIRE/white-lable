"""
Matching Algorithm Views.

Handles the capital matching workflow: loading user questionnaire data,
computing match scores, rendering the letter report, and generating
PDF/Word document exports.
"""
import json
import random
from functools import wraps

import pandas as pd
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.urls import reverse, NoReverseMatch
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from rest_framework.authtoken.models import Token

from registration.models import UserDetail
from connections.models import Match_Data, pay_load_string
from .models import Letter_Response, Matches_Purchased, Purchases
from .info_cm import info
from .definitions import definitions

# Refactored modules
from .task_helpers import create_capital_type_for_user
from .questionnaire_data import (
    load_user_profile,
    load_questionnaire_values,
    load_summary_context,
    load_payload_data,
)
from .matching_engine import (
    compute_match_percentages,
    persist_match_percentages,
    get_top_capital_names,
    load_capital_market_data,
    compute_pricing,
    load_api_data,
    save_letter_response,
)
from .capital_documents import get_capital_documents
from .document_generators import generate_pdf_response, generate_word_response


# ──────────────────────────────────────────────────────────────────────
# Authentication decorator
# ──────────────────────────────────────────────────────────────────────

def token_or_session_required(view_func):
    """Custom decorator that handles both token and session authentication."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Session-based auth
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        # Token-based auth
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
            try:
                token = Token.objects.get(key=token_key)
                request.user = token.user
                return view_func(request, *args, **kwargs)
            except Token.DoesNotExist:
                if request.headers.get('accept') == 'application/json':
                    return JsonResponse({"error": "Invalid token"}, status=401)
                return HttpResponse("Invalid token", status=401)

        return redirect('login_view')

    return wrapper


# ──────────────────────────────────────────────────────────────────────
# Shared helpers
# ──────────────────────────────────────────────────────────────────────

def _run_matching_pipeline(user):
    """
    Run the full matching pipeline for a user.

    Returns:
        (profile, values_list, top_5_names, cm_nums, cm_id_value, pricing)
    Raises:
        Exception if survey data is incomplete.
    """
    profile = load_user_profile(user)
    values_list = load_questionnaire_values(user)

    # Compute match percentages
    final_percentage, sorted_percentage = compute_match_percentages(values_list)
    persist_match_percentages(user, final_percentage)

    # Get top 5 capital types
    top_5_names = get_top_capital_names(user, values_list, sorted_percentage)

    # Create truth-in-capital record for the #1 match
    create_capital_type_for_user(user, top_5_names[0])

    # Load capital market vendor data
    _, cm_nums, cm_id_value = load_capital_market_data(top_5_names, user)

    # Compute pricing
    pricing = compute_pricing(cm_nums)

    return profile, values_list, top_5_names, cm_nums, cm_id_value, pricing


def _ensure_payload_string(user, profile):
    """Create the webhook payload string record if it doesn't exist."""
    try:
        pay_load_string.objects.get(user=user)
    except pay_load_string.DoesNotExist:
        payload_data = load_payload_data(user)
        pay_load_string.objects.create(user=user, payLoadString=payload_data)


def _build_letter_context(request, profile, top_5_names, cm_nums, pricing):
    """Build the template context dict used by the letter views."""
    total_matches, price, totalprice, discount, balancedue = pricing
    cm1name = top_5_names[0]

    # Get capital type documents (definition, FAQ, twelve-variable)
    docs = get_capital_documents(cm1name, request)
    definition = mark_safe(docs[0].content.decode('utf-8'))
    faq_que = mark_safe(docs[1].content.decode('utf-8'))
    twelvev = mark_safe(docs[2].content.decode('utf-8'))

    # Get or create report/purchases objects
    try:
        report = Matches_Purchased.objects.get(user=request.user)
    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=request.user)

    return {
        'date': profile['date'],
        'firstname': profile['firstname'],
        'lastname': profile['lastname'],
        'address': profile['primary_business_adress'],
        'phone': profile['business_phone'],
        'secondphone': UserDetail.objects.get(user=request.user).Mobile_Phone,
        'email': profile['primary_email'],
        'businessname': profile['company_name'],
        'count': 1,
        'fundgoal': profile['fundgoal'],
        'totalnum': total_matches,
        'cm1name': top_5_names[0],
        'cm1nameoutput': top_5_names[0],
        'cm2name': top_5_names[1],
        'cm2nameoutput': top_5_names[1],
        'cm3name': top_5_names[2],
        'cm3nameoutput': top_5_names[2],
        'cm4name': top_5_names[3],
        'cm5name': top_5_names[4],
        'cm1no': cm_nums[0],
        'cm2no': cm_nums[1],
        'cm3no': cm_nums[2],
        'cm4no': cm_nums[3],
        'cm5no': cm_nums[4],
        'price': price,
        'totalprice': totalprice,
        'discount': discount,
        'balancedue': balancedue,
        'report': report,
        'list_name': top_5_names,
        'info': info,
        'definition': definition,
        'faq_que': faq_que,
        'twelvev': twelvev,
    }


def _save_match_html(request, context):
    """Render and save the letter HTML for the connections app."""
    rendered_html = render_to_string('letter499.html', context)
    try:
        html_data = Match_Data.objects.get(user=request.user)
        html_data.html = rendered_html
        html_data.save()
    except Match_Data.DoesNotExist:
        Match_Data(user=request.user, html=rendered_html).save()


# ──────────────────────────────────────────────────────────────────────
# Views
# ──────────────────────────────────────────────────────────────────────

@login_required
def Match(request):
    """Main matching view — compute matches, render letter page."""
    try:
        pipeline = _run_matching_pipeline(request.user)
        profile, values_list, top_5_names, cm_nums, cm_id_value, pricing = pipeline
    except Exception:
        return HttpResponse("Please Go through survey and complete all questions!")

    # Ensure webhook payload exists
    _ensure_payload_string(request.user, profile)

    # Load API data
    load_api_data(request.user, top_5_names, cm_id_value)

    # Build context and save
    context = _build_letter_context(request, profile, top_5_names, cm_nums, pricing)
    save_letter_response(request.user, profile, top_5_names, cm_nums, pricing)
    _save_match_html(request, context)

    return render(request, 'thankyouresponse.html', context)


@login_required
def faq(request):
    """FAQ listing view for matched capital types."""
    try:
        output_list = Letter_Response.objects.get(user=request.user).top_6_name_output
        if output_list[-1] is True:
            output_list = output_list[:-1]
    except Exception:
        return HttpResponse("please complete the Survey to get the report!")

    # Check which FAQ links are valid
    links_with_error = []
    for link in output_list:
        try:
            reverse(link + 'faq')
        except NoReverseMatch:
            links_with_error.append(link + 'faq')

    return render(request, 'faq.html', {
        "list_name_output": output_list,
        "links_with_error": links_with_error,
    })


@login_required
def definition(request):
    """Definition listing view for matched capital types."""
    try:
        output_list = Letter_Response.objects.get(user=request.user).top_6_name_output
        if output_list[-1] is True:
            output_list = output_list[:-1]
    except Exception:
        return HttpResponse("please complete the Survey to get the report!")

    links_with_error = []
    for link in output_list:
        try:
            reverse(link)
        except NoReverseMatch:
            links_with_error.append(link)

    return render(request, 'definition.html', {
        "list_name_output": output_list,
        "links_with_error": links_with_error,
    })


@login_required
def twelvevariable(request):
    """Twelve-variable report listing view for matched capital types."""
    try:
        output_list = Letter_Response.objects.get(user=request.user).top_6_name_output
        if output_list[-1] is True:
            output_list = output_list[:-1]
    except Exception:
        return HttpResponse("please complete the Survey to get the report!")

    links_with_error = []
    for link in output_list:
        try:
            reverse(link + 'twelve')
        except NoReverseMatch:
            links_with_error.append(link + 'twelve')

    return render(request, 'twelvevariable.html', {
        "list_name_output": output_list,
        "links_with_error": links_with_error,
    })


@login_required
def summary(request):
    """Summary of all user questionnaire responses."""
    try:
        context = load_summary_context(request.user)
    except Exception:
        return HttpResponse("please complete the Survey to get the report!")

    return render(request, 'summary_of_response.html', context)


# ──────────────────────────────────────────────────────────────────────
# Document export views
# ──────────────────────────────────────────────────────────────────────

@token_or_session_required
def pdf(request):
    """Generate and download the FINFIRE letter as a PDF."""
    try:
        pipeline = _run_matching_pipeline(request.user)
        profile, values_list, top_5_names, cm_nums, cm_id_value, pricing = pipeline
    except Exception:
        return HttpResponse("Please Go through survey and complete all questions!")

    # Load API data
    load_api_data(request.user, top_5_names, cm_id_value)

    # Handle POST (purchase flow)
    if request.method == 'POST':
        return _handle_purchase_post(request, top_5_names, cm_id_value, profile)

    # Build context
    context = _build_letter_context(request, profile, top_5_names, cm_nums, pricing)
    context['tony_signature_url'] = request.build_absolute_uri(static('img/none.png'))
    context['logo_url'] = request.build_absolute_uri(static('img/b.png'))

    # Save response data
    save_letter_response(request.user, profile, top_5_names, cm_nums, pricing)
    _save_match_html(request, context)

    return generate_pdf_response(request, context, profile['company_name'])


@login_required
def word(request):
    """Generate and download the FINFIRE letter as a Word document."""
    try:
        pipeline = _run_matching_pipeline(request.user)
        profile, values_list, top_5_names, cm_nums, cm_id_value, pricing = pipeline
    except Exception:
        return HttpResponse("Please Go through survey and complete all questions!")

    # Load API data
    load_api_data(request.user, top_5_names, cm_id_value)

    # Handle POST (purchase flow)
    if request.method == 'POST':
        return _handle_purchase_post(request, top_5_names, cm_id_value, profile)

    # Build context
    context = _build_letter_context(request, profile, top_5_names, cm_nums, pricing)

    # Save response data
    save_letter_response(request.user, profile, top_5_names, cm_nums, pricing)

    return generate_word_response(request, context, profile['company_name'])


def _handle_purchase_post(request, top_5_names, cm_id_value, profile):
    """Handle POST requests for the purchase flow in pdf/word views."""
    from CM_Market.models import VQuestion1

    option1 = int(request.POST.get(top_5_names[0], 0))
    option2 = int(request.POST.get(top_5_names[1], 0))
    option3 = int(request.POST.get(top_5_names[2], 0))
    option4 = int(request.POST.get(top_5_names[3], 0))
    option5 = int(request.POST.get(top_5_names[4], 0))
    option7 = int(request.POST.get('option7', 0))

    # Sample data for each capital type
    all_data = []
    for name, count in zip(top_5_names, [option1, option2, option3, option4, option5]):
        try:
            cm_data = list(
                VQuestion1.objects.filter(CM_Type=name)
                .exclude(id__in=cm_id_value)
                .values()
            )
            try:
                sampled = random.sample(cm_data, count)
            except ValueError:
                sampled = cm_data[:count]
            all_data.extend(sampled)
        except Exception:
            pass

    # Save purchase record
    try:
        report = Matches_Purchased.objects.get(user=request.user)
    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=request.user)

    id_CM = cm_id_value + [int(a['id']) for a in all_data]
    report.match_id_cm = id_CM

    dfcm = pd.DataFrame(all_data)
    html_table = dfcm.to_html()

    purchase_dict = {
        top_5_names[0]: option1, top_5_names[1]: option2,
        top_5_names[2]: option3, top_5_names[3]: option4,
        top_5_names[4]: option5, 'intermediaries': option7,
    }

    total_num = option1
    price = 25
    total_price = total_num * price

    if total_num > 200:
        discount = 0.4 * total_price
    elif total_num > 100:
        discount = 0.2 * total_price
    else:
        discount = 0

    balance_due = total_price - discount

    report.purchased_matches = json.dumps(purchase_dict)
    report.total_num = total_num
    report.total_price = total_price
    report.discount = discount
    report.balance_due = balance_due
    report.price = price
    report.save()

    return render(request, 'finfo.html', {
        'table': html_table,
        'list_name': top_5_names,
    })
