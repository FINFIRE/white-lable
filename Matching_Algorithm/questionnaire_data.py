"""
Questionnaire data extraction for the Matching Algorithm.

Loads all user survey responses from the 12-step questionnaire models
and converts them into a flat values list used by the matching engine.
"""
from datetime import datetime
from django.http import HttpResponse
from entreprise_questions.models import (
    EQuestions, EQuestions1, EQuestions2, EQuestions3, EQuestions4,
    EQuestions5, EQuestions6, EQuestions7, EQuestions8, DocumentsPrepared,
)
from registration.models import UserDetail, UserDetail2
from entreprise_questions.models import LendingRequirements


def _encode_collateral(status):
    """Convert collateral status string to one-hot encoded list [not_applicable, yes, no, other]."""
    mapping = {"Not Applicable": 0, "Yes": 1, "No": 2}
    idx = mapping.get(status, 3)
    result = [0, 0, 0, 0]
    result[idx] = 1
    return result


def _encode_credit_score(score):
    """Convert credit score string to one-hot encoded list [<580, >620, >680, >720, >760]."""
    mapping = {"<580": 0, ">620": 1, ">680": 2, ">720": 3}
    idx = mapping.get(score, 4)
    result = [0, 0, 0, 0, 0]
    result[idx] = 1
    return result


def _encode_criminal_history(history):
    """Convert criminal history string to one-hot [none, misdemeanor, felony, fraud, securities]."""
    mapping = {"None": 0, "Misdemeanor": 1, "Felony": 2, "Fraud": 3}
    idx = mapping.get(history, 4)
    result = [0, 0, 0, 0, 0]
    result[idx] = 1
    return result


def load_user_profile(user):
    """
    Load user contact and business profile information.

    Returns a dict with keys: firstname, lastname, date, primary_business_adress,
    business_phone, fundgoal, mobile_phone, primary_email, company_website, company_name.
    Raises an exception if any required data is missing.
    """
    user_detail = UserDetail.objects.get(user=user)
    eq5 = EQuestions5.objects.get(user=user)
    eq2 = EQuestions2.objects.get(user=user)

    return {
        'firstname': user_detail.First_Name,
        'lastname': user_detail.Last_Name,
        'date': datetime.now().strftime('%B %d, %Y'),
        'primary_business_adress': user_detail.Business_Adress,
        'business_phone': user_detail.Business_Phone,
        'fundgoal': eq5.Selected_Option[:],
        'mobile_phone': user_detail.Mobile_Phone,
        'primary_email': user_detail.User_Email,
        'company_website': user_detail.Company_Website,
        'company_name': eq2.Business_Name,
    }


