"""
Capital matching engine for the Matching Algorithm.

Computes match percentages between user questionnaire answers and
capital type weight matrices, ranks results, and persists scores.
"""
import math
import random
import numpy as np
import pandas as pd
from Algorithm.models import capitalTypes, CapitalType
from CM_Market.models import VQuestion1
from .models import (
    Capital_Matches, Matches_Purchased, Letter_Response,
    Purchases, allCapitalMatchValues,
)
from .capitalHardCheck import capitalCheck


def sanitize_value(value):
    """Convert numpy types and handle NaN/Inf values."""
    if isinstance(value, (np.floating, np.integer)):
        value = float(value)
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return None
    return value


def compute_match_percentages(values_list):
    """
    Compute match percentage for each capital type.

    Args:
        values_list: Flat list of 0/1 questionnaire answer values.

    Returns:
        dict mapping capital type name -> match percentage (float),
        sorted ascending by percentage.
    """
    counter = (
        sum(1 for item in values_list if item == 1)
        - 2
        - sum(1 for item in values_list[103:112] if item == 1)
    )
    all_name_capital = capitalTypes.objects.values_list('name', flat=True)

    dict_name_percentage = {}
    for capital in all_name_capital:
        ct = CapitalType.objects.get(namec__name=capital)
        matrix_weight = np.array(ct.matrix_weights, dtype=np.float64)
        dict_name_percentage[capital] = (
            (sum(np.array(values_list) * matrix_weight)) * 10
        ) / counter

    # Sanitize and clean
    cleaned = {
        k: (sanitize_value(v) or 0)
        for k, v in dict_name_percentage.items()
    }

    # Sort ascending
    keys = list(cleaned.keys())
    vals = list(cleaned.values())
    sorted_idx = np.argsort(vals)
    sorted_percentage = {keys[i]: vals[i] for i in sorted_idx}

    # Ensure JSON-serializable
    final = {
        k: float(v) if isinstance(v, (np.floating, np.integer)) else v
        for k, v in sorted_percentage.items()
    }
    return capitalCheck(values_list, final), capitalCheck(values_list, sorted_percentage)


def persist_match_percentages(user, final_percentage):
    """Save or update the allCapitalMatchValues record for the user."""
    obj, created = allCapitalMatchValues.objects.get_or_create(
        user=user, defaults={'percentage': final_percentage}
    )
    if not created:
        allCapitalMatchValues.objects.filter(user=user).update(percentage=final_percentage)


def get_top_capital_names(user, values_list, sorted_percentage):
    """
    Get the top 5 capital type names for the user.

    If previously saved with override flag, use those; otherwise compute from scores.
    """
    try:
        status = Letter_Response.objects.get(user=user).top_6_name_output[-1]
    except Exception:
        status = False

    if status is True:
        return Letter_Response.objects.get(user=user).top_6_name_output
    else:
        return [
            item[0]
            for item in sorted(
                sorted_percentage.items(), key=lambda item: item[1], reverse=True
            )[:5]
        ]


def load_capital_market_data(top_5_names, user):
    """
    Load capital market vendor data for each of the top 5 capital types.

    Returns:
        cm_names: list of 5 capital type names
        cm_nums:  list of 5 vendor counts
        cm_id_value: list of already-purchased match IDs
    """
    try:
        purchased = Matches_Purchased.objects.get(user=user)
        cm_id_value = [0 if type(a) != int else int(a) for a in purchased.match_id_cm]
    except Matches_Purchased.DoesNotExist:
        cm_id_value = [0]

    cm_nums = []
    for name in top_5_names:
        try:
            count = VQuestion1.objects.filter(CM_Type=name).exclude(id__in=cm_id_value).count()
        except Exception:
            count = 0
        cm_nums.append(count)

    return top_5_names, cm_nums, cm_id_value


def compute_pricing(cm_nums):
    """
    Compute pricing based on total matches.

    Returns: (total_matches, price, totalprice, discount, balancedue)
    """
    total_matches = cm_nums[0] + cm_nums[1]
    price = 25
    totalprice = price * total_matches

    if total_matches >= 200:
        discount = 0.4 * totalprice
    elif total_matches >= 100:
        discount = 0.2 * totalprice
    else:
        discount = 0

    balancedue = totalprice - discount
    return total_matches, price, totalprice, discount, balancedue


def load_api_data(user, top_5_names, cm_id_value):
    """
    Load and sample capital market data for the API response.

    Returns:
        report: Matches_Purchased instance
        optionsapi: Purchases instance
        dfcm: DataFrame of sampled data
    """
    try:
        report = Matches_Purchased.objects.get(user=user)
    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=user)

    try:
        optionsapi = Purchases.objects.get(user=user)
    except Purchases.DoesNotExist:
        optionsapi = Purchases(user=user)

    cm1name = top_5_names[0]
    optionapi1 = optionsapi.cm1purchase

    try:
        cm1data = list(VQuestion1.objects.filter(CM_Type=cm1name).exclude(id__in=cm_id_value).values())
    except Exception:
        cm1data = []

    try:
        cm1dataapi = random.sample(cm1data, optionapi1)
    except Exception:
        cm1dataapi = cm1data[:optionapi1]

    all_data_api = cm1dataapi
    id_CM_api = cm_id_value + [int(a['id']) for a in all_data_api]
    report.match_id_cm = id_CM_api

    dfcm = pd.DataFrame(all_data_api)
    json_data_api = dfcm.to_json(orient='split')
    optionsapi.cm_matches = json_data_api
    optionsapi.save()

    return report, optionsapi, dfcm


def save_letter_response(user, profile, top_5_names, cm_nums, pricing):
    """Save match results to Letter_Response for API access."""
    total_matches, price, totalprice, discount, balancedue = pricing
    cm_type_count = 1

    try:
        output = Letter_Response.objects.get(user=user)
    except Letter_Response.DoesNotExist:
        output = Letter_Response(user=user)

    output.firstname = profile['firstname']
    output.lastname = profile['lastname']
    output.address = profile['primary_business_adress']
    output.phone = profile['business_phone']
    output.email = profile['primary_email']
    output.businessname = profile['company_name']
    output.count = cm_type_count
    output.fundgoal = profile['fundgoal']
    output.totalnum = total_matches
    output.cm1name = top_5_names[0]
    output.cm2name = top_5_names[1]
    output.cm3name = top_5_names[2]
    output.cm4name = top_5_names[3]
    output.cm5name = top_5_names[4]
    output.cm1no = cm_nums[0]
    output.cm2no = cm_nums[1]
    output.cm3no = cm_nums[2]
    output.cm4no = cm_nums[3]
    output.cm5no = cm_nums[4]
    output.price = price
    output.totalprice = totalprice
    output.discount = discount
    output.balancedue = balancedue
    output.top_6_name = top_5_names
    output.top_6_name_output = top_5_names
    output.save()
