from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.urls import reverse, NoReverseMatch
import pandas as pd
import math
import os
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared,PreRating
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases,allCapitalMatchValues
from CM_Market.models import VQuestion1
from django.template.loader import render_to_string
import json
import random
import numpy as np 
from .info_cm import info
from .definitions import definitions 
from weasyprint import HTML
from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_BREAK
from Algorithm.models import capitalTypes,CapitalType
from truth_in_capital.models import TruthCapitalType, Task, time as TruthTime, rating as TaskRating
from django.utils import timezone
from truth_in_capital.utils import ensure_rominadmin_tasks_exist, get_rominadmin_tasks_for_capital_type
from finfire_web.settings import BASE_DIR
from django.templatetags.static import static
from .capitalinformation import accelerator,acceleratorprivate1,acceleratorpublic2,acceleratoruniversity3,appscabbage4,bonds,bondsforeign5,bondsgovernmentbacked6,bondshighyieldjunk7,bondsinvestmentgrade8,bondsmortgagebacked9,bootstrappedcashsaving10,bootstrappedhomeequity11,bootstrappedpersonalcreditcards12,bootstrappedretirement401ksdi13,bootstrappedwholelifeinsurance14,bootstrapped,commercialbanking,commercialbankingacquisitionloan15,commercialbankingassestbased16,commercialbankingcollateralizeddebt17,commercialbankingcommercialbankloan18,commercialbankingcreditcard19,commercialbankingequipmentloan20,commercialbankinglineofcredit21,commercialbankingrealestateloan22,commercialbankingstandbylinesofcredit23,cryptocurrency,cryptocurrencyinitialcoinoffering24,cryptocurrencyinitialexchangeoffering25,cryptocurrencyinvestmentviacryptowallet26,factoring,factoringaccountsreceivable27,factoringinvoicefactoring28,factoringmerchantaccountadvances29,factoringpurchaseorderloan30,governmentincentiveeb5immigration31,governmentincentiveenterprisezone32,governmentincentives,grants,grantscorporategrants33,grantseducationgrants34,grantsgovernment35,grantsmunicipalities36,grantsresearchgrants37,grantsstateagencies38,hedgefunds,hedgefundsprivate39,hedgefundspublic40,incubator,incubatorprivate41,incubatorpublic42,incubatoruniversity43,investmentbanking,investmentbankingbrokerdealerrepresentation44,investmentbankingbrokersyndication45,investmentbankingequitysales46,investmentbankinginvestmentbankerdebt47,investmentbankingmezzaninefinancing48,privatedebt,privatedebtacquisitionloan49,privatedebtassetbasedlending50,privatedebtbridgefinancing51,privatedebtcollaterizeddebt52,privatedebthardmoneyloan53,privatedebtprivatedebt54,privatedebtpromisorynote55,privatedebtrealestateloan56,privateequitysecurities,privateequitysecuritiesacrreditedinvestors57,privateequitysecuritiesangelinvestors58,privateequitysecuritiesbrokerdealers3378_59,privateequitysecuritiesconvertiblenote60,privateequitysecuritiesfamilyandfriends61,privateequitysecuritiesfamilyoffices62,privateequitysecuritieshighnetworthindividuals63,privateequitysecuritiesprivateplacementmemorandum64,privateequitysecuritiesregulationa65,privateequitysecuritiesregulationCFtitleIII66,privateequitysecuritiesregulationd504_67,privateequitysecuritiesregulationd506b68,privateequitysecuritiesregulationd506c69,privateequitysecuritiesrule144_70,privateequitysecuritiessimpleagreementfutureequity71,royaltyfinancing,royaltyfinancingtoplinerevenue72,SmallBusinessAdministration,smallbusinessadministration504B73,smallbusinessadministration7a74,smallbusinessadministrationcdcsbdc77,smallbusinessadministrationexpress75,smallbusinessadministrationsbic78,smallbusinessadministrationveteran76,thirdpartycorporatecredit79,tokenization80,venturecapital,venturecapitalequitysale81,venturecapitallongtermdebt82,venturecapitalmezzaninefinancing83,venturecapitalmergersandacquisitionsfinancing84,venturecapitalshorttermbridgefinancing85,governmentincentivesgoldstar86
from django.utils.safestring import mark_safe
from django.conf import settings
from docx.shared import Inches,Cm
from weasyprint import CSS
from docx.shared import RGBColor
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
import time
from functools import wraps
import uuid
import threading
from django.http import FileResponse
from connections.models import pay_load_string
from entreprise_questions.models import ReferalResponse,LendingRequirements
from .capitalHardCheck import capitalCheck


def create_capital_type_for_user(user, cm1name):
    """
    Helper function to create a TruthCapitalType record for a user and associated tasks
    """
    try:
        # Check if a capital type already exists for this user
        existing_capital_type = TruthCapitalType.objects.filter(user=user).first()
        
        if existing_capital_type:
            # Update the existing record
            existing_capital_type.capital_type = cm1name
            existing_capital_type.save()
            capital_type = existing_capital_type
        else:
            # Create a new record
            capital_type = TruthCapitalType.objects.create(
                user=user,
                capital_type=cm1name
            )
            
            # Create default tasks for the new capital type
            create_default_tasks_for_capital_type(capital_type)
        
        # Create timing record with start_date = matched_date + 7 days only if it doesn't exist
        matched_date_plus_7 = timezone.now().date() + timedelta(days=7)
        TruthTime.objects.get_or_create(
            capital_type=capital_type,
            defaults={"start_date": matched_date_plus_7},
        )

        # Sync task ratings from pre_rating if available
        try:
            # Fetch pre-ratings for this user
            pre = PreRating.objects.filter(user=user).first()
            if pre and isinstance(pre.preratings, dict):
                # Map of task_name -> numeric rating from pre.preratings
                prer_dict = pre.preratings

                # Iterate over tasks for this capital_type and apply ratings
                for task in Task.objects.filter(capital_type=capital_type):
                    if task.task_name in prer_dict:
                        try:
                            task_rating_value = int(prer_dict.get(task.task_name))
                        except (TypeError, ValueError):
                            continue
                        if 0 <= task_rating_value <= 10:
                            TaskRating.objects.update_or_create(
                                task=task,
                                defaults={"rating": task_rating_value},
                            )
        except Exception as e:
            # Non-fatal: continue without blocking match flow
            print(f"Error syncing pre-ratings for user {user.id}: {e}")
            
    except Exception as e:
        print(f"Error creating capital type for user {user.id}: {e}")

def create_default_tasks_for_capital_type(capital_type):
    """
    Create default tasks for a new capital type based on rominadmin's tasks
    """
    try:
        # Ensure rominadmin tasks exist
        ensure_rominadmin_tasks_exist()
        
        # Get tasks from rominadmin for the same capital type
        rominadmin_tasks = get_rominadmin_tasks_for_capital_type("Private Equity Securities") #alternately capital_type.capital_type)
        
        if rominadmin_tasks:
            # Copy tasks from rominadmin's capital type
            for task in rominadmin_tasks:
                Task.objects.create(
                    capital_type=capital_type,
                    task_name=task.task_name,
                    task_max_hour=task.task_max_hour,
                    task_type=task.task_type,
                    task_precedence=task.task_precedence
                )
            return
        
        # If no rominadmin tasks found, create default tasks
        create_standard_default_tasks(capital_type)
        
    except Exception as e:
        print(f"Error creating default tasks for capital type {capital_type.id}: {e}")
        # Fallback to standard default tasks
        create_standard_default_tasks(capital_type)

def create_standard_default_tasks(capital_type):
    """
    Create standard default tasks when no rominadmin template is available
    """
    default_tasks = [
        {
            'task_name': 'Finfire Report - Capital Type',
            'task_max_hour': 4,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 0
        },
        {
            'task_name': 'Financial Model, forecast, pro forma',
            'task_max_hour': 20,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 0
        },
        {
            'task_name': 'Due Diligence Checklist Documents',
            'task_max_hour': 4,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 1
        },
        {
            'task_name': 'Historical Financials (P & L, BS, CF, Aging)',
            'task_max_hour': 1,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 1
        },
        {
            'task_name': 'Tax Returns (Up to 2 years, if applicable)',
            'task_max_hour': 1,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 1
        },
        {
            'task_name': 'Business Valuation (Equity only)',
            'task_max_hour': 20,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 1
        },
        {
            'task_name': 'Cap Table, Use of Funds, & Capitalization Plan',
            'task_max_hour': 5,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 1
        },
        {
            'task_name': 'Executive Summary Including Exit Strategy',
            'task_max_hour': 2,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Presentation Deck',
            'task_max_hour': 10,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Business Model Canvas',
            'task_max_hour': 2,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Resume of Founder/CEO Primary Leader',
            'task_max_hour': 1,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Application (If Applicable)',
            'task_max_hour': 6,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Presentation Video (From the AI Deep Dive)',
            'task_max_hour': 10,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Offering Documents',
            'task_max_hour': 25,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 2
        },
        {
            'task_name': 'Quality Assurance Checklist (Including AI)',
            'task_max_hour': 3,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 3
        },
        {
            'task_name': 'Capital Match List Generated',
            'task_max_hour': 10,
            'task_type': 'FINFIRE Staff Review & Scope of Work',
            'task_precedence': 3
        },
        {
            'task_name': 'Investor Marketing Campaign',
            'task_max_hour': 20,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 4
        },
        {
            'task_name': 'Investor Relations',
            'task_max_hour': 20,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 4
        },
        {
            'task_name': 'Progress Reports',
            'task_max_hour': 12,
            'task_type': 'Intermediary Services Scope of Work',
            'task_precedence': 4
        }
    ]
    
    for task_data in default_tasks:
        Task.objects.create(
            capital_type=capital_type,
            **task_data
        )