def load_questionnaire_values(user):
    """
    Load all questionnaire answers as a flat numeric list for the matching algorithm.

    Returns a list of 0/1 integer values representing user selections across
    all 12 questionnaire steps plus lending requirements encoding.
    """
    eq1 = EQuestions1.objects.get(user=user)
    eq2 = EQuestions2.objects.get(user=user)
    eq3 = EQuestions3.objects.get(user=user)
    eq4 = EQuestions4.objects.get(user=user)
    eq5 = EQuestions5.objects.get(user=user)
    eq6 = EQuestions6.objects.get(user=user)
    eq7 = EQuestions7.objects.get(user=user)
    eq8 = EQuestions8.objects.get(user=user)
    eq = EQuestions.objects.get(user=user)
    docs = DocumentsPrepared.objects.get(user=user)
    lending = LendingRequirements.objects.get(user=user)

    values = [
        # EQuestions1 - Stage of company (7 fields)
        eq1.Idea, eq1.Formation, eq1.Start_Up, eq1.Growth,
        eq1.M_And_A, eq1.Preparing_For_Public, eq1.Distressed,
        # EQuestions2 - Entity type (8 fields)
        eq2.No_Business, eq2.Sole_Proprietorship, eq2.LLC, eq2.LP,
        eq2.GP, eq2.S_Corporation, eq2.C_Corp, eq2.Other,
        # EQuestions3 - Pre-capital raised (9 fields)
        eq3.Less_25k, eq3.More_25K_Less_100k, eq3.More_100k_Less_250K,
        eq3.More_250k_Less_500K, eq3.More_500K_Less_1M, eq3.More_1M_Less_2M,
        eq3.More_2M_Less_5M, eq3.More_5M_Less_10M, eq3.More_10M,
        # EQuestions4 - Capital market preferences (20 fields)
        eq4.Accelerator, eq4.Bonds, eq4.Comercial_Banking, eq4.Cryptocurrency,
        eq4.EB5_Immigration, eq4.Enterprise_Zones, eq4.Factoring, eq4.Grants,
        eq4.Hedge_Funds, eq4.Incubator, eq4.Investment_Banking, eq4.Other_Owner_Equity,
        eq4.Private_Debt, eq4.Private_Equity, eq4.Public_Offereing, eq4.Real_Estate,
        eq4.Royalty_Financing, eq4.Small_Business_Administration, eq4.Venture_Capital,
        eq4.Unsure,
        # EQuestions5 - Planned raise amount (12 fields)
        eq5.Less_25k, eq5.More_25K_Less_100k, eq5.More_100k_Less_250K,
        eq5.More_250k_Less_500K, eq5.More_500K_Less_1M, eq5.More_1M_Less_1_35M,
        eq5.More_1_35M_Less_2M, eq5.More_2M_Less_5M, eq5.More_5M_Less_10M,
        eq5.More_10M_Less_20M, eq5.More_20M, eq5.Unsure,
        # EQuestions6 - Rounds (12 fields)
        eq6.Founders_Round, eq6.Pre_Seed, eq6.Seed, eq6.Series_A,
        eq6.Series_B, eq6.Series_C, eq6.Pre_Ipo, eq6.Ipo,
        eq6.Unsure, eq6.One, eq6.Two, eq6.TBD,
        # EQuestions7 - Use of funds (11 fields)
        eq7.Start_Up, eq7.Growth_Scalabitlity, eq7.Marketing_and_Sales,
        eq7.Cash_FLow_Capital, eq7.Human_Capital, eq7.Equipment,
        eq7.Merger_and_Acquistions, eq7.Inventory, eq7.Real_State,
        eq7.Other, eq7.Unsure,
        # EQuestions8 - Risk and cost tolerance (8 fields)
        eq8.Low_Risk_Tolerance, eq8.Medium_Risk_Tolerance, eq8.High_Risk_Tolerance,
        eq8.Low_Cost_Capital, eq8.Medium_Cost_Capital, eq8.High_Cost_Capital,
        eq8.Very_High_Cost_Capital, eq8.Immaterial_Cost_Capital,
        # EQuestions - Range of cost (8 fields)
        eq.RC_zero_to_499, eq.RC_500_to_999, eq.RC_1000_to_2499,
        eq.RC_2500_to_4999, eq.RC_5000_to_9999, eq.RC_10000_to_24999,
        eq.RC_25000_to_49999, eq.RC_More_Than_50000,
        # EQuestions - Range of timing (8 fields)
        eq.RT_1D_to_1W, eq.RT_1W_to_2W, eq.RT_2W_to_4W,
        eq.RT_1M_to_2M, eq.RT_2M_to_3M, eq.RT_3M_to_6M,
        eq.RT_6M_to_12M, eq.RT_More_Than_a_Year,
        # DocumentsPrepared (9 fields)
        docs.summary_of_offering, docs.financial_forecast, docs.lean_business_model,
        docs.presentation_deck, docs.leadership_overview, docs.exit_strategy,
        docs.offering_documents, docs.ai_generated_deep_dive, docs.virtual_data_room,
    ]

    # Append lending requirement encodings (collateral 4 + credit 5 + criminal 5 = 14)
    values += _encode_collateral(lending.collateral_status)
    values += _encode_credit_score(lending.credit_score)
    values += _encode_criminal_history(lending.criminal_history)

    return values