def token_or_session_required(view_func):
    """
    Custom decorator that handles both token and session authentication
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # First check if user is authenticated via session
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        
        # If not authenticated via session, check for token authentication
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
            try:
                token = Token.objects.get(key=token_key)
                request.user = token.user
                return view_func(request, *args, **kwargs)
            except Token.DoesNotExist:
                # Return JSON response for API requests
                if request.headers.get('accept') == 'application/json':
                    return JsonResponse({"error": "Invalid token"}, status=401)
                return HttpResponse("Invalid token", status=401)
        
        # If neither session nor token authentication works, redirect to login
        return redirect('login_view')
    
    return wrapper

@login_required
def Match(request):
    #time.sleep(5)  # Add 10 second delay
    try:
        collateral_status_check =LendingRequirements.objects.get(user=request.user).collateral_status
        credit_score_check = LendingRequirements.objects.get(user=request.user).credit_score 
        criminal_history_check = LendingRequirements.objects.get(user=request.user).criminal_history
        firstname = UserDetail.objects.get(user=request.user).First_Name #string
        lastname = UserDetail.objects.get(user=request.user).Last_Name #string
        date = datetime.now().strftime('%B %d, %Y') #no need
        primary_business_adress = UserDetail.objects.get(user=request.user).Business_Adress #string
        business_phone = UserDetail.objects.get(user=request.user).Business_Phone #string
        fundgoal = EQuestions5.objects.get(user=request.user).Selected_Option[:] # string based on question of how much capital user want to raise
        mobile_phone = UserDetail.objects.get(user=request.user).Mobile_Phone #string
        primary_email = UserDetail.objects.get(user=request.user).User_Email #string
        company_website = UserDetail.objects.get(user=request.user).Company_Website #string
        company_name = EQuestions2.objects.get(user=request.user).Business_Name #string
        one = EQuestions1.objects.get(user=request.user).Idea #int 0 if not selected 1 if selected
        two = EQuestions1.objects.get(user=request.user).Formation #int 0 if not selected 1 if selected
        three = EQuestions1.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        four = EQuestions1.objects.get(user=request.user).Growth #int 0 if not selected 1 if selected
        five = EQuestions1.objects.get(user=request.user).M_And_A #int 0 if not selected 1 if selected
        six = EQuestions1.objects.get(user=request.user).Preparing_For_Public #int 0 if not selected 1 if selected
        seven = EQuestions1.objects.get(user=request.user).Distressed #int 0 if not selected 1 if selected
        eight = EQuestions2.objects.get(user=request.user).No_Business #int 0 if not selected 1 if selected
        nine = EQuestions2.objects.get(user=request.user).Sole_Proprietorship #int 0 if not selected 1 if selected
        ten = EQuestions2.objects.get(user=request.user).LLC #int 0 if not selected 1 if selected
        eleven = EQuestions2.objects.get(user=request.user).LP #int 0 if not selected 1 if selected
        twelve = EQuestions2.objects.get(user=request.user).GP #int 0 if not selected 1 if selected
        thirteen = EQuestions2.objects.get(user=request.user).S_Corporation #int 0 if not selected 1 if selected
        fourteen = EQuestions2.objects.get(user=request.user).C_Corp #int 0 if not selected 1 if selected
        fifteen = EQuestions2.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        sixteen = EQuestions3.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        seventeen = EQuestions3.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        eighteen = EQuestions3.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        nineteen = EQuestions3.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        twenty = EQuestions3.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        twentyone = EQuestions3.objects.get(user=request.user).More_1M_Less_2M #int 0 if not selected 1 if selected
        twentytwo = EQuestions3.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        twentythree = EQuestions3.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        twentyfour = EQuestions3.objects.get(user=request.user).More_10M #int 0 if not selected 1 if selected
        twentyfive = EQuestions4.objects.get(user=request.user).Accelerator #int 0 if not selected 1 if selected
        twentysix = EQuestions4.objects.get(user=request.user).Bonds #int 0 if not selected 1 if selected
        twentyseven = EQuestions4.objects.get(user=request.user).Comercial_Banking #int 0 if not selected 1 if selected
        twentyeight = EQuestions4.objects.get(user=request.user).Cryptocurrency #int 0 if not selected 1 if selected
        twentynine = EQuestions4.objects.get(user=request.user).EB5_Immigration #int 0 if not selected 1 if selected
        thirty = EQuestions4.objects.get(user=request.user).Enterprise_Zones #int 0 if not selected 1 if selected
        thirtyone = EQuestions4.objects.get(user=request.user).Factoring #int 0 if not selected 1 if selected
        thirtytwo = EQuestions4.objects.get(user=request.user).Grants #int 0 if not selected 1 if selected
        thirtythree = EQuestions4.objects.get(user=request.user).Hedge_Funds #int 0 if not selected 1 if selected 
        thirtyfour = EQuestions4.objects.get(user=request.user).Incubator #int 0 if not selected 1 if selected
        thirtyfive = EQuestions4.objects.get(user=request.user).Investment_Banking #int 0 if not selected 1 if selected
        thirtysix = EQuestions4.objects.get(user=request.user).Other_Owner_Equity #int 0 if not selected 1 if selected
        thirtyseven = EQuestions4.objects.get(user=request.user).Private_Debt #int 0 if not selected 1 if selected
        thirtyeight = EQuestions4.objects.get(user=request.user).Private_Equity #int 0 if not selected 1 if selected
        thirtynine = EQuestions4.objects.get(user=request.user).Public_Offereing #int 0 if not selected 1 if selected
        fourty = EQuestions4.objects.get(user=request.user).Real_Estate #int 0 if not selected 1 if selected
        fourtyone = EQuestions4.objects.get(user=request.user).Royalty_Financing #int 0 if not selected 1 if selected
        fourtytwo = EQuestions4.objects.get(user=request.user).Small_Business_Administration #int 0 if not selected 1 if selected
        fourtythree = EQuestions4.objects.get(user=request.user).Venture_Capital #int 0 if not selected 1 if selected
        fourtyfour = EQuestions4.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        fourtyfive = EQuestions5.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        fourtysix = EQuestions5.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        fourtyseven = EQuestions5.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        fourtyeight = EQuestions5.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        fourtynine = EQuestions5.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        fifty = EQuestions5.objects.get(user=request.user).More_1M_Less_1_35M #int 0 if not selected 1 if selected
        fiftyone = EQuestions5.objects.get(user=request.user).More_1_35M_Less_2M #int 0 if not selected 1 if selected
        fiftytwo = EQuestions5.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        fiftythree = EQuestions5.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        fiftyfour = EQuestions5.objects.get(user=request.user).More_10M_Less_20M #int 0 if not selected 1 if selected
        fiftyfive = EQuestions5.objects.get(user=request.user).More_20M #int 0 if not selected 1 if selected
        fiftysix = EQuestions5.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        fiftyseven = EQuestions6.objects.get(user=request.user).Founders_Round #int 0 if not selected 1 if selected
        fiftyeight = EQuestions6.objects.get(user=request.user).Pre_Seed #int 0 if not selected 1 if selected
        fiftynine = EQuestions6.objects.get(user=request.user).Seed #int 0 if not selected 1 if selected
        sixty = EQuestions6.objects.get(user=request.user).Series_A #int 0 if not selected 1 if selected
        sixtyone = EQuestions6.objects.get(user=request.user).Series_B #int 0 if not selected 1 if selected
        sixtytwo = EQuestions6.objects.get(user=request.user).Series_C #int 0 if not selected 1 if selected
        sixtythree = EQuestions6.objects.get(user=request.user).Pre_Ipo #int 0 if not selected 1 if selected
        sixtyfour = EQuestions6.objects.get(user=request.user).Ipo #int 0 if not selected 1 if selected 
        sixtyfive = EQuestions6.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        sixtysix = EQuestions6.objects.get(user=request.user).One #int 0 if not selected 1 if selected
        sixtyseven = EQuestions6.objects.get(user=request.user).Two #int 0 if not selected 1 if selected
        sixtyeight = EQuestions6.objects.get(user=request.user).TBD #to be determined #int 0 if not selected 1 if selected
        sixtynine = EQuestions7.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        seventy = EQuestions7.objects.get(user=request.user).Growth_Scalabitlity #int 0 if not selected 1 if selected
        seventyone = EQuestions7.objects.get(user=request.user).Marketing_and_Sales #int 0 if not selected 1 if selected 
        seventytwo = EQuestions7.objects.get(user=request.user).Cash_FLow_Capital #int 0 if not selected 1 if selected
        seventythree = EQuestions7.objects.get(user=request.user).Human_Capital #int 0 if not selected 1 if selected
        seventyfour = EQuestions7.objects.get(user=request.user).Equipment #int 0 if not selected 1 if selected
        seventyfive = EQuestions7.objects.get(user=request.user).Merger_and_Acquistions #int 0 if not selected 1 if selected
        seventysix = EQuestions7.objects.get(user=request.user).Inventory #int 0 if not selected 1 if selected 
        seventyseven = EQuestions7.objects.get(user=request.user).Real_State #int 0 if not selected 1 if selected
        seventyeight = EQuestions7.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        seventynine = EQuestions7.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        eighty = EQuestions8.objects.get(user=request.user).Low_Risk_Tolerance #int 0 if not selected 1 if selected
        eightyone = EQuestions8.objects.get(user=request.user).Medium_Risk_Tolerance #int 0 if not selected 1 if selected
        eightytwo = EQuestions8.objects.get(user=request.user).High_Risk_Tolerance #int 0 if not selected 1 if selected
        eightythree = EQuestions8.objects.get(user=request.user).Low_Cost_Capital #int 0 if not selected 1 if selected
        eightyfour = EQuestions8.objects.get(user=request.user).Medium_Cost_Capital #int 0 if not selected 1 if selected
        eightyfive = EQuestions8.objects.get(user=request.user).High_Cost_Capital #int 0 if not selected 1 if selected
        eightysix = EQuestions8.objects.get(user=request.user).Very_High_Cost_Capital #int 0 if not selected 1 if selected
        eightyseven = EQuestions8.objects.get(user=request.user).Immaterial_Cost_Capital #int 0 if not selected 1 if selected
        eightyeight = EQuestions.objects.get(user=request.user).RC_zero_to_499
        eightynine = EQuestions.objects.get(user=request.user).RC_500_to_999
        ninety = EQuestions.objects.get(user=request.user).RC_1000_to_2499
        ninetyone = EQuestions.objects.get(user=request.user).RC_2500_to_4999
        ninetytwo = EQuestions.objects.get(user=request.user).RC_5000_to_9999
        ninetythree = EQuestions.objects.get(user=request.user).RC_10000_to_24999
        ninetyfour = EQuestions.objects.get(user=request.user).RC_25000_to_49999
        ninetyfive = EQuestions.objects.get(user=request.user).RC_More_Than_50000
        ninetysix = EQuestions.objects.get(user=request.user).RT_1D_to_1W
        ninetyseven = EQuestions.objects.get(user=request.user).RT_1W_to_2W
        ninetyeight = EQuestions.objects.get(user=request.user).RT_2W_to_4W
        ninetynine = EQuestions.objects.get(user=request.user).RT_1M_to_2M
        hundred = EQuestions.objects.get(user=request.user).RT_2M_to_3M
        hundredone = EQuestions.objects.get(user=request.user).RT_3M_to_6M
        hundredtwo = EQuestions.objects.get(user=request.user).RT_6M_to_12M
        hundredthree = EQuestions.objects.get(user=request.user).RT_More_Than_a_Year
        hundredfour = DocumentsPrepared.objects.get(user=request.user).summary_of_offering
        hundredfive = DocumentsPrepared.objects.get(user=request.user).financial_forecast
        hundredsix = DocumentsPrepared.objects.get(user=request.user).lean_business_model
        hundredseven = DocumentsPrepared.objects.get(user=request.user).presentation_deck
        hundredeight = DocumentsPrepared.objects.get(user=request.user).leadership_overview
        hundrednine = DocumentsPrepared.objects.get(user=request.user).exit_strategy
        hundredten = DocumentsPrepared.objects.get(user=request.user).offering_documents
        hundredeleven = DocumentsPrepared.objects.get(user=request.user).ai_generated_deep_dive
        hundredtwelve = DocumentsPrepared.objects.get(user=request.user).virtual_data_room
        
        # Collateral status
        if collateral_status_check == "Not Applicable":
            hundredthirteen = 1  # not applicable
            hundredfourteen = 0
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "Yes":
            hundredthirteen = 0
            hundredfourteen = 1  # Yes
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "No":
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 1   # No
            hundredsixteen = 0
        else:
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 0            
            hundredsixteen = 1   # Other

        # Credit score
        if credit_score_check == "<580":
            hundredseventeen = 1 #<580
            hundredeighteen = 0
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">620":
            hundredseventeen = 0
            hundredeighteen = 1 #<620
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">680":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 1 #>680
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">720":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 1 #>720
            hundredtwentyone = 0 
        else:
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 0            
            hundredtwentyone = 1 #>760

        # Criminal history
        if criminal_history_check == "None":
            hundredtwentytwo = 1
            hundredtwentythree = 0
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0
        elif criminal_history_check == "Misdemeanor":
            hundredtwentytwo = 0
            hundredtwentythree = 1 #Misdemeanor
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Felony":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 1 #Felony
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Fraud":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 1 #Fraud
            hundredtwentysix = 0                
        else:
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 1 #Securities Violation   
        #eightyeight = EQuestions9.objects.get(user=request.user).One_Page_Tear_Sheet #int value between 1 to 5
        #eightynine = EQuestions9.objects.get(user=request.user).Elevator_Peach #int value between 1 to 5
        #ninety = EQuestions9.objects.get(user=request.user).Business_Plan #int value between 1 to 5
        #ninetyone = EQuestions9.objects.get(user=request.user).DD_Corporate_Identity #int value between 1 to 5
        #ninetytwo = EQuestions9.objects.get(user=request.user).DD_Technology #int value between 1 to 5
        #ninetythree = EQuestions9.objects.get(user=request.user).Executive_Summary #int value between 1 to 5
        #ninetyfour = EQuestions9.objects.get(user=request.user).Virtual_Portal #int value between 1 to 5
        #ninetyfive = EQuestions10.objects.get(user=request.user).Assumption_Worksheets #int value between 1 to 5
        #ninetysix = EQuestions10.objects.get(user=request.user).Capital_Structure_Plan #int value between 1 to 5
        #ninetyseven = EQuestions10.objects.get(user=request.user).Capitalization_Table #int value between 1 to 5
        #ninetyeight = EQuestions10.objects.get(user=request.user).Financial_Modeling_FC #int value between 1 to 5
        #ninetynine = EQuestions10.objects.get(user=request.user).Financial_Modeling_RC #int value between 1 to 5
        #hundred = EQuestions10.objects.get(user=request.user).Financial_Modeling_SP #int value between 1 to 5
        #hundredone = EQuestions10.objects.get(user=request.user).Sources_Uses #int value between 1 to 5
        #hundredtwo = EQuestions10.objects.get(user=request.user).Valuation_Spreadsheets #int value between 1 to 5
        #hundredthree = EQuestions10.objects.get(user=request.user).Valuation_OLFVW #int value between 1 to 5
        #hundredfour = EQuestions11.objects.get(user=request.user).Business_Model_Canvas #int value between 1 to 5
        #hundredfive = EQuestions11.objects.get(user=request.user).Company_Website_V3 #int value between 1 to 5
        #hundredsix = EQuestions11.objects.get(user=request.user).Website_Marketing #int value between 1 to 5
        #hundredseven = EQuestions11.objects.get(user=request.user).Due_Diligence_CA #int value between 1 to 5
        #hundredeight = EQuestions11.objects.get(user=request.user).Marketing #int value between 1 to 5
        #hunderednine = EQuestions11.objects.get(user=request.user).Marketing_Plan_Budget #int value between 1 to 5
        #hundredten = EQuestions11.objects.get(user=request.user).Marketing_Research_Report #int value between 1 to 5
        #hundredeleven = EQuestions11.objects.get(user=request.user).Presentation_Deck #int value between 1 to 5
        #hundredtwelve = EQuestions11.objects.get(user=request.user).Strategic_Tactical_Plan #int value between 1 to 5
        #hundredthirteen = EQuestions12.objects.get(user=request.user).Leadership #int value between 1 to 5
        #hundredfourteen = EQuestions12.objects.get(user=request.user).Management_Experience #int value between 1 to 5
        #hundredfifteen = EQuestions12.objects.get(user=request.user).Consultant_Advisor #int value between 1 to 5 
        #hundredsixteen = EQuestions12.objects.get(user=request.user).Staff #int value between 1 to 5
        #hundredseventeen = EQuestions12.objects.get(user=request.user).Culture #int value between 1 to 5
        #hundredeighteen = EQuestions13.objects.get(user=request.user).Capital_Marketing_Plan #int value between 1 to 5
        #hundrednineteen = EQuestions13.objects.get(user=request.user).Capital_Offering_Documents #int value between 1 to 5
        #hundredtwetnty =  EQuestions13.objects.get(user=request.user).Due_Diligence_IP #int value between 1 to 5
        #hundredtwetntyone = EQuestions13.objects.get(user=request.user).Due_Diligence_LE #int value between 1 to 5
        #hundredtwetntytwo = EQuestions13.objects.get(user=request.user).Due_Diligence_RA #int value between 1 to 5
        #hundredtwentythree = EQuestions13.objects.get(user=request.user).Exit_Strategy #int value between 1 to 5

    except:
        return HttpResponse("Please Go through survey and complete all questions!")    
    # Get all local variables after they have been assigned
    all_variables = locals()
    try:
        a = pay_load_string.objects.get(user=request.user)
        pass
    except:
       pay_load_jsonBody = {
           "email": primary_email,
           "timing": EQuestions.objects.get(user=request.user).Selected_Option2,
           "fundsUse": EQuestions7.objects.get(user=request.user).Selected_Options,
           "entityName": EQuestions2.objects.get(user=request.user).Business_Name,
           "entityType": EQuestions2.objects.get(user=request.user).Selected_Option,
           "mobilePhone": mobile_phone,
           "rangeofCost": EQuestions.objects.get(user=request.user).Selected_Option,
           "display_name": UserDetail.objects.get(user=request.user).First_Name + ' ' + UserDetail.objects.get(user=request.user).Last_Name,
           "exitStrategy": DocumentsPrepared.objects.get(user=request.user).exit_strategy,
           "plannedRaise": EQuestions5.objects.get(user=request.user).Selected_Option,
           "businessPhone": business_phone,
           "currentRounds": EQuestions6.objects.get(user=request.user).Selected_Options,
           "howManyRounds": EQuestions6.objects.get(user=request.user).Selected_Option,
           "primaryAppUse": UserDetail2.objects.get(user=request.user).Primary_Purpose,
           "companyWebsite": UserDetail.objects.get(user=request.user).Company_Website,
           "stageofCompany": EQuestions1.objects.get(user=request.user).Selected_Option,
           "preCapitalRaise": EQuestions3.objects.get(user=request.user).Selected_Option,
           "specialPrograms": UserDetail.objects.get(user=request.user).Special_Programs,
           "virtualDataroom": DocumentsPrepared.objects.get(user=request.user).virtual_data_room,
           "presentationDeck": DocumentsPrepared.objects.get(user=request.user).presentation_deck,
           "capitalPreMarkets":EQuestions4.objects.get(user=request.user).Selected_Options,
           "financialForecast": DocumentsPrepared.objects.get(user=request.user).financial_forecast,
           "offeringDocuments": DocumentsPrepared.objects.get(user=request.user).offering_documents,
           "summaryofOffering": DocumentsPrepared.objects.get(user=request.user).summary_of_offering,
           "companyAffiliation": UserDetail.objects.get(user=request.user).Affiliation,
           "leadershipOverview": DocumentsPrepared.objects.get(user=request.user).leadership_overview,
           "aiGeneratedDeepDive": DocumentsPrepared.objects.get(user=request.user).ai_generated_deep_dive,
           "riskToleranceFounder": EQuestions8.objects.get(user=request.user).Selected_Option,
           "riskToleranceInvestor": EQuestions8.objects.get(user=request.user).Selected_Option2,
           "primaryBusinessAddress": UserDetail.objects.get(user=request.user).Business_Adress,
           "leanBusinessModelCanvas": DocumentsPrepared.objects.get(user=request.user).lean_business_model,
           "entityStateofRegistration": EQuestions2.objects.get(user=request.user).Registration_Region,
           "referralSource": ReferalResponse.objects.get(user=request.user).referral_source,
           "referrerName": ReferalResponse.objects.get(user=request.user).referrer_name,
           "referralOther": ReferalResponse.objects.get(user=request.user).referral_other,
       }
       # objects.create() already saves the instance and triggers post_save once
       # Avoid calling save() again to prevent duplicate webhook calls via the signal
       payloadjson = pay_load_string.objects.create(user=request.user,payLoadString=pay_load_jsonBody)

    # Create a list to store the variable values
    values_list = [value for key, value in all_variables.items() if key != 'request'][13:]
    print(values_list)
    counter = sum(1 for item in values_list if item==1)-2 - sum(1 for item in values_list[103:112] if item == 1)
    all_name_capital = capitalTypes.objects.values_list('name', flat=True)

    dict_name_percentage = {}

    for capital in all_name_capital:
        # Retrieve `matrix_weights` and `counter` safely
        matrix_weight = np.array(CapitalType.objects.get(namec__name=capital).matrix_weights, dtype=np.float64)
        counter_value = CapitalType.objects.get(namec__name=capital).counter

        # Calculate the percentage
        dict_name_percentage[capital] = ((sum(np.array(values_list) * matrix_weight)) * 10) / counter #counter_value
    print (dict_name_percentage)
    def sanitize_value(value):
        if isinstance(value, (np.floating, np.integer)):
            value = float(value)
        if isinstance(value, float):
            if math.isnan(value):
                return None  # Convert NaN to None
            if math.isinf(value):  # Handle infinity cases
                return None
        return value

    dict_name_percentage_sanitized = {k: sanitize_value(v) for k, v in dict_name_percentage.items()}

    # Convert None values to a number that makes sense in your context (e.g., 0 or -1)
    # Alternatively, remove keys with None values if appropriate
    cleaned_percentage = {
        k: v if v is not None else 0  # Replace None with 0 or another appropriate value
        for k, v in dict_name_percentage_sanitized.items()
    }

    # Now sort the dictionary
    keys = list(cleaned_percentage.keys())
    values = list(cleaned_percentage.values())
    sorted_value_index = np.argsort(values)
    sorted_percentage = {keys[i]: values[i] for i in sorted_value_index}

    # Ensure all values are JSON-serializable
    final_percentage = {
        k: float(v) if isinstance(v, (np.floating, np.integer)) else v
        for k, v in sorted_percentage.items()
    }
    final_percentage = capitalCheck(values_list,final_percentage)
    
    # Instead of creating a new record, get_or_create or update existing
    all_match_percentage, created = allCapitalMatchValues.objects.get_or_create(
        user=request.user,
        defaults={'percentage': final_percentage}
    )
    if not created:
        # Update existing record
        allCapitalMatchValues.objects.filter(user=request.user).update(percentage=final_percentage)
    # Try to get existing record for the user
    #try:
    #    all_match_percentage = allCapitalMatchValues.objects.get(user=request.user)
    #    # Update the existing record
    #    all_match_percentage.percentage = final_percentage
    #    all_match_percentage.save()
    #except allCapitalMatchValues.DoesNotExist:
        # Create new record if it doesn't exist
    #    all_match_percentage = allCapitalMatchValues(user=request.user, percentage=final_percentage)
    #    all_match_percentage.save()
    
    try:
        status = Letter_Response.objects.get(user=request.user).top_6_name_output[-1]
    except:
        status = False

    if status == True:
        top_6_name = Letter_Response.objects.get(user=request.user).top_6_name_output
    else:
        sorted_percentage = capitalCheck(values_list,sorted_percentage)
        top_6_name = [item[0] for item in sorted(sorted_percentage.items(), key=lambda item: item[1], reverse=True)[:5]]
    dfcm = pd.DataFrame() # store the data details from database capital market
    
    #try:
    #    id_checker_i = Matches_Purchased.objects.get(user=request.user)
    #    i_id_value = id_checker_i.match_id_i
    #    i_id_value = [int(a) for a in i_id_value]
    #    print(i_id_value)

    #except Matches_Purchased.DoesNotExist:
    #    # Handle the case where no matching record exists
    #    i_id_value = [0]

    #if eightyeight != 5:
    #    try:
    #        i1data = list(IQuestions1.objects.filter(I_Type__in = ['Technical Writer','Content Creator','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        pass
    #        i1data = [] # replace every [None] with 0 and change line 790 list aprehension
    #else:
    #    i1data = []               
    # wrote code to retrieve the rows where either the technical writer is 1 or business consultant is 1 or content creator is 1

    #if eightynine !=5:
    #    try:
    #        i2data = list(IQuestions1.objects.filter(I_Type__in = ['Marketing Analyst','Content Creator','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        pass
    #        i2data = []
    #else:        
    #    i2data = []                     
    
    #if ninety !=5:
    #    try:
    #        i3data = list(IQuestions1.objects.filter(I_Type__in = ['Business Plan Writer','Content Creator','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i3data = []
    #else:
    #    i3data = []                    

    #if ninetyone !=5:
    #    try:
    #        i4data = list(IQuestions1.objects.filter(I_Type__in = ['Attorney - Business Law','Attorney - Corporate Law','Attorney - Securities Law','Business Consultant','Researcher'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i4data = []
    #else:
    #    i4data = []                

    #if ninetytwo !=5:
    #    try:
    #        i5data = list(IQuestions1.objects.filter(I_Type__in = ['Subject Matter Expert','Researcher','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i5data = []
    #else:
    #    i5data = []                    

    #if ninetythree !=5:
    #    try:
    #        i6data = list(IQuestions1.objects.filter(I_Type__in = ['Techical Writer','Business Consultant','Content Creator'] ).exclude(id__in=i_id_value).values())
    #    except:
    #       i6data = []
    #else:
    #    i6data = []                  
    
    #if ninetyfour !=5:
    #    try:
    #        i7data = list(IQuestions1.objects.filter(I_Type__in = ['Business Analyst','Business Consultant','Data Entry'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i7data = []
    #else:
    #    i7data = []                    

    #if ninetyfive !=5:
    #    try:
    #        i8data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i8data = []
    #else:
    #    pass
    #    i8data = []

        

    #if ninetysix !=5:
    #    try:
    #        i9data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','CPA'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i9data = []
    #else:
    #    i9data = []                           

    #if ninetyseven !=5:
    #    try:
    #        i10data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','CPA'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i10data = []
    #else:
    #    i10data = []                    

    #if ninetyeight !=5:
    #    try:
    #        i11data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','Financial Modeler'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i11data = []
    #else:
    #    i11data = []                   

    #if ninetynine !=5:
    #    try:
    #        i12data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','Financial Modeler'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i12data = []
    #else:
    #    i12data = []                    

    #if hundred !=5:
    #    try:
    #        i13data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','Business Analyst'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i13data = []
    #else:
    #    i13data = []

    #if hundredone !=5:
    #    try:
    #        i14data = list(IQuestions1.objects.filter(I_Type__in = ['Financial Analyst','Accountant','CPA'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i14data = []
    #else:
    #    i14data = []


    #if hundredtwo !=5:
    #    try:
    #        i15data = list(IQuestions1.objects.filter(I_Type__in = ['Valuation Analyst','Accountant','Banker'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i15data = []
    #else:
    #    i15data = []            

    #if hundredthree !=5:
    #    try:
    #        i16data = list(IQuestions1.objects.filter(I_Type__in = ['Valuation Analyst','Accountant','Banker'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i16data = []
    #else:
    #    i16data = []                    
#
    #if hundredfour !=5:
    #    try:
    #        i17data = list(IQuestions1.objects.filter(I_Type__in = ['Technical Writer','Business Consultant','Content Creator'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i17data = []
    #else:
    #    i17data = []            
#
    #if hundredfive !=5:
    #    try:
    #        i18data = list(IQuestions1.objects.filter(I_Type__in = ['Web Developer','Marketing Consultant','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i18data = []
    #else:
    #    i18data = []                
#
    #if hundredsix !=5:
    #    try:
    #        i19data = list(IQuestions1.objects.filter(I_Type__in = ['Transfer Agency','Accountant','Business Consultant'] ).exclude(id__in=i_id_value).values())
    #    except:
    #        i19data = []
    #else:
    #    i19data = []               
#
    #if hundredseven !=5:
    #    try:
    #        i20data = list(IQuestions1.objects.filter(I_Type__in = ['Marketing Analyst','Marketing Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i20data = []
    #else:
    #    i20data = []            
#
    #if hundredeight !=5:
    #    try:
    #        i21data = list(IQuestions1.objects.filter(I_Type__in = ['Marketing Analyst','Marketing Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i21data = []
    #else:
    #    i21data = []           
#
    #if hunderednine !=5:
    #    try:
    #        i22data = list(IQuestions1.objects.filter(I_Type__in = ['Marketing Analyst','Marketing Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i22data = []
    #else:
    #    i22data = []                   
#
    #if hundredten !=5:
    #    try:
    #        i23data = list(IQuestions1.objects.filter(I_Type__in = ['Marketing Analyst','Marketing Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i23data = []
    #else:
    #    i23data = []                    
#
    #if hundredeleven !=5:
    #    try:
    #        i24data = list(IQuestions1.objects.filter(I_Type__in = ['Graphic Designer','Marketing Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i24data = []
    #else:
    #    i24data = []                   
#
    #if hundredtwelve !=5:
    #    try:
    #        i25data = list(IQuestions1.objects.filter(I_Type__in = ['Business Plan Writer','Content Writer','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i25data = []
    #else:
    #    i25data = []                    
#
    #if hundredthirteen !=5:
    #    try:
    #        i26data = list(IQuestions1.objects.filter(I_Type__in = ['HR Due Diligence','Management Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i26data = []
    #else:
    #    i26data = []                    

    #if hundredfourteen !=5:
    #    try:
    #        i27data = list(IQuestions1.objects.filter(I_Type__in = ['HR Due Diligence','Management Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i27data = []
    #else:
    #    i27data = []                    
#
    #if hundredfifteen !=5:
    #    try:
    #        i28data = list(IQuestions1.objects.filter(I_Type__in = ['Business Analyst','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i28data = []
    #else:
    #    i28data = []                   
#
    #if hundredsixteen !=5:
    #    try:
    #        i29data = list(IQuestions1.objects.filter(I_Type__in = ['Business Analyst','HR Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i29data = []        
    #else:
    #    i29data = []
#
    #if hundredseventeen !=5:
    #    try:
    #        i30data = list(IQuestions1.objects.filter(I_Type__in = ['Subject Matter Expert','HR Consultant','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i30data = []        
    #else:
    #    i30data = []
#
    #if hundredeighteen !=5:
    #    try:
    #        i31data = list(IQuestions1.objects.filter(I_Type__in = ['Broker Agency','Platform','Marketing Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i31data = []
    #else:
    #    i31data = []                   
#
    #if hundrednineteen !=5:
    #    try:
    #        i32data = list(IQuestions1.objects.filter(I_Type__in = ['Attorney - Securities Law','Paralegal','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i32data = []        
    #else:
    #    i32data = []
#
    #if hundredtwetnty !=5:
    #    try:
    #        i33data = list(IQuestions1.objects.filter(I_Type__in = ['Attorney - Intelectual Property','Legal Assistant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i33data = []
    #else:
    #    i33data = []                   
#
    #if hundredtwetntyone !=5:
    #    try:
    #        i34data = list(IQuestions1.objects.filter(I_Type__in = ['Attorney - Business Law','Paralegal','Legal Assistant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i34data = []
    #else:
    #    i34data = []                    
#
    #if hundredtwetntytwo !=5:
    #    try:
    #        i35data = list(IQuestions1.objects.filter(I_Type__in = ['Risk Analyst','Underwriter','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i35data = []    
    #else:
    #    i35data = []
#
    #if hundredtwentythree !=5:
    #    try:
    #        i36data = list(IQuestions1.objects.filter(I_Type__in = ['Attorney - Business Law','CPA','Business Consultant']).exclude(id__in=i_id_value).values())
    #    except:
    #        i36data = []
    #else:
    #    i36data = []            
#
    #all_i_data = i1data+i2data+i3data+i4data+i5data+i6data+i7data+i8data+i9data+i10data+i11data+\
    #i12data+i13data+i14data+i15data+i16data+i17data+i18data+i19data+i20data+i21data+i22data+i23data+\
    #i24data+i25data+i26data+i27data+i28data+i29data+i30data+i31data+i32data+i33data+i34data+i35data+i36data 
    #all_i_data_f = pd.DataFrame(all_i_data)
    #all_i_data_f = all_i_data_f.drop_duplicates()
    #print(all_i_data_f)
    #intermediaries = len(all_i_data_f)

    cm1name = top_6_name[0] 
    cm2name = top_6_name[1]
    cm3name =  top_6_name[2]
    cm4name = top_6_name[3]
    cm5name = top_6_name[4]
    #cm6name = top_6_name[5]
    
    # Create capital type record for the user
    create_capital_type_for_user(request.user, cm1name)

    try:
        id_checker_cm = Matches_Purchased.objects.get(user=request.user)
        cm_id_value = id_checker_cm.match_id_cm
        cm_id_value = [0 if type(a) != int else int(a) for a in cm_id_value]

    except Matches_Purchased.DoesNotExist:
        # Handle the case where no matching record exists
        cm_id_value = [0]


    try:
        cm1num = VQuestion1.objects.filter(CM_Type = cm1name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm1data = list(VQuestion1.objects.filter(CM_Type=cm1name).exclude(id__in=cm_id_value).values())
    except:
        cm1num = 0
    try:
        cm2num = VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm2data = list(VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).values())
    except:
        cm2num = 0
    try:
        cm3num = VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm3data = list(VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in= cm_id_value).values())
    except:
        cm3num = 0
    try:    
        cm4num = VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm4data = list(VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).values())
    except:
        cm4num = 0
    try:    
        cm5num =VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm5data = list(VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).values())
    except:
        cm5num = 0
    #try:   
    #    cm6num = VQuestion1.objects.filter(CM_Type = cm6name ).exclude(id__in=cm_id_value).count() # should be replaced after database
    #    cm6data = list(VQuestion1.objects.filter(CM_Type = cm6name ).exclude(id__in=cm_id_value).values())
    #except:
    #    cm6num = 0

    cm_type_count = 1 
    total_matches = cm1num +cm2num#+cm3num+cm4num+cm5num#+cm6num # should be replaced after database    
    price = 25 # need to discuss on this
    totalprice = price * total_matches

    if total_matches >= 100:
        discount = 0.2 * totalprice

    elif total_matches >=200:
        discount = 0.4*totalprice

    else:
        discount = 0    
    balancedue = totalprice - discount

    #For POST data for user purchase of matches:
    try:
        report = Matches_Purchased.objects.get(user=request.user)

    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=request.user)

    #intermediaries = len(all_i_data_f)

    #For Backend API request of purchases done
    try:
        optionsapi = Purchases.objects.get(user=request.user)

    except Purchases.DoesNotExist:
        optionsapi = Purchases(user=request.user) 

    optionapi1 = optionsapi.cm1purchase
    optionapi2 = optionsapi.cm2purchase
    optionapi3 = optionsapi.cm3purchase
    optionapi4 = optionsapi.cm4purchase
    optionapi5 = optionsapi.cm5purchase
    optionapi6 = optionsapi.cm6purchase
    ipurchase = optionsapi.ipurchase

    try:
        cm1dataapi = random.sample(cm1data,optionapi1)
    except:
        cm1dataapi = cm1dataapi[:optionapi1]  
    #try:          
    #    cm2dataapi = random.sample(cm2data,optionapi2)
    #except:
    #    cm2dataapi = cm2dataapi[:optionapi2]
    #try:              
    #    cm3dataapi = random.sample(cm3data,optionapi3)
    #except:
    #    cm3dataapi= cm3dataapi[:optionapi3]
    #try:
    #    cm4dataapi = random.sample(cm4data,optionapi4)
    #except:
    #    cm4dataapi= cm4dataapi[:optionapi4] 
    #try:           
    #    cm5dataapi = random.sample(cm5data,optionapi5)
    #except:
    #    cm5dataapi= cm5dataapi[:optionapi5]
    #try:        
    #    cm6dataapi = random.sample(cm6data,optionapi6)
    #except:
    #    cm6dataapi = cm6dataapi[:optionapi6]
            
    all_data_api = cm1dataapi #+cm2dataapi+cm3dataapi+cm4dataapi+cm5dataapi+cm6dataapi
    id_CM_api =   cm_id_value+[int(a['id']) for a in all_data_api]
    report.match_id_cm = id_CM_api
    #all_i_data_api = random.sample(all_i_data_api,option7)
    #id_i =  i_id_value + [0 if a is None else int(a['id']) for a in all_i_data] #[int(a['id']) for a in all_i_data]
    #report.match_id_i = id_i

    #dfim = all_i_data_f
    #dfim = dfim.drop_duplicates()
    #dfim = dfim.sample(n=option7)
    dfcm = pd.DataFrame(all_data_api)
    #print(dfim.head())


    #print(dfcm.head())
    # Convert the DataFrame to JSON
    json_data_api = dfcm.to_json(orient='split')
    optionsapi.cm_matches = json_data_api
    optionsapi.save()
    #json_data_i = dfim.to_json(orient='records')
#END FOR API DATA RETRIEVAL FROM DATABASE

#    if request.method == 'POST':
#        # Get input values from the POST data
#        option1 = int(request.POST.get( cm1name, 0))
#        option2 = int(request.POST.get( cm2name , 0))
#        option3 = int(request.POST.get(cm3name , 0))
#        option4 = int(request.POST.get( cm4name, 0))
#        option5 = int(request.POST.get( cm5name, 0))
#        #option6 = int(request.POST.get( cm6name , 0))
#        option7 = int(request.POST.get( 'option7', 0))
#        #print(option1,option2)
#
#       try:
#            cm1data = random.sample(cm1data,option1)
#        except:
#            cm1data = cm1data[:option1]  
#        try:          
#            cm2data = random.sample(cm2data,option2)
#        except:
#            cm2data = cm2data[:option2]
#        try:              
#            cm3data = random.sample(cm3data,option3)
#        except:
#            cm3data= cm3data[:option3]
#       try:
#            cm4data = random.sample(cm4data,option4)
#        except:
#            cm4data= cm4data[:option4] 
#        try:           
#            cm5data = random.sample(cm5data,option5)
#        except:
#            cm5data= cm5data[:option5]
        #try:        
        #    cm6data = random.sample(cm6data,option6)
        #except:
        #    cm6data = cm6data[:option6]
            
#        all_data = cm1data +cm2data+cm3data+cm4data+cm5data#+cm6data
#        id_CM =   cm_id_value+[int(a['id']) for a in all_data]
#        report.match_id_cm = id_CM
        #try:
        #    all_i_data_f = all_i_data_f.sample(n=option7)
        #except:
        #    all_i_data_f = all_i_data_f.sample(n=0)
        #id_i =  i_id_value + [0 if a is None else int(a['id']) for index, a in all_i_data_f.iterrows()] #[int(a['id']) for a in all_i_data]
        #report.match_id_i = id_i

        #dfim = all_i_data_f
        #dfim = dfim.drop_duplicates()
        #try:
        #    dfim = dfim.sample(n=option7)
        #except:
        #    dfim = dfim.sample(n=0)    
#        dfcm = pd.DataFrame(all_data)
        #print(dfim.head())


        #print(dfcm.head())
        # Convert the DataFrame to JSON
#        json_data = dfcm.to_json(orient='records')
        #json_data_i = dfim.to_json(orient='records')

        #Conveert the DataFrame to CSV
#        csv_data = dfcm.to_csv(index=False)
        #csv_data_i = dfim.to_csv(index=False)

        # To HTML table
#        html_table = dfcm.to_html()
        #html_table_2 = dfim.to_html()

#        purchase_dict = {cm1name:option1,cm2name:option2,cm3name:option3,cm4name:option4,cm5name:option5,'intermediaries':option7}#cm6name:option6}

        # Calculate total_num, total_price, discount, and balance_due
#        total_num = option1 #+ option2 + option3 + option4 + option5 + option6 + option7
#        price = 25 # Example price, this could be dynamic
#        total_price = total_num * price

        # Calculate discount
#        if total_num > 200:
#            discount = 0.4 * total_price
#        elif total_num > 100:
#            discount = 0.2 * total_price
#        else:
#            discount = 0

#        balance_due = total_price - discount

        # Save the data to the model
#        report.purchased_matches = json.dumps(purchase_dict)
#        report.total_num = total_num
#        report.total_price = total_price
#        report.discount = discount
#        report.balance_due = balance_due
#        report.price = price
        # Save the model instance
#        report.save()    

#        return render(request,'finfo.html',{'table':html_table,'list_name':top_6_name})#,'table_i':html_table_2})
        # Redirect to the same page to display the updated data
        #return JsonResponse(json_data, safe=False)

#        response = HttpResponse(csv_data, content_type='text/csv')
#        response['Content-Disposition'] = 'attachment; filename="data.csv"'

#        return response

    output_list = top_6_name

    # In the dictionary pdf_documents for the final pdf download to properly work, definition should come first,faq second and tewelve variable report third. This order determines the order in the letter.
    pdf_documents = {
        'Accelerator' : [accelerator.accelerator(request),accelerator.acceleratorfaq(request),accelerator.acceleratortwelve(request)],
        'Bonds' : [bonds.bonds(request),bonds.bondsfaq(request),bonds.bondstwelve(request)],
        'Bootstrapped' : [bootstrapped.bootstrapped(request),bootstrapped.bootstrappedfaq(request),bootstrapped.bootstrappedtwelve(request)],
        'Commercial Banking' : [commercialbanking.commercialbanking(request),commercialbanking.commercialbankingfaq(request),commercialbanking.commercialbankingtwelve(request)],
        'Cryptocurrency' : [cryptocurrency.cryptocurrency(request),cryptocurrency.cryptocurrencyfaq(request),cryptocurrency.cryptocurrencytwelve(request)],
        'Factoring' : [factoring.factoring(request),factoring.factoringfaq(request),factoring.factoringtwelve(request)],
        'Grants' : [grants.grants(request),grants.grantsfaq(request),grants.grantstwelve(request)],
        'Hedge Funds' : [hedgefunds.hedgefunds(request),hedgefunds.hedgefundsfaq(request),hedgefunds.hedgefundstwelve(request)],
        'Incubator' : [incubator.incubator(request),incubator.incubatorfaq(request),incubator.incubatortwelve(request)],
        'Investment Banking' : [investmentbanking.investmentbanking(request),investmentbanking.investmentbankingfaq(request),investmentbanking.investmentbankingtwelve(request)],
        'Private Debt' : [privatedebt.privatedebt(request),privatedebt.privatedebtfaq(request),privatedebt.privatedebttwelve(request)],
        'Private Equity Securities' : [privateequitysecurities.privateequitysecurities(request),privateequitysecurities.privateequitysecuritiesfaq(request),privateequitysecurities.privateequitysecuritiestwelve(request)],
        'Royalty Financing' : [royaltyfinancing.royaltyfinancing(request),royaltyfinancing.royaltyfinancingfaq(request),royaltyfinancing.royaltyfinancingtwelve(request)],
        'Small Business Administration (SBA)' : [SmallBusinessAdministration.SmallBusinessAdministration(request),SmallBusinessAdministration.SmallBusinessAdministrationfaq(request),SmallBusinessAdministration.SmallBusinessAdministrationtwelve(request)],
        'Third Party Corporate Credit' : [thirdpartycorporatecredit79.thirdpartycorporatecredit(request),thirdpartycorporatecredit79.thirdpartycorporatecreditfaq(request),thirdpartycorporatecredit79.thirdpartycorporatecredittwelve(request)],
        'Tokenization' : [tokenization80.tokenization(request),tokenization80.tokenizationfaq(request),tokenization80.tokenizationtwelve(request)],
        'Venture Capital' : [venturecapital.venturecapital(request),venturecapital.venturecapitalfaq(request),venturecapital.venturecapitaltwelve(request)],
        }
    
    # Definition,faq and twelvev variables would http content and decode it to utf-8 from the http response object for top capital market match which would be used to generate pdf. 
    definition = "Short term solution" # mark_safe(pdf_documents[cm1name][0].content.decode('utf-8'))
    faq_que = "Short term solution" #mark_safe(pdf_documents[cm1name][1].content.decode('utf-8'))
    twelvev = "Short term solution" #mark_safe(pdf_documents[cm1name][2].content.decode('utf-8'))
    cost_dict = {
        'Accelerator': '$2,500 to $25,000',
        'Bonds' : '$50,000 to $250,000',
        'Bootstrapped' : '0 to $5,000',
        'Commercial Banking': '0 to $5,000',
        'Cryptocurrency' : '$1,000 to 25,000',
        'Factoring' : '0 to $5,000',
        'Grants' : '$250 to $10,000',
        'Hedge Funds' : '$10,000 to $25,000',
        'Incubator' : '0 to $25,000',
        'Investment Banking' : '$20,000 to $75,000',
        'Private Debt' : '0 to $5,000',
        'Royalty Financing': '$2,500 to $10,000',
        'Third Party Corporate Credit': '$10,000 to $25,000',     
        'Private Equity Securities' : '$25,000 to $150,000',
        'Venture Capital' : '$25,000 $150,000',
        'Tokenization' : '$1,000 to $15,000',
        'Small Business Administration (SBA)' : '$500 to $2,500',
    }
    
    context = {
        'date':date,
        'firstname':firstname,
        'lastname':lastname,
        'address':primary_business_adress,
        'phone' :business_phone,
        'secondphone':UserDetail.objects.get(user=request.user).Mobile_Phone,
        'email': primary_email,
        'businessname' : company_name,
        'count': cm_type_count,
        'fundgoal': fundgoal,
        'totalnum': total_matches,
        'cm1name': cm1name,
        'cm1nameoutput':output_list[0],
        #'definition1':definitions[output_list[0]],
        'cm2name': cm2name,
        'cm2nameoutput': output_list[1],
        #'definition2':definitions[output_list[1]],
        'cm3name': cm3name,
        'cm3nameoutput': output_list[2],
        'cm4name': cm4name,
        'cm5name': cm5name,
        #'cm6name': cm6name,
        'cm1no':cm1num,
        'cm2no':cm2num,
        'cm3no':cm3num,
        'cm4no':cm4num,
        'cm5no':cm5num,
        #'cm6no':cm6num,
        #'i':intermediaries,
        'price':price,
        'totalprice':totalprice,
        'discount':discount,
        'balancedue':balancedue,
        'report':report,
        'list_name':top_6_name,
        'info':info,
        'definition' : definition,
        'faq_que' : faq_que,
        'twelvev' : twelvev,
        #'cost' : cost_dict[cm1name],
        #'one':info[str(cm1name)],
        #'two':info[str(cm2name)],
        #'three':info[str(cm3name)],
        #'four':info[str(cm4name)],
        #'five':info[str(cm5name)],
        #'six':info[str(cm6name)],
    }

    #Saving individual variable for output to share in api endpoint
    try:
        output = Letter_Response.objects.get(user=request.user)

    except Letter_Response.DoesNotExist:
        output = Letter_Response(user=request.user)

    output.firstname = firstname
    output.lastname = lastname
    output.address = primary_business_adress
    output.phone = business_phone
    output.email = primary_email
    output.businessname = company_name
    output.count = cm_type_count
    output.fundgoal = fundgoal
    output.totalnum = total_matches
    output.cm1name = cm1name
    output.cm2name = cm2name
    output.cm3name = cm3name
    output.cm4name = cm4name
    output.cm5name = cm5name
    #output.cm6name = cm6name
    output.cm1no = cm1num
    output.cm2no = cm2num
    output.cm3no = cm3num
    output.cm4no = cm4num
    output.cm5no = cm5num
    #output.cm6no = cm6num
    #output.intermediaries = intermediaries
    output.price = price
    output.totalprice = totalprice
    output.discount = discount
    output.balancedue = balancedue
    output.top_6_name = top_6_name
    output.top_6_name_output = output_list
    #output.infocm1 = info[str(cm1name)]
    #output.infocm2 = info[str(cm2name)]
    #output.infocm3 = info[str(cm3name)]
    #output.infocm4 = info[str(cm4name)]
    #output.infocm5 = info[str(cm5name)]
    #output.infocm6 = info[str(cm6name)]
    output.save()


    
    rendered_html = render_to_string('letter.html',context)
    try:
        # Try to retrieve the existing Match_Data for the user
        html_data = Match_Data.objects.get(user=request.user)
        # Update the html content if the object already exists
        html_data.html = rendered_html
        html_data.save()

    except Match_Data.DoesNotExist:
        # If no Match_Data exists for the user, create a new one
        html_data = Match_Data(user=request.user, html=rendered_html)
        html_data.save()

    return render(request,'thankyouresponse.html',context)

@login_required
def faq(request):
    try:
        list_of_top_capital_output =Letter_Response.objects.get(user=request.user).top_6_name_output
        if list_of_top_capital_output[-1] == True:
            list_of_top_capital_output =list_of_top_capital_output[:-1]    
    except:
        return HttpResponse("please complete the Survey to get the report!")
    
    # Check if each link resolves to a valid URL
    links_with_error = []
    for link in list_of_top_capital_output:
        modified_link = link + 'faq'
        try:
            reverse(modified_link)  # Try to resolve the link
        except NoReverseMatch:
            links_with_error.append(modified_link)  # Only append the modified link once

    cap_list = {
        "list_name_output": list_of_top_capital_output,
        "links_with_error": links_with_error
    }

    return render(request, 'FAQ.html', cap_list)

@login_required
def definition(request):
    try:
        list_of_top_capital_output =Letter_Response.objects.get(user=request.user).top_6_name_output
        if list_of_top_capital_output[-1] == True:
            list_of_top_capital_output =list_of_top_capital_output[:-1]    
    except:
        return HttpResponse("please complete the Survey to get the report!")

    # Check if each link resolves to a valid URL
    links_with_error = []
    for link in list_of_top_capital_output:
        try:
            reverse(link)  # Try to resolve the link
        except NoReverseMatch:
            links_with_error.append(link)

    cap_list = {"list_name_output":list_of_top_capital_output,
    'links_with_error': links_with_error}

    return render(request,'definition.html',cap_list)

@login_required
def twelvevariable(request):
    try:
        list_of_top_capital_output =Letter_Response.objects.get(user=request.user).top_6_name_output
        if list_of_top_capital_output[-1] == True:
            list_of_top_capital_output =list_of_top_capital_output[:-1]    
    except:
        return HttpResponse("please complete the Survey to get the report!")
        
    cap_list ={"list_name_output":list_of_top_capital_output}

   # Check if each link resolves to a valid URL
    links_with_error = []
    for link in list_of_top_capital_output:
        modified_link = link + 'twelve'
        try:
            reverse(modified_link)  # Try to resolve the link
        except NoReverseMatch:
            links_with_error.append(modified_link)  # Only append the modified link once

    cap_list = {
        "list_name_output": list_of_top_capital_output,
        "links_with_error": links_with_error
    }

    return render(request,'twelvevariable.html',cap_list)

@login_required
def summary(request):
    # Contact Information
    try:
        first_name = UserDetail.objects.get(user=request.user).First_Name
        middle_name = UserDetail.objects.get(user=request.user).Middle_Name
        last_name = UserDetail.objects.get(user=request.user).Last_Name
        affiliation = UserDetail.objects.get(user=request.user).Affiliation
        primary_email = UserDetail.objects.get(user=request.user).User_Email
        website = UserDetail.objects.get(user=request.user).Company_Website
        address = UserDetail.objects.get(user=request.user).Business_Adress
        business_phone = UserDetail.objects.get(user=request.user).Business_Phone
        mobile_phone = UserDetail.objects.get(user=request.user).Mobile_Phone
        special_program = UserDetail.objects.get(user=request.user).Special_Programs
        #Account    
        account_type = UserDetail2.objects.get(user=request.user).Account_Type
        billing_options = UserDetail2.objects.get(user=request.user).Billing_Option
        primary_purpose = UserDetail2.objects.get(user=request.user).Primary_Purpose
        #Stage
        stage = EQuestions1.objects.get(user=request.user).Selected_Option
        #Entity
        entity_name = EQuestions2.objects.get(user=request.user).Business_Name
        entity_state = EQuestions2.objects.get(user=request.user).Registration_Region
        entity_type = EQuestions2.objects.get(user=request.user).Selected_Option
        #Pre-Capital
        raised_capital =EQuestions3.objects.get(user=request.user).Selected_Option
        #Pre Market Capital Type
        capital_till_date = EQuestions4.objects.get(user=request.user).Selected_Options
        #Planned Raise
        planned_raise = EQuestions5.objects.get(user=request.user).Selected_Option
        #Rounds
        round_type = EQuestions6.objects.get(user=request.user).Selected_Options
        round_tranches = EQuestions6.objects.get(user=request.user).Selected_Option
        #Use of Funds
        use_of_funds = EQuestions7.objects.get(user=request.user).Selected_Options
        #Risk Assessment
        risk_tolerance_investor = EQuestions8.objects.get(user=request.user).Selected_Option
        risk_tolerance_enterprise = EQuestions8.objects.get(user=request.user).Selected_Option2

        #Up front Cost
        up_front_cost = EQuestions.objects.get(user=request.user).Selected_Option

        #Up front Cost
        up_front_timming = EQuestions.objects.get(user=request.user).Selected_Option2

        #Documents Prepared
        summary_of_offering = DocumentsPrepared.objects.get(user=request.user).summary_of_offering
        financials = DocumentsPrepared.objects.get(user=request.user).financial_forecast
        lean_business_model_canvas = DocumentsPrepared.objects.get(user=request.user).lean_business_model
        presentation_deck = DocumentsPrepared.objects.get(user=request.user).presentation_deck
        leadership_overview = DocumentsPrepared.objects.get(user=request.user).leadership_overview
        exit_strategy = DocumentsPrepared.objects.get(user=request.user).exit_strategy
        offering_documents = DocumentsPrepared.objects.get(user=request.user).offering_documents
        ai_generated_deep_dive = DocumentsPrepared.objects.get(user=request.user).ai_generated_deep_dive
        virtual_data_room = DocumentsPrepared.objects.get(user=request.user).virtual_data_room

    except:
        return HttpResponse("please complete the Survey to get the report!")    
    context = {
        'first_name':first_name,
        'middle_name':middle_name,
        'last_name':last_name,
        'affiliation':affiliation,
        'primary_email':primary_email,
        'website': website,
        'address':address,
        'business_phone':business_phone,
        'mobile_phone':mobile_phone,
        'special_program':special_program,
        'primary_purpose': primary_purpose,
        'account_type':account_type,
        'billing_option':billing_options,
        'stage': stage,
        'entity_name':entity_name,
        'entity_state':entity_state,
        'entity_type':entity_type,
        'raised_capital':raised_capital,
        'capital_till_date':capital_till_date,
        'planned_raise':planned_raise,
        'round_type':round_type,
        'round_tranches':round_tranches,
        'use_of_funds':use_of_funds,
        'risk_tolerance_investor':risk_tolerance_investor,
        'risk_tolerance_enterprise':risk_tolerance_enterprise,
        'up_front_cost':up_front_cost,
        'up_front_timming':up_front_timming,
        'summary_of_offering':summary_of_offering,
        'financials':financials,
        'lean_business_model_canvas':lean_business_model_canvas,
        'presentation_deck':presentation_deck,
        'leadership_overview':leadership_overview,
        'exit_strategy':exit_strategy,
        'offering_documents':offering_documents,
        'ai_generated_deep_dive':ai_generated_deep_dive,
        'virtual_data_room':virtual_data_room,
        }
        
    return render(request,'summary_of_response.html',context)



#############CONVERTING TO PDF################################################################
@token_or_session_required
def pdf(request):
    try:
        #Lending requirements
        try:
            collateral_status_check =LendingRequirements.objects.get(user=request.user).collateral_status
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: (LendingRequirements.collateral_status)")
        try:
            credit_score_check = LendingRequirements.objects.get(user=request.user).credit_score
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: (LendingRequirements.credit_score)")     
        try:
            criminal_history_check = LendingRequirements.objects.get(user=request.user).criminal_history
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: (LendingRequirements.criminal_history)")        
        
        # UserDetail fields
        try:
            firstname = UserDetail.objects.get(user=request.user).First_Name #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: firstname (UserDetail.First_Name)")
        
        try:
            lastname = UserDetail.objects.get(user=request.user).Last_Name #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: lastname (UserDetail.Last_Name)")
        
        date = datetime.now().strftime('%B %d, %Y') #no need
        
        try:
            primary_business_adress = UserDetail.objects.get(user=request.user).Business_Adress #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: primary_business_adress (UserDetail.Business_Adress)")
        
        try:
            business_phone = UserDetail.objects.get(user=request.user).Business_Phone #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: business_phone (UserDetail.Business_Phone)")
        
        try:
            fundgoal = EQuestions5.objects.get(user=request.user).Selected_Option[:] # string based on question of how much capital user want to raise
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fundgoal (EQuestions5.Selected_Option)")
        
        try:
            mobile_phone = UserDetail.objects.get(user=request.user).Mobile_Phone #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: mobile_phone (UserDetail.Mobile_Phone)")
        
        try:
            primary_email = UserDetail.objects.get(user=request.user).User_Email #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: primary_email (UserDetail.User_Email)")
        
        try:
            company_website = UserDetail.objects.get(user=request.user).Company_Website #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: company_website (UserDetail.Company_Website)")
        
        try:
            company_name = EQuestions2.objects.get(user=request.user).Business_Name #string
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: company_name (EQuestions2.Business_Name)")
        
        # EQuestions1 fields
        try:
            one = EQuestions1.objects.get(user=request.user).Idea #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: one (EQuestions1.Idea)")
        
        try:
            two = EQuestions1.objects.get(user=request.user).Formation #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: two (EQuestions1.Formation)")
        
        try:
            three = EQuestions1.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: three (EQuestions1.Start_Up)")
        
        try:
            four = EQuestions1.objects.get(user=request.user).Growth #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: four (EQuestions1.Growth)")
        
        try:
            five = EQuestions1.objects.get(user=request.user).M_And_A #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: five (EQuestions1.M_And_A)")
        
        try:
            six = EQuestions1.objects.get(user=request.user).Preparing_For_Public #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: six (EQuestions1.Preparing_For_Public)")
        
        try:
            seven = EQuestions1.objects.get(user=request.user).Distressed #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seven (EQuestions1.Distressed)")
        
        # EQuestions2 fields
        try:
            eight = EQuestions2.objects.get(user=request.user).No_Business #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eight (EQuestions2.No_Business)")
        
        try:
            nine = EQuestions2.objects.get(user=request.user).Sole_Proprietorship #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: nine (EQuestions2.Sole_Proprietorship)")
        
        try:
            ten = EQuestions2.objects.get(user=request.user).LLC #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ten (EQuestions2.LLC)")
        
        try:
            eleven = EQuestions2.objects.get(user=request.user).LP #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eleven (EQuestions2.LP)")
        
        try:
            twelve = EQuestions2.objects.get(user=request.user).GP #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twelve (EQuestions2.GP)")
        
        try:
            thirteen = EQuestions2.objects.get(user=request.user).S_Corporation #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirteen (EQuestions2.S_Corporation)")
        
        try:
            fourteen = EQuestions2.objects.get(user=request.user).C_Corp #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourteen (EQuestions2.C_Corp)")
        
        try:
            fifteen = EQuestions2.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fifteen (EQuestions2.Other)")
        
        # EQuestions3 fields
        try:
            sixteen = EQuestions3.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixteen (EQuestions3.Less_25k)")
        
        try:
            seventeen = EQuestions3.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventeen (EQuestions3.More_25K_Less_100k)")
        
        try:
            eighteen = EQuestions3.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eighteen (EQuestions3.More_100k_Less_250K)")
        
        try:
            nineteen = EQuestions3.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: nineteen (EQuestions3.More_250k_Less_500K)")
        
        try:
            twenty = EQuestions3.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twenty (EQuestions3.More_500K_Less_1M)")
        
        try:
            twentyone = EQuestions3.objects.get(user=request.user).More_1M_Less_2M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentyone (EQuestions3.More_1M_Less_2M)")
        
        try:
            twentytwo = EQuestions3.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentytwo (EQuestions3.More_2M_Less_5M)")
        
        try:
            twentythree = EQuestions3.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentythree (EQuestions3.More_5M_Less_10M)")
        
        try:
            twentyfour = EQuestions3.objects.get(user=request.user).More_10M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentyfour (EQuestions3.More_10M)")
        
        # EQuestions4 fields
        try:
            twentyfive = EQuestions4.objects.get(user=request.user).Accelerator #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentyfive (EQuestions4.Accelerator)")
        
        try:
            twentysix = EQuestions4.objects.get(user=request.user).Bonds #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentysix (EQuestions4.Bonds)")
        
        try:
            twentyseven = EQuestions4.objects.get(user=request.user).Comercial_Banking #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentyseven (EQuestions4.Comercial_Banking)")
        
        try:
            twentyeight = EQuestions4.objects.get(user=request.user).Cryptocurrency #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentyeight (EQuestions4.Cryptocurrency)")
        
        try:
            twentynine = EQuestions4.objects.get(user=request.user).EB5_Immigration #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: twentynine (EQuestions4.EB5_Immigration)")
        
        try:
            thirty = EQuestions4.objects.get(user=request.user).Enterprise_Zones #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirty (EQuestions4.Enterprise_Zones)")
        
        try:
            thirtyone = EQuestions4.objects.get(user=request.user).Factoring #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtyone (EQuestions4.Factoring)")
        
        try:
            thirtytwo = EQuestions4.objects.get(user=request.user).Grants #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtytwo (EQuestions4.Grants)")
        
        try:
            thirtythree = EQuestions4.objects.get(user=request.user).Hedge_Funds #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtythree (EQuestions4.Hedge_Funds)")
        
        try:
            thirtyfour = EQuestions4.objects.get(user=request.user).Incubator #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtyfour (EQuestions4.Incubator)")
        
        try:
            thirtyfive = EQuestions4.objects.get(user=request.user).Investment_Banking #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtyfive (EQuestions4.Investment_Banking)")
        
        try:
            thirtysix = EQuestions4.objects.get(user=request.user).Other_Owner_Equity #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtysix (EQuestions4.Other_Owner_Equity)")
        
        try:
            thirtyseven = EQuestions4.objects.get(user=request.user).Private_Debt #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtyseven (EQuestions4.Private_Debt)")
        
        try:
            thirtyeight = EQuestions4.objects.get(user=request.user).Private_Equity #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtyeight (EQuestions4.Private_Equity)")
        
        try:
            thirtynine = EQuestions4.objects.get(user=request.user).Public_Offereing #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: thirtynine (EQuestions4.Public_Offereing)")
        
        try:
            fourty = EQuestions4.objects.get(user=request.user).Real_Estate #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourty (EQuestions4.Real_Estate)")
        
        try:
            fourtyone = EQuestions4.objects.get(user=request.user).Royalty_Financing #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtyone (EQuestions4.Royalty_Financing)")
        
        try:
            fourtytwo = EQuestions4.objects.get(user=request.user).Small_Business_Administration #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtytwo (EQuestions4.Small_Business_Administration)")
        
        try:
            fourtythree = EQuestions4.objects.get(user=request.user).Venture_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtythree (EQuestions4.Venture_Capital)")
        
        try:
            fourtyfour = EQuestions4.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtyfour (EQuestions4.Unsure)")
        
        # EQuestions5 fields
        try:
            fourtyfive = EQuestions5.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtyfive (EQuestions5.Less_25k)")
        
        try:
            fourtysix = EQuestions5.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtysix (EQuestions5.More_25K_Less_100k)")
        
        try:
            fourtyseven = EQuestions5.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtyseven (EQuestions5.More_100k_Less_250K)")
        
        try:
            fourtyeight = EQuestions5.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtyeight (EQuestions5.More_250k_Less_500K)")
        
        try:
            fourtynine = EQuestions5.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fourtynine (EQuestions5.More_500K_Less_1M)")
        
        try:
            fifty = EQuestions5.objects.get(user=request.user).More_1M_Less_1_35M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fifty (EQuestions5.More_1M_Less_1_35M)")
        
        try:
            fiftyone = EQuestions5.objects.get(user=request.user).More_1_35M_Less_2M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftyone (EQuestions5.More_1_35M_Less_2M)")
        
        try:
            fiftytwo = EQuestions5.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftytwo (EQuestions5.More_2M_Less_5M)")
        
        try:
            fiftythree = EQuestions5.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftythree (EQuestions5.More_5M_Less_10M)")
        
        try:
            fiftyfour = EQuestions5.objects.get(user=request.user).More_10M_Less_20M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftyfour (EQuestions5.More_10M_Less_20M)")
        
        try:
            fiftyfive = EQuestions5.objects.get(user=request.user).More_20M #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftyfive (EQuestions5.More_20M)")
        
        try:
            fiftysix = EQuestions5.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftysix (EQuestions5.Unsure)")
        
        # EQuestions6 fields
        try:
            fiftyseven = EQuestions6.objects.get(user=request.user).Founders_Round #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftyseven (EQuestions6.Founders_Round)")
        
        try:
            fiftyeight = EQuestions6.objects.get(user=request.user).Pre_Seed #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftyeight (EQuestions6.Pre_Seed)")
        
        try:
            fiftynine = EQuestions6.objects.get(user=request.user).Seed #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: fiftynine (EQuestions6.Seed)")
        
        try:
            sixty = EQuestions6.objects.get(user=request.user).Series_A #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixty (EQuestions6.Series_A)")
        
        try:
            sixtyone = EQuestions6.objects.get(user=request.user).Series_B #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtyone (EQuestions6.Series_B)")
        
        try:
            sixtytwo = EQuestions6.objects.get(user=request.user).Series_C #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtytwo (EQuestions6.Series_C)")
        
        try:
            sixtythree = EQuestions6.objects.get(user=request.user).Pre_Ipo #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtythree (EQuestions6.Pre_Ipo)")
        
        try:
            sixtyfour = EQuestions6.objects.get(user=request.user).Ipo #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtyfour (EQuestions6.Ipo)")
        
        try:
            sixtyfive = EQuestions6.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtyfive (EQuestions6.Unsure)")
        
        try:
            sixtysix = EQuestions6.objects.get(user=request.user).One #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtysix (EQuestions6.One)")
        
        try:
            sixtyseven = EQuestions6.objects.get(user=request.user).Two #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtyseven (EQuestions6.Two)")
        
        try:
            sixtyeight = EQuestions6.objects.get(user=request.user).TBD #to be determined #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtyeight (EQuestions6.TBD)")
        
        # EQuestions7 fields
        try:
            sixtynine = EQuestions7.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: sixtynine (EQuestions7.Start_Up)")
        
        try:
            seventy = EQuestions7.objects.get(user=request.user).Growth_Scalabitlity #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventy (EQuestions7.Growth_Scalabitlity)")
        
        try:
            seventyone = EQuestions7.objects.get(user=request.user).Marketing_and_Sales #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventyone (EQuestions7.Marketing_and_Sales)")
        
        try:
            seventytwo = EQuestions7.objects.get(user=request.user).Cash_FLow_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventytwo (EQuestions7.Cash_FLow_Capital)")
        
        try:
            seventythree = EQuestions7.objects.get(user=request.user).Human_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventythree (EQuestions7.Human_Capital)")
        
        try:
            seventyfour = EQuestions7.objects.get(user=request.user).Equipment #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventyfour (EQuestions7.Equipment)")
        
        try:
            seventyfive = EQuestions7.objects.get(user=request.user).Merger_and_Acquistions #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventyfive (EQuestions7.Merger_and_Acquistions)")
        
        try:
            seventysix = EQuestions7.objects.get(user=request.user).Inventory #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventysix (EQuestions7.Inventory)")
        
        try:
            seventyseven = EQuestions7.objects.get(user=request.user).Real_State #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventyseven (EQuestions7.Real_State)")
        
        try:
            seventyeight = EQuestions7.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventyeight (EQuestions7.Other)")
        
        try:
            seventynine = EQuestions7.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: seventynine (EQuestions7.Unsure)")
        
        # EQuestions8 fields
        try:
            eighty = EQuestions8.objects.get(user=request.user).Low_Risk_Tolerance #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eighty (EQuestions8.Low_Risk_Tolerance)")
        
        try:
            eightyone = EQuestions8.objects.get(user=request.user).Medium_Risk_Tolerance #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightyone (EQuestions8.Medium_Risk_Tolerance)")
        
        try:
            eightytwo = EQuestions8.objects.get(user=request.user).High_Risk_Tolerance #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightytwo (EQuestions8.High_Risk_Tolerance)")
        
        try:
            eightythree = EQuestions8.objects.get(user=request.user).Low_Cost_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightythree (EQuestions8.Low_Cost_Capital)")
        
        try:
            eightyfour = EQuestions8.objects.get(user=request.user).Medium_Cost_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightyfour (EQuestions8.Medium_Cost_Capital)")
        
        try:
            eightyfive = EQuestions8.objects.get(user=request.user).High_Cost_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightyfive (EQuestions8.High_Cost_Capital)")
        
        try:
            eightysix = EQuestions8.objects.get(user=request.user).Very_High_Cost_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightysix (EQuestions8.Very_High_Cost_Capital)")
        
        try:
            eightyseven = EQuestions8.objects.get(user=request.user).Immaterial_Cost_Capital #int 0 if not selected 1 if selected
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightyseven (EQuestions8.Immaterial_Cost_Capital)")
        
        # EQuestions fields
        try:
            eightyeight = EQuestions.objects.get(user=request.user).RC_zero_to_499
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightyeight (EQuestions.RC_zero_to_499)")
        
        try:
            eightynine = EQuestions.objects.get(user=request.user).RC_500_to_999
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: eightynine (EQuestions.RC_500_to_999)")
        
        try:
            ninety = EQuestions.objects.get(user=request.user).RC_1000_to_2499
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninety (EQuestions.RC_1000_to_2499)")
        
        try:
            ninetyone = EQuestions.objects.get(user=request.user).RC_2500_to_4999
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetyone (EQuestions.RC_2500_to_4999)")
        
        try:
            ninetytwo = EQuestions.objects.get(user=request.user).RC_5000_to_9999
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetytwo (EQuestions.RC_5000_to_9999)")
        
        try:
            ninetythree = EQuestions.objects.get(user=request.user).RC_10000_to_24999
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetythree (EQuestions.RC_10000_to_24999)")
        
        try:
            ninetyfour = EQuestions.objects.get(user=request.user).RC_25000_to_49999
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetyfour (EQuestions.RC_25000_to_49999)")
        
        try:
            ninetyfive = EQuestions.objects.get(user=request.user).RC_More_Than_50000
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetyfive (EQuestions.RC_More_Than_50000)")
        
        try:
            ninetysix = EQuestions.objects.get(user=request.user).RT_1D_to_1W
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetysix (EQuestions.RT_1D_to_1W)")
        
        try:
            ninetyseven = EQuestions.objects.get(user=request.user).RT_1W_to_2W
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetyseven (EQuestions.RT_1W_to_2W)")
        
        try:
            ninetyeight = EQuestions.objects.get(user=request.user).RT_2W_to_4W
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetyeight (EQuestions.RT_2W_to_4W)")
        
        try:
            ninetynine = EQuestions.objects.get(user=request.user).RT_1M_to_2M
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: ninetynine (EQuestions.RT_1M_to_2M)")
        
        try:
            hundred = EQuestions.objects.get(user=request.user).RT_2M_to_3M
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundred (EQuestions.RT_2M_to_3M)")
        
        try:
            hundredone = EQuestions.objects.get(user=request.user).RT_3M_to_6M
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredone (EQuestions.RT_3M_to_6M)")
        
        try:
            hundredtwo = EQuestions.objects.get(user=request.user).RT_6M_to_12M
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredtwo (EQuestions.RT_6M_to_12M)")
        
        try:
            hundredthree = EQuestions.objects.get(user=request.user).RT_More_Than_a_Year
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredthree (EQuestions.RT_More_Than_a_Year)")
        
        # DocumentsPrepared fields
        try:
            hundredfour = DocumentsPrepared.objects.get(user=request.user).summary_of_offering
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredfour (DocumentsPrepared.summary_of_offering)")
        
        try:
            hundredfive = DocumentsPrepared.objects.get(user=request.user).financial_forecast
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredfive (DocumentsPrepared.financial_forecast)")
        
        try:
            hundredsix = DocumentsPrepared.objects.get(user=request.user).lean_business_model
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredsix (DocumentsPrepared.lean_business_model)")
        
        try:
            hundredseven = DocumentsPrepared.objects.get(user=request.user).presentation_deck
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredseven (DocumentsPrepared.presentation_deck)")
        
        try:
            hundredeight = DocumentsPrepared.objects.get(user=request.user).leadership_overview
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredeight (DocumentsPrepared.leadership_overview)")
        
        try:
            hundrednine = DocumentsPrepared.objects.get(user=request.user).exit_strategy
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundrednine (DocumentsPrepared.exit_strategy)")
        
        try:
            hundredten = DocumentsPrepared.objects.get(user=request.user).offering_documents
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredten (DocumentsPrepared.offering_documents)")
        
        try:
            hundredeleven = DocumentsPrepared.objects.get(user=request.user).ai_generated_deep_dive
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredeleven (DocumentsPrepared.ai_generated_deep_dive)")
        
        try:
            hundredtwelve = DocumentsPrepared.objects.get(user=request.user).virtual_data_room
        except:
            return HttpResponse("Please Go through the survey and complete all questions! Failed to retrieve: hundredtwelve (DocumentsPrepared.virtual_data_room)")
        # Collateral status
        # Collateral status
        if collateral_status_check == "Not Applicable":
            hundredthirteen = 1  # not applicable
            hundredfourteen = 0
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "Yes":
            hundredthirteen = 0
            hundredfourteen = 1  # Yes
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "No":
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 1   # No
            hundredsixteen = 0
        else:
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 0            
            hundredsixteen = 1   # Other

        # Credit score
        if credit_score_check == "<580":
            hundredseventeen = 1 #<580
            hundredeighteen = 0
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">620":
            hundredseventeen = 0
            hundredeighteen = 1 #<620
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">680":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 1 #>680
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">720":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 1 #>720
            hundredtwentyone = 0 
        else:
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 0            
            hundredtwentyone = 1 #>760

        # Criminal history
        if criminal_history_check == "None":
            hundredtwentytwo = 1
            hundredtwentythree = 0
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0
        elif criminal_history_check == "Misdemeanor":
            hundredtwentytwo = 0
            hundredtwentythree = 1 #Misdemeanor
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Felony":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 1 #Felony
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Fraud":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 1 #Fraud
            hundredtwentysix = 0                
        else:
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 1 #Securities Violation   
    except:
        return HttpResponse("Please Go through the survey and complete all questions!")
    # Get all local variables after they have been assigned
    all_variables = locals()
    image_path = BASE_DIR / "finfire_web" / "static" / "img" / "b.png"
    # Create a list to store the variable values
    values_list = [value for key, value in all_variables.items() if key != 'request'][13:]
    counter = sum(1 for item in values_list if item==1)-2 - sum(1 for item in values_list[103:112] if item == 1)
    all_name_capital = capitalTypes.objects.values_list('name', flat=True)

    dict_name_percentage = {}

    for capital in all_name_capital:
        # Retrieve `matrix_weights` and `counter` safely
        matrix_weight = np.array(CapitalType.objects.get(namec__name=capital).matrix_weights, dtype=np.float64)
        counter_value = CapitalType.objects.get(namec__name=capital).counter

        # Calculate the percentage
        dict_name_percentage[capital] = ((sum(np.array(values_list) * matrix_weight)) * 10) / counter #counter_value

    def sanitize_value(value):
        if isinstance(value, (np.floating, np.integer)):
            value = float(value)
        if isinstance(value, float):
            if math.isnan(value):
                return None  # Convert NaN to None
            if math.isinf(value):  # Handle infinity cases
                return None
        return value

    dict_name_percentage_sanitized = {k: sanitize_value(v) for k, v in dict_name_percentage.items()}

    # Convert None values to a number that makes sense in your context (e.g., 0 or -1)
    # Alternatively, remove keys with None values if appropriate
    cleaned_percentage = {
        k: v if v is not None else 0  # Replace None with 0 or another appropriate value
        for k, v in dict_name_percentage_sanitized.items()
    }

    # Now sort the dictionary
    keys = list(cleaned_percentage.keys())
    values = list(cleaned_percentage.values())
    sorted_value_index = np.argsort(values)
    sorted_percentage = {keys[i]: values[i] for i in sorted_value_index}

    # Ensure all values are JSON-serializable
    final_percentage = {
        k: float(v) if isinstance(v, (np.floating, np.integer)) else v
        for k, v in sorted_percentage.items()
    }
    final_percentage = capitalCheck(values_list,final_percentage)   
    
    # Try to get existing record for the user
    # Instead of creating a new record, get_or_create or update existing
    all_match_percentage, created = allCapitalMatchValues.objects.get_or_create(
        user=request.user,
        defaults={'percentage': final_percentage}
    )
    if not created:
        # Update existing record
        allCapitalMatchValues.objects.filter(user=request.user).update(percentage=final_percentage)
    
    try:
        status = Letter_Response.objects.get(user=request.user).top_6_name_output[-1]
    except:
        status = False

    if status == True:
        top_6_name = Letter_Response.objects.get(user=request.user).top_6_name_output
    else:
        sorted_percentage = capitalCheck(values_list,sorted_percentage)
        top_6_name = [item[0] for item in sorted(sorted_percentage.items(), key=lambda item: item[1], reverse=True)[:5]]
    dfcm = pd.DataFrame() # store the data details from database capital market

    cm1name = top_6_name[0] 
    cm2name = top_6_name[1]
    cm3name =  top_6_name[2]
    cm4name = top_6_name[3]
    cm5name = top_6_name[4]
    #cm6name = top_6_name[5]
    
    # Create capital type record for the user
    create_capital_type_for_user(request.user, cm1name)

    try:
        id_checker_cm = Matches_Purchased.objects.get(user=request.user)
        cm_id_value = id_checker_cm.match_id_cm
        cm_id_value = [0 if type(a) != int else int(a) for a in cm_id_value]

    except Matches_Purchased.DoesNotExist:
        # Handle the case where no matching record exists
        cm_id_value = [0]


    try:
        cm1num = VQuestion1.objects.filter(CM_Type = cm1name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm1data = list(VQuestion1.objects.filter(CM_Type=cm1name).exclude(id__in=cm_id_value).values())
    except:
        cm1num = 0
    try:
        cm2num = VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm2data = list(VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).values())
    except:
        cm2num = 0
    try:
        cm3num = VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm3data = list(VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in= cm_id_value).values())
    except:
        cm3num = 0
    try:    
        cm4num = VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm4data = list(VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).values())
    except:
        cm4num = 0
    try:    
        cm5num =VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm5data = list(VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).values())
    except:
        cm5num = 0

    cm_type_count = 1 
    total_matches = cm1num +cm2num#+cm3num+cm4num+cm5num#+cm6num # should be replaced after database    
    price = 25 # need to discuss on this
    totalprice = price * total_matches

    if total_matches >= 100:
        discount = 0.2 * totalprice

    elif total_matches >=200:
        discount = 0.4*totalprice

    else:
        discount = 0    
    balancedue = totalprice - discount

    #For POST data for user purchase of matches:
    try:
        report = Matches_Purchased.objects.get(user=request.user)

    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=request.user)

    #intermediaries = len(all_i_data_f)

    #For Backend API request of purchases done
    try:
        optionsapi = Purchases.objects.get(user=request.user)

    except Purchases.DoesNotExist:
        optionsapi = Purchases(user=request.user) 

    optionapi1 = optionsapi.cm1purchase
    optionapi2 = optionsapi.cm2purchase
    optionapi3 = optionsapi.cm3purchase
    optionapi4 = optionsapi.cm4purchase
    optionapi5 = optionsapi.cm5purchase
    optionapi6 = optionsapi.cm6purchase
    ipurchase = optionsapi.ipurchase

    try:
        cm1dataapi = random.sample(cm1data,optionapi1)
    except:
        cm1dataapi = cm1dataapi[:optionapi1]  
            
    all_data_api = cm1dataapi #+cm2dataapi+cm3dataapi+cm4dataapi+cm5dataapi+cm6dataapi
    id_CM_api =   cm_id_value+[int(a['id']) for a in all_data_api]
    report.match_id_cm = id_CM_api
    dfcm = pd.DataFrame(all_data_api)



    #print(dfcm.head())
    # Convert the DataFrame to JSON
    json_data_api = dfcm.to_json(orient='split')
    optionsapi.cm_matches = json_data_api
    optionsapi.save()


    if request.method == 'POST':
        # Get input values from the POST data
        option1 = int(request.POST.get( cm1name, 0))
        option2 = int(request.POST.get( cm2name , 0))
        option3 = int(request.POST.get(cm3name , 0))
        option4 = int(request.POST.get( cm4name, 0))
        option5 = int(request.POST.get( cm5name, 0))
        option7 = int(request.POST.get( 'option7', 0))


        try:
            cm1data = random.sample(cm1data,option1)
        except:
            cm1data = cm1data[:option1]  
        try:          
            cm2data = random.sample(cm2data,option2)
        except:
            cm2data = cm2data[:option2]
        try:              
            cm3data = random.sample(cm3data,option3)
        except:
            cm3data= cm3data[:option3]
        try:
            cm4data = random.sample(cm4data,option4)
        except:
            cm4data= cm4data[:option4] 
        try:           
            cm5data = random.sample(cm5data,option5)
        except:
            cm5data= cm5data[:option5]
            
        all_data = cm1data +cm2data+cm3data+cm4data+cm5data#+cm6data
        id_CM =   cm_id_value+[int(a['id']) for a in all_data]
        report.match_id_cm = id_CM  
        dfcm = pd.DataFrame(all_data)


        #print(dfcm.head())
        # Convert the DataFrame to JSON
        json_data = dfcm.to_json(orient='records')

        #Conveert the DataFrame to CSV
        csv_data = dfcm.to_csv(index=False)

        # To HTML table
        html_table = dfcm.to_html()

        purchase_dict = {cm1name:option1,cm2name:option2,cm3name:option3,cm4name:option4,cm5name:option5,'intermediaries':option7}#cm6name:option6}

        # Calculate total_num, total_price, discount, and balance_due
        total_num = option1 #+ option2 + option3 + option4 + option5 + option6 + option7
        price = 25 # Example price, this could be dynamic
        total_price = total_num * price

        # Calculate discount
        if total_num > 200:
            discount = 0.4 * total_price
        elif total_num > 100:
            discount = 0.2 * total_price
        else:
            discount = 0

        balance_due = total_price - discount

        # Save the data to the model
        report.purchased_matches = json.dumps(purchase_dict)
        report.total_num = total_num
        report.total_price = total_price
        report.discount = discount
        report.balance_due = balance_due
        report.price = price
        # Save the model instance
        report.save()    

        return render(request,'finfo.html',{'table':html_table,'list_name':top_6_name})#,'table_i':html_table_2})


        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        return response

    output_list = top_6_name

    # In the dictionary pdf_documents for the final pdf download to properly work, definition should come first,faq second and tewelve variable report third. This order determines the order in the letter.
    # In the dictionary pdf_documents for the final pdf download to properly work, definition should come first,faq second and tewelve variable report third. This order determines the order in the letter.
    pdf_documents = {
        'Accelerator' : [accelerator.accelerator(request),accelerator.acceleratorfaq(request),accelerator.acceleratortwelve(request)],
        'Bonds' : [bonds.bonds(request),bonds.bondsfaq(request),bonds.bondstwelve(request)],
        'Bootstrapped' : [bootstrapped.bootstrapped(request),bootstrapped.bootstrappedfaq(request),bootstrapped.bootstrappedtwelve(request)],
        'Commercial Banking' : [commercialbanking.commercialbanking(request),commercialbanking.commercialbankingfaq(request),commercialbanking.commercialbankingtwelve(request)],
        'Cryptocurrency' : [cryptocurrency.cryptocurrency(request),cryptocurrency.cryptocurrencyfaq(request),cryptocurrency.cryptocurrencytwelve(request)],
        'Factoring' : [factoring.factoring(request),factoring.factoringfaq(request),factoring.factoringtwelve(request)],
        'Grants' : [grants.grants(request),grants.grantsfaq(request),grants.grantstwelve(request)],
        'Hedge Funds' : [hedgefunds.hedgefunds(request),hedgefunds.hedgefundsfaq(request),hedgefunds.hedgefundstwelve(request)],
        'Incubator' : [incubator.incubator(request),incubator.incubatorfaq(request),incubator.incubatortwelve(request)],
        'Investment Banking' : [investmentbanking.investmentbanking(request),investmentbanking.investmentbankingfaq(request),investmentbanking.investmentbankingtwelve(request)],
        'Private Debt' : [privatedebt.privatedebt(request),privatedebt.privatedebtfaq(request),privatedebt.privatedebttwelve(request)],
        'Private Equity Securities' : [privateequitysecurities.privateequitysecurities(request),privateequitysecurities.privateequitysecuritiesfaq(request),privateequitysecurities.privateequitysecuritiestwelve(request)],
        'Royalty Financing' : [royaltyfinancing.royaltyfinancing(request),royaltyfinancing.royaltyfinancingfaq(request),royaltyfinancing.royaltyfinancingtwelve(request)],
        'Small Business Administration (SBA)' : [SmallBusinessAdministration.SmallBusinessAdministration(request),SmallBusinessAdministration.SmallBusinessAdministrationfaq(request),SmallBusinessAdministration.SmallBusinessAdministrationtwelve(request)],
        'Third Party Corporate Credit' : [thirdpartycorporatecredit79.thirdpartycorporatecredit(request),thirdpartycorporatecredit79.thirdpartycorporatecreditfaq(request),thirdpartycorporatecredit79.thirdpartycorporatecredittwelve(request)],
        'Tokenization' : [tokenization80.tokenization(request),tokenization80.tokenizationfaq(request),tokenization80.tokenizationtwelve(request)],
        'Venture Capital' : [venturecapital.venturecapital(request),venturecapital.venturecapitalfaq(request),venturecapital.venturecapitaltwelve(request)],
        }
    
    # Definition,faq and twelvev variables would http content and decode it to utf-8 from the http response object for top capital market match which would be used to generate pdf. 
    definition = "Temporary sollution"#mark_safe(pdf_documents[cm1name][0].content.decode('utf-8'))
    faq_que = "Temporary sollution"#mark_safe(pdf_documents[cm1name][1].content.decode('utf-8'))
    twelvev = "Temporary sollution"#mark_safe(pdf_documents[cm1name][2].content.decode('utf-8'))

    cost_dict = {
        'Accelerator': '$2,500 to $25,000',
        'Bonds' : '$50,000 to $250,000',
        'Bootstrapped' : '0 to $5,000',
        'Commercial Banking': '0 to $5,000',
        'Cryptocurrency' : '$1,000 to 25,000',
        'Factoring' : '0 to $5,000',
        'Grants' : '$250 to $10,000',
        'Hedge Funds' : '$10,000 to $25,000',
        'Incubator' : '0 to $25,000',
        'Investment Banking' : '$20,000 to $75,000',
        'Private Debt' : '0 to $5,000',
        'Royalty Financing': '$2,500 to $10,000',
        'Third Party Corporate Credit': '$10,000 to $25,000',     
        'Private Equity Securities' : '$25,000 to $150,000',
        'Venture Capital' : '$25,000 $150,000',
        'Tokenization' : '$1,000 to $15,000',
        'Small Business Administration (SBA)' : '$500 to $2,500',
    }
    try:
        context = {
            'date':date,
            'firstname':firstname,
            'lastname':lastname,
            'address':primary_business_adress,
            'phone' :business_phone,
            'secondphone':UserDetail.objects.get(user=request.user).Mobile_Phone,
            'email': primary_email,
            'businessname' : company_name,
            'count': cm_type_count,
            'fundgoal': fundgoal, 
            'totalnum': total_matches,
            'cm1name': cm1name,
            'cm1nameoutput':output_list[0],
            'cm2name': cm2name,
            'cm2nameoutput':output_list[1],
            'cm3name': cm3name,
            'cm3nameoutput':output_list[2],
            'cm4name': cm4name,
            'cm5name': cm5name,
            'cm1no':cm1num,
            'cm2no':cm2num,
            'cm3no':cm3num,
            'cm4no':cm4num,
            'cm5no':cm5num,
            'price':price,
            'totalprice':totalprice,
            'discount':discount,
            'balancedue':balancedue,
            'report':report,
            'list_name':top_6_name,
            'info':info,
            'tony_signature_url': request.build_absolute_uri(static('img/none.png')),
            'logo_url': request.build_absolute_uri(static('img/b.png')),
            'definition' : definition,
            'faq_que' : faq_que,
            'twelvev' : twelvev,
            #'cost' : cost_dict[cm1name],
        }
    except:
        return HttpResponse("Options Mismatch need debugging in backend")

    #Saving individual variable for output to share in api endpoint
    try:
        output = Letter_Response.objects.get(user=request.user)

    except Letter_Response.DoesNotExist:
        output = Letter_Response(user=request.user)

    output.firstname = firstname
    output.lastname = lastname
    output.address = primary_business_adress
    output.phone = business_phone
    output.email = primary_email
    output.businessname = company_name
    output.count = cm_type_count
    output.fundgoal = fundgoal
    output.totalnum = total_matches
    output.cm1name = cm1name
    output.cm2name = cm2name
    output.cm3name = cm3name
    output.cm4name = cm4name
    output.cm5name = cm5name
    #output.cm6name = cm6name
    output.cm1no = cm1num
    output.cm2no = cm2num
    output.cm3no = cm3num
    output.cm4no = cm4num
    output.cm5no = cm5num
    #output.cm6no = cm6num
    #output.intermediaries = intermediaries
    output.price = price
    output.totalprice = totalprice
    output.discount = discount
    output.balancedue = balancedue
    output.top_6_name = top_6_name
    output.top_6_name_output = output_list
    output.save()
    
    rendered_htmlclassic = render_to_string('letter.html',context)
    try:
        # Try to retrieve the existing Match_Data for the user
        html_data = Match_Data.objects.get(user=request.user)
        # Update the html content if the object already exists
        html_data.html = rendered_htmlclassic
        html_data.save()

    except Match_Data.DoesNotExist:
        # If no Match_Data exists for the user, create a new one
        html_data = Match_Data(user=request.user, html=rendered_htmlclassic)
        html_data.save()    


    
    rendered_html = render_to_string('letterpdf.html',context)
    
    # Add CSS for header, footer and page numbers
    css_style = '''
         <style>
                body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .logo {
            display: inline-block; /* Display as inline to avoid block-level spacing */
            margin: 0;
            padding: 0;
            line-height: 0; /* Reduces extra vertical space */
        }
        .logo img {
            display: inline; /* Ensure image is treated as inline content */
            vertical-align: middle; /* Align the image vertically in line with text */
        }
        .spacing {
            margin-top: 20px;
        }
        .content {
            text-align: left;
            margin-top: 20px;
            line-height: 1.5;
            font-family: "Times New Roman", Times, serif;
            font-size: 11px;   
        }
        .capital-source, .pricing {
            display: flex;
            justify-content: space-between;
        }
        .pricing-summary {
            margin-top: 20px;
            text-align: right;
        }
        .signature {
            margin-top: 40px;
            text-align: left;
        }
        .button {
            margin-top: 20px;
            text-align: right;    
        }
        .page {
            margin: 0 auto; 
            padding: 20px; 
            max-width: 80%; border: 1px solid #ccc; 
            border-radius: 10px; 
            background-color: #f9f9f9;
        }

        .page-break {
            page-break-after: always;
        }
            @page {
                size: letter;
                margin: 1in;
                @top-center {
                    content: "FINFIRE REPORT";
                    font-size: 11px;
                    font-weight: bold;
                }
                @bottom-center {
                    content: "4760 S. Pecos Road, Suite 100-28, Las Vegas, NV 89121";
                    font-size: 11px;
                }
                @bottom-right {
                    content: counter(page);
                    font-size: 11px;
                }
            }
        </style>
    '''
    if company_name.strip().lower() == "none":
        company_report = 'FINFIRE REPORT'
    else:
        company_report = company_name + 'FINFIRE REPORT'      
    css_style = css_style.replace('FINFIRE REPORT',company_report.upper())

    # Insert the CSS into the HTML
    rendered_html = rendered_html.replace('</style>', f'{css_style}</style>')    
    
    html = HTML(string=rendered_html, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    # Create a unique filename for the PDF
    import uuid
    unique_filename = f"FINFIRE_Letter_{uuid.uuid4().hex}.pdf"
    
    # Create the media directory if it doesn't exist
    import os
    from django.conf import settings
    media_dir = os.path.join(settings.MEDIA_ROOT, 'temp_pdfs')
    os.makedirs(media_dir, exist_ok=True)
    
    # Save the PDF to the media directory
    pdf_path = os.path.join(media_dir, unique_filename)
    with open(pdf_path, 'wb') as f:
        f.write(pdf)
    
    # Serve the file and delete it after serving
    from django.http import FileResponse
    import threading
    
    def serve_and_delete(request, file_path):
        # Option 1: Serve file directly (current approach)
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="FINFIRE_Letter.pdf"'
        
        # Option 2: Return file URL for frontend to handle
        #from django.http import JsonResponse
        #file_url = f"{request.build_absolute_uri('/')[:-1]}{settings.MEDIA_URL}temp_pdfs/{unique_filename}"
        #response = JsonResponse({'pdf_url': file_url, 'filename': 'FINFIRE_Letter.pdf'})
        
        # Schedule file deletion after response is sent
        def delete_file():
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        
        #Start deletion in a separate thread after a short delay
        timer = threading.Timer(30.0, delete_file)
        timer.start()
        
        return response
    return serve_and_delete(request, pdf_path)


#####################################################WORD#################################
@login_required
def word(request):
    #time.sleep(5)
    try:
        collateral_status_check =LendingRequirements.objects.get(user=request.user).collateral_status
        credit_score_check = LendingRequirements.objects.get(user=request.user).credit_score 
        criminal_history_check = LendingRequirements.objects.get(user=request.user).criminal_history                
        firstname = UserDetail.objects.get(user=request.user).First_Name #string
        lastname = UserDetail.objects.get(user=request.user).Last_Name #string
        date = datetime.now().strftime('%B %d, %Y') #no need
        primary_business_adress = UserDetail.objects.get(user=request.user).Business_Adress #string
        business_phone = UserDetail.objects.get(user=request.user).Business_Phone #string
        fundgoal = EQuestions5.objects.get(user=request.user).Selected_Option[:] # string based on question of how much capital user want to raise
        mobile_phone = UserDetail.objects.get(user=request.user).Mobile_Phone #string
        primary_email = UserDetail.objects.get(user=request.user).User_Email #string
        company_website = UserDetail.objects.get(user=request.user).Company_Website #string
        company_name = EQuestions2.objects.get(user=request.user).Business_Name #string
        one = EQuestions1.objects.get(user=request.user).Idea #int 0 if not selected 1 if selected
        two = EQuestions1.objects.get(user=request.user).Formation #int 0 if not selected 1 if selected
        three = EQuestions1.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        four = EQuestions1.objects.get(user=request.user).Growth #int 0 if not selected 1 if selected
        five = EQuestions1.objects.get(user=request.user).M_And_A #int 0 if not selected 1 if selected
        six = EQuestions1.objects.get(user=request.user).Preparing_For_Public #int 0 if not selected 1 if selected
        seven = EQuestions1.objects.get(user=request.user).Distressed #int 0 if not selected 1 if selected
        eight = EQuestions2.objects.get(user=request.user).No_Business #int 0 if not selected 1 if selected
        nine = EQuestions2.objects.get(user=request.user).Sole_Proprietorship #int 0 if not selected 1 if selected
        ten = EQuestions2.objects.get(user=request.user).LLC #int 0 if not selected 1 if selected
        eleven = EQuestions2.objects.get(user=request.user).LP #int 0 if not selected 1 if selected
        twelve = EQuestions2.objects.get(user=request.user).GP #int 0 if not selected 1 if selected
        thirteen = EQuestions2.objects.get(user=request.user).S_Corporation #int 0 if not selected 1 if selected
        fourteen = EQuestions2.objects.get(user=request.user).C_Corp #int 0 if not selected 1 if selected
        fifteen = EQuestions2.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        sixteen = EQuestions3.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        seventeen = EQuestions3.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        eighteen = EQuestions3.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        nineteen = EQuestions3.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        twenty = EQuestions3.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        twentyone = EQuestions3.objects.get(user=request.user).More_1M_Less_2M #int 0 if not selected 1 if selected
        twentytwo = EQuestions3.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        twentythree = EQuestions3.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        twentyfour = EQuestions3.objects.get(user=request.user).More_10M #int 0 if not selected 1 if selected
        twentyfive = EQuestions4.objects.get(user=request.user).Accelerator #int 0 if not selected 1 if selected
        twentysix = EQuestions4.objects.get(user=request.user).Bonds #int 0 if not selected 1 if selected
        twentyseven = EQuestions4.objects.get(user=request.user).Comercial_Banking #int 0 if not selected 1 if selected
        twentyeight = EQuestions4.objects.get(user=request.user).Cryptocurrency #int 0 if not selected 1 if selected
        twentynine = EQuestions4.objects.get(user=request.user).EB5_Immigration #int 0 if not selected 1 if selected
        thirty = EQuestions4.objects.get(user=request.user).Enterprise_Zones #int 0 if not selected 1 if selected
        thirtyone = EQuestions4.objects.get(user=request.user).Factoring #int 0 if not selected 1 if selected
        thirtytwo = EQuestions4.objects.get(user=request.user).Grants #int 0 if not selected 1 if selected
        thirtythree = EQuestions4.objects.get(user=request.user).Hedge_Funds #int 0 if not selected 1 if selected 
        thirtyfour = EQuestions4.objects.get(user=request.user).Incubator #int 0 if not selected 1 if selected
        thirtyfive = EQuestions4.objects.get(user=request.user).Investment_Banking #int 0 if not selected 1 if selected
        thirtysix = EQuestions4.objects.get(user=request.user).Other_Owner_Equity #int 0 if not selected 1 if selected
        thirtyseven = EQuestions4.objects.get(user=request.user).Private_Debt #int 0 if not selected 1 if selected
        thirtyeight = EQuestions4.objects.get(user=request.user).Private_Equity #int 0 if not selected 1 if selected
        thirtynine = EQuestions4.objects.get(user=request.user).Public_Offereing #int 0 if not selected 1 if selected
        fourty = EQuestions4.objects.get(user=request.user).Real_Estate #int 0 if not selected 1 if selected
        fourtyone = EQuestions4.objects.get(user=request.user).Royalty_Financing #int 0 if not selected 1 if selected
        fourtytwo = EQuestions4.objects.get(user=request.user).Small_Business_Administration #int 0 if not selected 1 if selected
        fourtythree = EQuestions4.objects.get(user=request.user).Venture_Capital #int 0 if not selected 1 if selected
        fourtyfour = EQuestions4.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        fourtyfive = EQuestions5.objects.get(user=request.user).Less_25k #int 0 if not selected 1 if selected
        fourtysix = EQuestions5.objects.get(user=request.user).More_25K_Less_100k #int 0 if not selected 1 if selected
        fourtyseven = EQuestions5.objects.get(user=request.user).More_100k_Less_250K #int 0 if not selected 1 if selected
        fourtyeight = EQuestions5.objects.get(user=request.user).More_250k_Less_500K #int 0 if not selected 1 if selected
        fourtynine = EQuestions5.objects.get(user=request.user).More_500K_Less_1M #int 0 if not selected 1 if selected
        fifty = EQuestions5.objects.get(user=request.user).More_1M_Less_1_35M #int 0 if not selected 1 if selected
        fiftyone = EQuestions5.objects.get(user=request.user).More_1_35M_Less_2M #int 0 if not selected 1 if selected
        fiftytwo = EQuestions5.objects.get(user=request.user).More_2M_Less_5M #int 0 if not selected 1 if selected
        fiftythree = EQuestions5.objects.get(user=request.user).More_5M_Less_10M #int 0 if not selected 1 if selected
        fiftyfour = EQuestions5.objects.get(user=request.user).More_10M_Less_20M #int 0 if not selected 1 if selected
        fiftyfive = EQuestions5.objects.get(user=request.user).More_20M #int 0 if not selected 1 if selected
        fiftysix = EQuestions5.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        fiftyseven = EQuestions6.objects.get(user=request.user).Founders_Round #int 0 if not selected 1 if selected
        fiftyeight = EQuestions6.objects.get(user=request.user).Pre_Seed #int 0 if not selected 1 if selected
        fiftynine = EQuestions6.objects.get(user=request.user).Seed #int 0 if not selected 1 if selected
        sixty = EQuestions6.objects.get(user=request.user).Series_A #int 0 if not selected 1 if selected
        sixtyone = EQuestions6.objects.get(user=request.user).Series_B #int 0 if not selected 1 if selected
        sixtytwo = EQuestions6.objects.get(user=request.user).Series_C #int 0 if not selected 1 if selected
        sixtythree = EQuestions6.objects.get(user=request.user).Pre_Ipo #int 0 if not selected 1 if selected
        sixtyfour = EQuestions6.objects.get(user=request.user).Ipo #int 0 if not selected 1 if selected 
        sixtyfive = EQuestions6.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        sixtysix = EQuestions6.objects.get(user=request.user).One #int 0 if not selected 1 if selected
        sixtyseven = EQuestions6.objects.get(user=request.user).Two #int 0 if not selected 1 if selected
        sixtyeight = EQuestions6.objects.get(user=request.user).TBD #to be determined #int 0 if not selected 1 if selected
        sixtynine = EQuestions7.objects.get(user=request.user).Start_Up #int 0 if not selected 1 if selected
        seventy = EQuestions7.objects.get(user=request.user).Growth_Scalabitlity #int 0 if not selected 1 if selected
        seventyone = EQuestions7.objects.get(user=request.user).Marketing_and_Sales #int 0 if not selected 1 if selected 
        seventytwo = EQuestions7.objects.get(user=request.user).Cash_FLow_Capital #int 0 if not selected 1 if selected
        seventythree = EQuestions7.objects.get(user=request.user).Human_Capital #int 0 if not selected 1 if selected
        seventyfour = EQuestions7.objects.get(user=request.user).Equipment #int 0 if not selected 1 if selected
        seventyfive = EQuestions7.objects.get(user=request.user).Merger_and_Acquistions #int 0 if not selected 1 if selected
        seventysix = EQuestions7.objects.get(user=request.user).Inventory #int 0 if not selected 1 if selected 
        seventyseven = EQuestions7.objects.get(user=request.user).Real_State #int 0 if not selected 1 if selected
        seventyeight = EQuestions7.objects.get(user=request.user).Other #int 0 if not selected 1 if selected
        seventynine = EQuestions7.objects.get(user=request.user).Unsure #int 0 if not selected 1 if selected
        eighty = EQuestions8.objects.get(user=request.user).Low_Risk_Tolerance #int 0 if not selected 1 if selected
        eightyone = EQuestions8.objects.get(user=request.user).Medium_Risk_Tolerance #int 0 if not selected 1 if selected
        eightytwo = EQuestions8.objects.get(user=request.user).High_Risk_Tolerance #int 0 if not selected 1 if selected
        eightythree = EQuestions8.objects.get(user=request.user).Low_Cost_Capital #int 0 if not selected 1 if selected
        eightyfour = EQuestions8.objects.get(user=request.user).Medium_Cost_Capital #int 0 if not selected 1 if selected
        eightyfive = EQuestions8.objects.get(user=request.user).High_Cost_Capital #int 0 if not selected 1 if selected
        eightysix = EQuestions8.objects.get(user=request.user).Very_High_Cost_Capital #int 0 if not selected 1 if selected
        eightyseven = EQuestions8.objects.get(user=request.user).Immaterial_Cost_Capital #int 0 if not selected 1 if selected
        eightyeight = EQuestions.objects.get(user=request.user).RC_zero_to_499
        eightynine = EQuestions.objects.get(user=request.user).RC_500_to_999
        ninety = EQuestions.objects.get(user=request.user).RC_1000_to_2499
        ninetyone = EQuestions.objects.get(user=request.user).RC_2500_to_4999
        ninetytwo = EQuestions.objects.get(user=request.user).RC_5000_to_9999
        ninetythree = EQuestions.objects.get(user=request.user).RC_10000_to_24999
        ninetyfour = EQuestions.objects.get(user=request.user).RC_25000_to_49999
        ninetyfive = EQuestions.objects.get(user=request.user).RC_More_Than_50000
        ninetysix = EQuestions.objects.get(user=request.user).RT_1D_to_1W
        ninetyseven = EQuestions.objects.get(user=request.user).RT_1W_to_2W
        ninetyeight = EQuestions.objects.get(user=request.user).RT_2W_to_4W
        ninetynine = EQuestions.objects.get(user=request.user).RT_1M_to_2M
        hundred = EQuestions.objects.get(user=request.user).RT_2M_to_3M
        hundredone = EQuestions.objects.get(user=request.user).RT_3M_to_6M
        hundredtwo = EQuestions.objects.get(user=request.user).RT_6M_to_12M
        hundredthree = EQuestions.objects.get(user=request.user).RT_More_Than_a_Year
        hundredfour = DocumentsPrepared.objects.get(user=request.user).summary_of_offering
        hundredfive = DocumentsPrepared.objects.get(user=request.user).financial_forecast
        hundredsix = DocumentsPrepared.objects.get(user=request.user).lean_business_model
        hundredseven = DocumentsPrepared.objects.get(user=request.user).presentation_deck
        hundredeight = DocumentsPrepared.objects.get(user=request.user).leadership_overview
        hundrednine = DocumentsPrepared.objects.get(user=request.user).exit_strategy
        hundredten = DocumentsPrepared.objects.get(user=request.user).offering_documents
        hundredeleven = DocumentsPrepared.objects.get(user=request.user).ai_generated_deep_dive
        hundredtwelve = DocumentsPrepared.objects.get(user=request.user).virtual_data_room
        # Collateral status
        # Collateral status
        if collateral_status_check == "Not Applicable":
            hundredthirteen = 1  # not applicable
            hundredfourteen = 0
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "Yes":
            hundredthirteen = 0
            hundredfourteen = 1  # Yes
            hundredfifteen = 0
            hundredsixteen = 0
        elif collateral_status_check == "No":
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 1   # No
            hundredsixteen = 0
        else:
            hundredthirteen = 0
            hundredfourteen = 0            
            hundredfifteen = 0            
            hundredsixteen = 1   # Other

        # Credit score
        if credit_score_check == "<580":
            hundredseventeen = 1 #<580
            hundredeighteen = 0
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">620":
            hundredseventeen = 0
            hundredeighteen = 1 #<620
            hundrednineteen = 0
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">680":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 1 #>680
            hundredtwenty = 0
            hundredtwentyone = 0
        elif credit_score_check == ">720":
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 1 #>720
            hundredtwentyone = 0 
        else:
            hundredseventeen = 0
            hundredeighteen = 0           
            hundrednineteen = 0            
            hundredtwenty = 0            
            hundredtwentyone = 1 #>760

        # Criminal history
        if criminal_history_check == "None":
            hundredtwentytwo = 1
            hundredtwentythree = 0
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0
        elif criminal_history_check == "Misdemeanor":
            hundredtwentytwo = 0
            hundredtwentythree = 1 #Misdemeanor
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Felony":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 1 #Felony
            hundredtwentyfive = 0
            hundredtwentysix = 0            
        elif criminal_history_check == "Fraud":
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 1 #Fraud
            hundredtwentysix = 0                
        else:
            hundredtwentytwo = 0
            hundredtwentythree = 0 
            hundredtwentyfour = 0
            hundredtwentyfive = 0
            hundredtwentysix = 1 #Securities Violation      
    except:
        return HttpResponse("Please Go through survey and complete all questions!")
    # Get all local variables after they have been assigned
    all_variables = locals()

    # Create a list to store the variable values
    values_list = [value for key, value in all_variables.items() if key != 'request'][13:]
    counter = sum(1 for item in values_list if item==1)-2 - sum(1 for item in values_list[103:112] if item == 1)
    all_name_capital = capitalTypes.objects.values_list('name', flat=True)

    dict_name_percentage = {}

    for capital in all_name_capital:
        # Retrieve `matrix_weights` and `counter` safely
        matrix_weight = np.array(CapitalType.objects.get(namec__name=capital).matrix_weights, dtype=np.float64)
        counter_value = CapitalType.objects.get(namec__name=capital).counter

        # Calculate the percentage
        dict_name_percentage[capital] = ((sum(np.array(values_list) * matrix_weight)) * 10) / counter#counter_value

    def sanitize_value(value):
        if isinstance(value, (np.floating, np.integer)):
            value = float(value)
        if isinstance(value, float):
            if math.isnan(value):
                return None  # Convert NaN to None
            if math.isinf(value):  # Handle infinity cases
                return None
        return value

    dict_name_percentage_sanitized = {k: sanitize_value(v) for k, v in dict_name_percentage.items()}

    # Convert None values to a number that makes sense in your context (e.g., 0 or -1)
    # Alternatively, remove keys with None values if appropriate
    cleaned_percentage = {
        k: v if v is not None else 0  # Replace None with 0 or another appropriate value
        for k, v in dict_name_percentage_sanitized.items()
    }

    # Now sort the dictionary
    keys = list(cleaned_percentage.keys())
    values = list(cleaned_percentage.values())
    sorted_value_index = np.argsort(values)
    sorted_percentage = {keys[i]: values[i] for i in sorted_value_index}

    # Ensure all values are JSON-serializable
    final_percentage = {
        k: float(v) if isinstance(v, (np.floating, np.integer)) else v
        for k, v in sorted_percentage.items()
    }
    final_percentage = capitalCheck(values_list,final_percentage)
    print(final_percentage)
    
    # Try to get existing record for the user
    # Instead of creating a new record, get_or_create or update existing
    all_match_percentage, created = allCapitalMatchValues.objects.get_or_create(
        user=request.user,
        defaults={'percentage': final_percentage}
    )
    if not created:
        # Update existing record
        allCapitalMatchValues.objects.filter(user=request.user).update(percentage=final_percentage)
    
    try:
        status = Letter_Response.objects.get(user=request.user).top_6_name_output[-1]
    except:
        status = False

    if status == True:
        top_6_name = Letter_Response.objects.get(user=request.user).top_6_name_output
    else:
        sorted_percentage = capitalCheck(values_list,sorted_percentage)
        top_6_name = [item[0] for item in sorted(sorted_percentage.items(), key=lambda item: item[1], reverse=True)[:5]]
    dfcm = pd.DataFrame() # store the data details from database capital market
    

    cm1name = top_6_name[0] 
    cm2name = top_6_name[1]
    cm3name =  top_6_name[2]
    cm4name = top_6_name[3]
    cm5name = top_6_name[4]
    #cm6name = top_6_name[5]
    
    # Create capital type record for the user
    #create_capital_type_for_user(request.user, cm1name)

    try:
        id_checker_cm = Matches_Purchased.objects.get(user=request.user)
        cm_id_value = id_checker_cm.match_id_cm
        cm_id_value = [0 if type(a) != int else int(a) for a in cm_id_value]

    except Matches_Purchased.DoesNotExist:
        # Handle the case where no matching record exists
        cm_id_value = [0]


    try:
        cm1num = VQuestion1.objects.filter(CM_Type = cm1name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm1data = list(VQuestion1.objects.filter(CM_Type=cm1name).exclude(id__in=cm_id_value).values())
    except:
        cm1num = 0
    try:
        cm2num = VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm2data = list(VQuestion1.objects.filter(CM_Type = cm2name ).exclude(id__in=cm_id_value).values())
    except:
        cm2num = 0
    try:
        cm3num = VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm3data = list(VQuestion1.objects.filter(CM_Type = cm3name ).exclude(id__in= cm_id_value).values())
    except:
        cm3num = 0
    try:    
        cm4num = VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm4data = list(VQuestion1.objects.filter(CM_Type = cm4name ).exclude(id__in=cm_id_value).values())
    except:
        cm4num = 0
    try:    
        cm5num =VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).count() # should be replaced after database
        cm5data = list(VQuestion1.objects.filter(CM_Type = cm5name ).exclude(id__in=cm_id_value).values())
    except:
        cm5num = 0

    cm_type_count = 1 
    total_matches = cm1num +cm2num#+cm3num+cm4num+cm5num#+cm6num # should be replaced after database    
    price = 25 # need to discuss on this
    totalprice = price * total_matches

    if total_matches >= 100:
        discount = 0.2 * totalprice

    elif total_matches >=200:
        discount = 0.4*totalprice

    else:
        discount = 0    
    balancedue = totalprice - discount

    #For POST data for user purchase of matches:
    try:
        report = Matches_Purchased.objects.get(user=request.user)

    except Matches_Purchased.DoesNotExist:
        report = Matches_Purchased(user=request.user)

    #intermediaries = len(all_i_data_f)

    #For Backend API request of purchases done
    try:
        optionsapi = Purchases.objects.get(user=request.user)

    except Purchases.DoesNotExist:
        optionsapi = Purchases(user=request.user) 

    optionapi1 = optionsapi.cm1purchase
    optionapi2 = optionsapi.cm2purchase
    optionapi3 = optionsapi.cm3purchase
    optionapi4 = optionsapi.cm4purchase
    optionapi5 = optionsapi.cm5purchase
    optionapi6 = optionsapi.cm6purchase
    ipurchase = optionsapi.ipurchase

    try:
        cm1dataapi = random.sample(cm1data,optionapi1)
    except:
        cm1dataapi = cm1dataapi[:optionapi1]  
            
    all_data_api = cm1dataapi #+cm2dataapi+cm3dataapi+cm4dataapi+cm5dataapi+cm6dataapi
    id_CM_api =   cm_id_value+[int(a['id']) for a in all_data_api]
    report.match_id_cm = id_CM_api

    dfcm = pd.DataFrame(all_data_api)
    # Convert the DataFrame to JSON
    json_data_api = dfcm.to_json(orient='split')
    optionsapi.cm_matches = json_data_api
    optionsapi.save()
    #json_data_i = dfim.to_json(orient='records')
#END FOR API DATA RETRIEVAL FROM DATABASE

    if request.method == 'POST':
        # Get input values from the POST data
        option1 = int(request.POST.get( cm1name, 0))
        option2 = int(request.POST.get( cm2name , 0))
        option3 = int(request.POST.get(cm3name , 0))
        option4 = int(request.POST.get( cm4name, 0))
        option5 = int(request.POST.get( cm5name, 0))
        #option6 = int(request.POST.get( cm6name , 0))
        option7 = int(request.POST.get( 'option7', 0))
        #print(option1,option2)

        try:
            cm1data = random.sample(cm1data,option1)
        except:
            cm1data = cm1data[:option1]  
        try:          
            cm2data = random.sample(cm2data,option2)
        except:
            cm2data = cm2data[:option2]
        try:              
            cm3data = random.sample(cm3data,option3)
        except:
            cm3data= cm3data[:option3]
        try:
            cm4data = random.sample(cm4data,option4)
        except:
            cm4data= cm4data[:option4] 
        try:           
            cm5data = random.sample(cm5data,option5)
        except:
            cm5data= cm5data[:option5]
        #try:        
        #    cm6data = random.sample(cm6data,option6)
        #except:
        #    cm6data = cm6data[:option6]
            
        all_data = cm1data +cm2data+cm3data+cm4data+cm5data#+cm6data
        id_CM =   cm_id_value+[int(a['id']) for a in all_data]
        report.match_id_cm = id_CM
        #try:
        #    all_i_data_f = all_i_data_f.sample(n=option7)
        #except:
        #    all_i_data_f = all_i_data_f.sample(n=0)
        #id_i =  i_id_value + [0 if a is None else int(a['id']) for index, a in all_i_data_f.iterrows()] #[int(a['id']) for a in all_i_data]
        #report.match_id_i = id_i

        #dfim = all_i_data_f
        #dfim = dfim.drop_duplicates()
        #try:
        #    dfim = dfim.sample(n=option7)
        #except:
        #    dfim = dfim.sample(n=0)    
        dfcm = pd.DataFrame(all_data)
        #print(dfim.head())


        #print(dfcm.head())
        # Convert the DataFrame to JSON
        json_data = dfcm.to_json(orient='records')
        #json_data_i = dfim.to_json(orient='records')

        #Conveert the DataFrame to CSV
        csv_data = dfcm.to_csv(index=False)
        #csv_data_i = dfim.to_csv(index=False)

        # To HTML table
        html_table = dfcm.to_html()
        #html_table_2 = dfim.to_html()

        purchase_dict = {cm1name:option1,cm2name:option2,cm3name:option3,cm4name:option4,cm5name:option5,'intermediaries':option7}#cm6name:option6}

        # Calculate total_num, total_price, discount, and balance_due
        total_num = option1 #+ option2 + option3 + option4 + option5 + option6 + option7
        price = 25 # Example price, this could be dynamic
        total_price = total_num * price

        # Calculate discount
        if total_num > 200:
            discount = 0.4 * total_price
        elif total_num > 100:
            discount = 0.2 * total_price
        else:
            discount = 0

        balance_due = total_price - discount

        # Save the data to the model
        report.purchased_matches = json.dumps(purchase_dict)
        report.total_num = total_num
        report.total_price = total_price
        report.discount = discount
        report.balance_due = balance_due
        report.price = price
        # Save the model instance
        report.save()    

        return render(request,'finfo.html',{'table':html_table,'list_name':top_6_name})#,'table_i':html_table_2})
        # Redirect to the same page to display the updated data
        #return JsonResponse(json_data, safe=False)

        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        return response


    output_list = top_6_name

    # In the dictionary pdf_documents for the final pdf download to properly work, definition should come first,faq second and tewelve variable report third. This order determines the order in the letter.
    # In the dictionary pdf_documents for the final pdf download to properly work, definition should come first,faq second and tewelve variable report third. This order determines the order in the letter.
    pdf_documents = {
        'Accelerator' : [accelerator.accelerator(request),accelerator.acceleratorfaq(request),accelerator.acceleratortwelve(request)],
        'Bonds' : [bonds.bonds(request),bonds.bondsfaq(request),bonds.bondstwelve(request)],
        'Bootstrapped' : [bootstrapped.bootstrapped(request),bootstrapped.bootstrappedfaq(request),bootstrapped.bootstrappedtwelve(request)],
        'Commercial Banking' : [commercialbanking.commercialbanking(request),commercialbanking.commercialbankingfaq(request),commercialbanking.commercialbankingtwelve(request)],
        'Cryptocurrency' : [cryptocurrency.cryptocurrency(request),cryptocurrency.cryptocurrencyfaq(request),cryptocurrency.cryptocurrencytwelve(request)],
        'Factoring' : [factoring.factoring(request),factoring.factoringfaq(request),factoring.factoringtwelve(request)],
        'Grants' : [grants.grants(request),grants.grantsfaq(request),grants.grantstwelve(request)],
        'Hedge Funds' : [hedgefunds.hedgefunds(request),hedgefunds.hedgefundsfaq(request),hedgefunds.hedgefundstwelve(request)],
        'Incubator' : [incubator.incubator(request),incubator.incubatorfaq(request),incubator.incubatortwelve(request)],
        'Investment Banking' : [investmentbanking.investmentbanking(request),investmentbanking.investmentbankingfaq(request),investmentbanking.investmentbankingtwelve(request)],
        'Private Debt' : [privatedebt.privatedebt(request),privatedebt.privatedebtfaq(request),privatedebt.privatedebttwelve(request)],
        'Private Equity Securities' : [privateequitysecurities.privateequitysecurities(request),privateequitysecurities.privateequitysecuritiesfaq(request),privateequitysecurities.privateequitysecuritiestwelve(request)],
        'Royalty Financing' : [royaltyfinancing.royaltyfinancing(request),royaltyfinancing.royaltyfinancingfaq(request),royaltyfinancing.royaltyfinancingtwelve(request)],
        'Small Business Administration (SBA)' : [SmallBusinessAdministration.SmallBusinessAdministration(request),SmallBusinessAdministration.SmallBusinessAdministrationfaq(request),SmallBusinessAdministration.SmallBusinessAdministrationtwelve(request)],
        'Third Party Corporate Credit' : [thirdpartycorporatecredit79.thirdpartycorporatecredit(request),thirdpartycorporatecredit79.thirdpartycorporatecreditfaq(request),thirdpartycorporatecredit79.thirdpartycorporatecredittwelve(request)],
        'Tokenization' : [tokenization80.tokenization(request),tokenization80.tokenizationfaq(request),tokenization80.tokenizationtwelve(request)],
        'Venture Capital' : [venturecapital.venturecapital(request),venturecapital.venturecapitalfaq(request),venturecapital.venturecapitaltwelve(request)],
        }
    
    # Definition,faq and twelvev variables would http content and decode it to utf-8 from the http response object for top capital market match which would be used to generate pdf. 
    definition = "Temporary sollution"# mark_safe(pdf_documents[cm1name][0].content.decode('utf-8'))
    faq_que = "Temporary sollution"# mark_safe(pdf_documents[cm1name][1].content.decode('utf-8'))
    twelvev = "Temporary sollution" #mark_safe(pdf_documents[cm1name][2].content.decode('utf-8'))

    cost_dict = {
        'Accelerator': '$2,500 to $25,000',
        'Bonds' : '$50,000 to $250,000',
        'Bootstrapped' : '0 to $5,000',
        'Commercial Banking': '0 to $5,000',
        'Cryptocurrency' : '$1,000 to 25,000',
        'Factoring' : '0 to $5,000',
        'Grants' : '$250 to $10,000',
        'Hedge Funds' : '$10,000 to $25,000',
        'Incubator' : '0 to $25,000',
        'Investment Banking' : '$20,000 to $75,000',
        'Private Debt' : '0 to $5,000',
        'Royalty Financing': '$2,500 to $10,000',
        'Third Party Corporate Credit': '$10,000 to $25,000',     
        'Private Equity Securities' : '$25,000 to $150,000',
        'Venture Capital' : '$25,000 $150,000',
        'Tokenization' : '$1,000 to $15,000',
        'Small Business Administration (SBA)' : '$500 to $2,500',
    }

    context = {
        'date':date,
        'firstname':firstname,
        'lastname':lastname,
        'address':primary_business_adress,
        'phone' :business_phone,
        'email': primary_email,
        'businessname' : company_name,
        'count': cm_type_count,
        'fundgoal': fundgoal, 
        'totalnum': total_matches,
        'cm1name': cm1name,
        'cm1nameoutput':output_list[0],
        'cm2name': cm2name,
        'cm2nameoutput':output_list[1],
        'cm3name': cm3name,
        'cm3nameoutput':output_list[2],
        'cm4name': cm4name,
        'cm5name': cm5name,
        'cm1no':cm1num,
        'cm2no':cm2num,
        'cm3no':cm3num,
        'cm4no':cm4num,
        'cm5no':cm5num,
        'price':price,
        'totalprice':totalprice,
        'discount':discount,
        'balancedue':balancedue,
        'report':report,
        'list_name':top_6_name,
        'info':info,
        'definition' : definition,
        'faq_que' : faq_que,
        'twelvev' : twelvev,
        #'cost' : cost_dict[cm1name],
    }

    #Saving individual variable for output to share in api endpoint
    try:
        output = Letter_Response.objects.get(user=request.user)

    except Letter_Response.DoesNotExist:
        output = Letter_Response(user=request.user)

    output.firstname = firstname
    output.lastname = lastname
    output.address = primary_business_adress
    output.phone = business_phone
    output.email = primary_email
    output.businessname = company_name
    output.count = cm_type_count
    output.fundgoal = fundgoal
    output.totalnum = total_matches
    output.cm1name = cm1name
    output.cm2name = cm2name
    output.cm3name = cm3name
    output.cm4name = cm4name
    output.cm5name = cm5name
    #output.cm6name = cm6name
    output.cm1no = cm1num
    output.cm2no = cm2num
    output.cm3no = cm3num
    output.cm4no = cm4num
    output.cm5no = cm5num
    output.price = price
    output.totalprice = totalprice
    output.discount = discount
    output.balancedue = balancedue
    output.top_6_name = top_6_name
    output.top_6_name_output = output_list
    output.save()


    
    rendered_html = render_to_string('letter499pdf.html',context)

    soup = BeautifulSoup(rendered_html,"html.parser")
    # Create a Word document
    document = Document()
    
    # Set default font to Times New Roman 10pt
    style = document.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(10)
    
    section = document.sections[-1]

    # Reduce header space
    #section.top_margin = Inches(0.5)
    #section.header_distance = Inches(0.1)
    header = section.header
    header_paragraph = header.paragraphs[0]
    if (company_name.strip()).lower() == "none":
        header_paragraph.text = "FINFIRE REPORT"
    else:
        header_paragraph.text = f"{company_name} FINFIRE REPORT"
    header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header_paragraph.runs[0]
    header_run.bold = False
    header_run.font.size = Pt(10)
    header_run.font.name = "Times New Roman"
    
    # Add logo
    img_paragraph = document.add_paragraph()
    img_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    img_run = img_paragraph.add_run()    
    img_run.add_picture(os.path.join(settings.BASE_DIR, 'static', 'img', 'b.png'),width=Inches(2.44),height=Inches(0.656))
    
    # Process each container
    containers = soup.find_all('div', class_='container')
    for idx, container in enumerate(containers):
        content_divs = container.find_all('div', class_='content')
        for content_div in content_divs:
            # Process all elements in the content
            for element in content_div.find_all(['p', 'center', 'div']):
                if element.name == "center":
                    paragraph = document.add_paragraph()
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

                    # Handle centered content with nested formatting
                    if (element.find('b') and element.find('u')):
                        run = paragraph.add_run(element.text.strip())
                        run.bold = True
                        run.underline = True
                        run.font.name = 'Times New Roman'
                        run.font.size = Pt(10)
                    else:
                        run = paragraph.add_run(element.text.strip())
                        run.font.name = 'Times New Roman'
                        run.font.size = Pt(10)

                elif element.name == "p":
                    paragraph = document.add_paragraph()
                    paragraph.style = document.styles['Normal']

                    # Handle nested elements within paragraph
                    for part in element.contents:
                        if isinstance(part, str):
                            # Handle plain text
                            run = paragraph.add_run(part.strip())
                            run.font.name = 'Times New Roman'
                            run.font.size = Pt(10)
                        elif part.name == "br":
                            # Handle line breaks
                            paragraph.add_run().add_break(WD_BREAK.LINE)
                        elif part.name == "b":
                            # Handle bold text
                            run = paragraph.add_run(part.text.strip())
                            run.bold = True
                            run.font.name = 'Times New Roman'
                            run.font.size = Pt(10)
                        elif part.name == "u":
                            # Handle underlined text
                            run = paragraph.add_run(part.text.strip())
                            run.underline = True
                            run.font.name = 'Times New Roman'
                            run.font.size = Pt(10)
                        elif part.name == "a":
                            # Handle links
                            run = paragraph.add_run(part.text.strip())
                            run.font.name = 'Times New Roman'
                            run.font.size = Pt(10)
                            run.font.color.rgb = RGBColor(0, 0, 255)  # Blue color for links

                elif element.name == "div" and 'class' in element.attrs:
                    pass
                    #if 'signature' in element.attrs['class']:
                    #    # Handle signature section
                    #    signature_paragraph = document.add_paragraph()
                    #    signature_paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    #    try:
                    #        signature_run = signature_paragraph.add_run()
                    #        signature_run.add_picture(
                    #            os.path.join(settings.BASE_DIR, 'static', 'img', 'nick_cope.png'),
                    #            width=Inches(1.52),height=Inches(0.51)
                    #        )
                    #    except FileNotFoundError:
                    #        fallback_paragraph = document.add_paragraph()
                    #        fallback_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    #        fallback_paragraph.add_run("[Signature]")

        # Add page break after each container except the last
        if idx < len(containers) - 1:
            # Get the last paragraph in the document
            last_paragraph = document.paragraphs[-1]
            # Add the page break directly to the last run of the last paragraph
            if last_paragraph.runs:
                last_paragraph.runs[-1].add_break(WD_BREAK.PAGE)
            else:
                # If no runs exist in the paragraph, add a run with the break
                last_paragraph.add_run().add_break(WD_BREAK.PAGE)

    # Add footer
    section = document.sections[-1]
    footer = section.footer
    footer_paragraph = footer.paragraphs[0]
    footer_paragraph.text = "4760 S. Pecos Road, Suite 100-28, Las Vegas, NV 89121"
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_paragraph.style.font.size = Pt(8)
    footer_paragraph.style.font.name = 'Times New Roman'
    # Create response for download
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = 'attachment; filename="FINFIRE_Letter.docx"'
    document.save(response)
    return response




    





    