def load_summary_context(user):
    """Load all data needed for the summary view."""
    user_detail = UserDetail.objects.get(user=user)
    user_detail2 = UserDetail2.objects.get(user=user)
    eq1 = EQuestions1.objects.get(user=user)
    eq2 = EQuestions2.objects.get(user=user)
    eq3 = EQuestions3.objects.get(user=user)
    eq4 = EQuestions4.objects.get(user=user)
    eq5 = EQuestions5.objects.get(user=user)
    eq6 = EQuestions6.objects.get(user=user)
    eq7 = EQuestions7.objects.get(user=user)
    eq8 = EQuestions8.objects.get(user=user)
    eq = EQuestions.objects.get(user=user)
    docs = DocumentsPrepared.objects.get(user=user)

    return {
        'first_name': user_detail.First_Name,
        'middle_name': user_detail.Middle_Name,
        'last_name': user_detail.Last_Name,
        'affiliation': user_detail.Affiliation,
        'primary_email': user_detail.User_Email,
        'website': user_detail.Company_Website,
        'address': user_detail.Business_Adress,
        'business_phone': user_detail.Business_Phone,
        'mobile_phone': user_detail.Mobile_Phone,
        'special_program': user_detail.Special_Programs,
        'primary_purpose': user_detail2.Primary_Purpose,
        'account_type': user_detail2.Account_Type,
        'billing_option': user_detail2.Billing_Option,
        'stage': eq1.Selected_Option,
        'entity_name': eq2.Business_Name,
        'entity_state': eq2.Registration_Region,
        'entity_type': eq2.Selected_Option,
        'raised_capital': eq3.Selected_Option,
        'capital_till_date': eq4.Selected_Options,
        'planned_raise': eq5.Selected_Option,
        'round_type': eq6.Selected_Options,
        'round_tranches': eq6.Selected_Option,
        'use_of_funds': eq7.Selected_Options,
        'risk_tolerance_investor': eq8.Selected_Option,
        'risk_tolerance_enterprise': eq8.Selected_Option2,
        'up_front_cost': eq.Selected_Option,
        'up_front_timming': eq.Selected_Option2,
        'summary_of_offering': docs.summary_of_offering,
        'financials': docs.financial_forecast,
        'lean_business_model_canvas': docs.lean_business_model,
        'presentation_deck': docs.presentation_deck,
        'leadership_overview': docs.leadership_overview,
        'exit_strategy': docs.exit_strategy,
        'offering_documents': docs.offering_documents,
        'ai_generated_deep_dive': docs.ai_generated_deep_dive,
        'virtual_data_room': docs.virtual_data_room,
    }


def load_payload_data(user):
    """Load data needed to build the webhook payload JSON body."""
    user_detail = UserDetail.objects.get(user=user)
    user_detail2 = UserDetail2.objects.get(user=user)
    eq = EQuestions.objects.get(user=user)
    eq1 = EQuestions1.objects.get(user=user)
    eq2 = EQuestions2.objects.get(user=user)
    eq4 = EQuestions4.objects.get(user=user)
    eq5 = EQuestions5.objects.get(user=user)
    eq6 = EQuestions6.objects.get(user=user)
    eq7 = EQuestions7.objects.get(user=user)
    eq8 = EQuestions8.objects.get(user=user)
    docs = DocumentsPrepared.objects.get(user=user)
    from entreprise_questions.models import ReferalResponse
    referral = ReferalResponse.objects.get(user=user)

    return {
        "email": user_detail.User_Email,
        "timing": eq.Selected_Option2,
        "fundsUse": eq7.Selected_Options,
        "entityName": eq2.Business_Name,
        "entityType": eq2.Selected_Option,
        "mobilePhone": user_detail.Mobile_Phone,
        "rangeofCost": eq.Selected_Option,
        "display_name": f"{user_detail.First_Name} {user_detail.Last_Name}",
        "exitStrategy": docs.exit_strategy,
        "plannedRaise": eq5.Selected_Option,
        "businessPhone": user_detail.Business_Phone,
        "currentRounds": eq6.Selected_Options,
        "howManyRounds": eq6.Selected_Option,
        "primaryAppUse": user_detail2.Primary_Purpose,
        "companyWebsite": user_detail.Company_Website,
        "stageofCompany": eq1.Selected_Option,
        "preCapitalRaise": EQuestions3.objects.get(user=user).Selected_Option,
        "specialPrograms": user_detail.Special_Programs,
        "virtualDataroom": docs.virtual_data_room,
        "presentationDeck": docs.presentation_deck,
        "capitalPreMarkets": eq4.Selected_Options,
        "financialForecast": docs.financial_forecast,
        "offeringDocuments": docs.offering_documents,
        "summaryofOffering": docs.summary_of_offering,
        "companyAffiliation": user_detail.Affiliation,
        "leadershipOverview": docs.leadership_overview,
        "aiGeneratedDeepDive": docs.ai_generated_deep_dive,
        "riskToleranceFounder": eq8.Selected_Option,
        "riskToleranceInvestor": eq8.Selected_Option2,
        "primaryBusinessAddress": user_detail.Business_Adress,
        "leanBusinessModelCanvas": docs.lean_business_model,
        "entityStateofRegistration": eq2.Registration_Region,
        "referralSource": referral.referral_source,
        "referrerName": referral.referrer_name,
        "referralOther": referral.referral_other,
    }
