from django.shortcuts import render
from .forms import UserSelectionForm, manualCapitalTypeform
from registration.models import UserDetail
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared,ReferalResponse,LendingRequirements
from connections.models import Match_Data
from Matching_Algorithm.models import Letter_Response
from Matching_Algorithm.views import Match
from registration.forms import RegistrationFormOne
from entreprise_questions.forms import EQuestionsForma,EQuestionsFormb,EQuestions1Form,EQuestions2Form,EQuestions3Form,EQuestions4Form,EQuestions5Form,EQuestions6Form,EQuestions7Form,EQuestions8Form,DocumentsPreparedForm,ReferralResponseForm,LendingRequirementsForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import FileResponse
from django.urls import reverse
import os
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

allowed_user = ['tonyfinfire','rominadmin','hudson','sam']

@login_required
@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
def download_file(request):
    file_path = os.path.join(os.path.dirname(__file__), 'templates', 'finfireagreement.docx')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='finfireagreement.docx')

@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
def manual_match(request):
    url = reverse('master-review')
    selected_user_id = request.session.get('selected_user_id')
    if selected_user_id:
        try:
            selected_user = User.objects.get(id=selected_user_id)
            #context_vars['selected_user'] = selected_user
            #responses = UserDetail.objects.filter(user=selected_user)
        except User.DoesNotExist:
            del request.session['selected_user_id']
    

    if request.method == "POST":
        form = UserSelectionForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['user']
            request.session['selected_user_id'] = selected_user.id
    request.user = selected_user
    Match(request)
    if 'selected_user_id' in request.session:
        del request.session['selected_user_id']
    dashboard_url = reverse('master-review')
    return HttpResponse(f"""Success!<a href='{dashboard_url}'> Back to Dashboard</a>""")

@login_required
@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
def superuser_dashboard(request):
    selected_user = None
    responses = True
    letter_content = None
    stage = None
    entity_state = None
    entity_name = None
    form = None
    form2 = None
    form3 = None
    form4 = None
    form5 = None
    form6 = None
    form7 = None
    form8 = None
    form9 = None
    form10 = None
    form11 = None
    form12 = None
    form13 = None
    form14 = None
    form15 = None
    form16 = None
    url = reverse('master-review')

    # Session handling for selected user
    selected_user_id = request.session.get('selected_user_id')
    if selected_user_id:
        try:
            selected_user = User.objects.get(id=selected_user_id)
            #context_vars['selected_user'] = selected_user
            #responses = UserDetail.objects.filter(user=selected_user)
        except User.DoesNotExist:
            del request.session['selected_user_id']
    

    if request.method == "POST":
        # Check if this is a user selection or unified form submission
        if 'user' in request.POST:
            # This is the user selection form
            form = UserSelectionForm(request.POST)
            if form.is_valid():
                selected_user = form.cleaned_data['user']
                request.session['selected_user_id'] = selected_user.id
                # Initialize all forms with existing data
                try:
                    responseregistration = UserDetail.objects.get(user=selected_user)
                    initial_dataregistration_stage = {
                        'user':selected_user,
                        'First_Name':responseregistration.First_Name,
                        'Middle_Name': responseregistration.Middle_Name,
                        'Last_Name':responseregistration.Last_Name,
                        'Affiliation':responseregistration.Affiliation,
                        'User_Email':responseregistration.User_Email,
                        'Company_Website':responseregistration.Company_Website,
                        'Business_Adress': responseregistration.Business_Adress,
                        'Business_Phone':responseregistration.Business_Phone,
                        'Mobile_Phone':responseregistration.Mobile_Phone,
                        'Special_Programs':responseregistration.Special_Programs,
                    }                           
                except UserDetail.DoesNotExist:
                    responseregistration = UserDetail(user=selected_user) #
                    initial_dataregistration_stage = {}                

                try:    
                    responsestage = EQuestions1.objects.get(user=selected_user)
                    initial_data_stage = {
                        'user':selected_user,
                        'selected_option':responsestage.Selected_Option,
                    }
                except EQuestions1.DoesNotExist:    
                    responsestage = EQuestions1(user=selected_user)
                    initial_data_stage = {}
                try:
                    responseentity = EQuestions2.objects.get(user=selected_user)
                    initial_data_entity ={
                                'user':selected_user,
                                'Business_Name':responseentity.Business_Name,
                                'selected_option':responseentity.Selected_Option,
                                'Registration_Region':responseentity.Registration_Region,
                    }
                except EQuestions2.DoesNotExist:    
                    responseentity =EQuestions2(user=selected_user)
                    initial_data_entity= {}
                
                try:
                    responseprecapital = EQuestions3.objects.get(user=selected_user)
                    initial_data_precapital={
                        'user':selected_user,
                        'selected_option':responseprecapital.Selected_Option,
                    }
                except EQuestions3.DoesNotExist:    
                    responseprecapital = EQuestions3(user=selected_user)
                    initial_data_precapital = {}

                try:    
                    responsepremarket = EQuestions4.objects.get(user=selected_user)
                    initial_data_premarket = {
                        'user':selected_user,
                        'Market':responsepremarket.Selected_Options,
                    }
                except EQuestions4.DoesNotExist:    
                    responsepremarket = EQuestions4(user=selected_user)
                    initial_data_premarket = {}

                try:                                     
                    responseplannedraise = EQuestions5.objects.get(user=selected_user)
                    initial_data_plannedraise ={
                        'user':selected_user,
                        'selected_option':responseplannedraise.Selected_Option,
                    }            
                except EQuestions5.DoesNotExist:    
                    responseplannedraise = EQuestions5(user=selected_user)
                    initial_data_plannedraise = {}                

                try:    
                    responserounds = EQuestions6.objects.get(user=selected_user)
                    initial_data_rounds = {
                        'user':selected_user,
                        'capital_market':responserounds.Selected_Options,
                        'selected_option':responserounds.Selected_Option
                    }
                except EQuestions6.DoesNotExist:    
                    responserounds = EQuestions6(user=selected_user)
                    initial_data_rounds = {}
                
                try:
                    responseuseoffunds = EQuestions7.objects.get(user=selected_user)
                    initial_data_useoffunds = {
                        'user':selected_user,
                        'selected_uses':responseuseoffunds.Selected_Options,
                    }
                except EQuestions7.DoesNotExist:    
                    responseuseoffunds = EQuestions7(user=selected_user)
                    initial_data_useoffunds = {}
                try:                                                    
                    responserisk = EQuestions8.objects.get(user=selected_user)
                    initial_data_risk={
                        'user':selected_user,
                        'selected_option1':responserisk.Selected_Option,
                        'selected_option2':responserisk.Selected_Option2,
                    }
                except EQuestions8.DoesNotExist:    
                    responserisk = EQuestions8(user=selected_user)
                    initial_data_risk = {}
                try:
                    responseupfrontcost = EQuestions.objects.get(user=selected_user)
                    responsetiming = EQuestions.objects.get(user=selected_user)
                    initial_data_upfrontcost = {
                        'user':selected_user,
                        'upfrontcost':responseupfrontcost.Selected_Option,
                        'timming':responsetiming.Selected_Option2,
                    }
                    initial_data_timing={
                        'user':selected_user,
                        'timming':responsetiming.Selected_Option2,                    
                    }
                                    
                except EQuestions.DoesNotExist:    
                    responseupfrontcost = EQuestions(user=selected_user)
                    responsetiming = EQuestions(user=selected_user)
                    initial_data_timing = {}
                    initial_data_upfrontcost = {}
                try:
                    responsedocumentsprepared = DocumentsPrepared.objects.get(user=selected_user)
                    initial_data_documentsprepared = {
                        'user':selected_user,
                        'summary_of_offering':responsedocumentsprepared.summary_of_offering,
                        'financial_forecast':responsedocumentsprepared.financial_forecast,
                        'lean_business_model_canvas':responsedocumentsprepared.lean_business_model,
                        'presentation_deck': responsedocumentsprepared.presentation_deck,
                        'leadership_overview': responsedocumentsprepared.leadership_overview,
                        'exit_strategy':responsedocumentsprepared.exit_strategy,
                        'offering_documents': responsedocumentsprepared.offering_documents,
                        'ai_generated_deep_dive':responsedocumentsprepared.ai_generated_deep_dive,
                        'virtual_data_room':responsedocumentsprepared.virtual_data_room
                    }                 

                except DocumentsPrepared.DoesNotExist:    
                    responsedocumentsprepared = DocumentsPrepared(user=selected_user)
                    initial_data_documentsprepared = {}
                
                try:
                    responsereferral = ReferalResponse.objects.get(user=selected_user)
                    initial_data_referral = {
                        'user':selected_user,
                        'referral_source':responsereferral.referral_source,
                        'referrer_name':responsereferral.referrer_name,
                        'referral_other':responsereferral.referral_other,
                    }
                except ReferalResponse.DoesNotExist:
                    responsereferral = ReferalResponse(user=selected_user)
                    initial_data_referral = {}
                
                try:
                    responselending = LendingRequirements.objects.get(user=selected_user)
                    initial_data_lending = {
                        'user':selected_user,
                        'collateral_status':responselending.collateral_status,
                        'credit_score':responselending.credit_score,
                        'criminal_history':responselending.criminal_history,
                    }
                except LendingRequirements.DoesNotExist:
                    responsereferral = LendingRequirements(user=selected_user)
                    initial_data_lending = {}                    
                try:
                    responsecapitalranks = Letter_Response.objects.get(user=selected_user)
                    initial_data_capitaltype = {
                        'rankone' : responsecapitalranks.top_6_name_output[0],
                        'ranktwo' : responsecapitalranks.top_6_name_output[1],
                        'rankthree' : responsecapitalranks.top_6_name_output[2],
                        'rankfour' : responsecapitalranks.top_6_name_output[3],
                        'rankfive' : responsecapitalranks.top_6_name_output[4],
                        'status' : responsecapitalranks.top_6_name_output[5],
                    }
                except IndexError:
                    responsecapitalranks = Letter_Response.objects.get(user=selected_user)
                    try:
                        rankone = responsecapitalranks.top_6_name_output[0]
                    except:
                        rankone = 'Accelerator'
                    try:
                        ranktwo = responsecapitalranks.top_6_name_output[1]
                    except:
                        ranktwo = 'Accelerator'
                    try:
                        rankthree = responsecapitalranks.top_6_name_output[2]
                    except:
                        rankthree = 'Accelerator'
                    try:
                        rankfour = responsecapitalranks.top_6_name_output[3]
                    except:
                        rankfour = 'Accelerator'
                    try:
                        rankfive = responsecapitalranks.top_6_name_output[4]
                    except:
                        rankfive = 'Accelerator'                        
                    initial_data_capitaltype = {
                        'rankone' :rankone,
                        'ranktwo' : ranktwo,
                        'rankthree' : rankthree,
                        'rankfour' : rankfour,
                        'rankfive' : rankfive,
                        'status' : False,               
                    }
                    #return HttpResponse("This user has not trigered new match function!<p>Their data would be availabe once they click match from their account or we manually triger match and intergrate old user to latest changes.")
                    
                except Letter_Response.DoesNotExist:
                    initial_data_capitaltype = {}                
            else:
                form = UserSelectionForm()
        else:
            # This is the unified form submission
            selected_user_id = request.session.get('selected_user_id')
            if selected_user_id:
                try:
                    selected_user = User.objects.get(id=selected_user_id)
                    # Process all forms in the unified submission
                    form2 = RegistrationFormOne(request.POST, prefix="form2")
                    form3 = EQuestions1Form(request.POST, prefix="form3")
                    form4 = EQuestions2Form(request.POST, prefix="form4")
                    form5 = EQuestions3Form(request.POST, prefix="form5")
                    form6 = EQuestions4Form(request.POST, prefix="form6")
                    form7 = EQuestions5Form(request.POST, prefix="form7")
                    form8 = EQuestions6Form(request.POST, prefix="form8")
                    form9 = EQuestions7Form(request.POST, prefix="form9")
                    form10 = EQuestions8Form(request.POST, prefix="form10")
                    form11 = EQuestionsForma(request.POST, prefix="form11")
                    form12 = EQuestionsFormb(request.POST, prefix="form12")
                    form13 = DocumentsPreparedForm(request.POST, prefix="form13")
                    form14 = manualCapitalTypeform(request.POST, prefix="form14")
                    form15 = ReferralResponseForm(request.POST, prefix="form15")
                    form16 = LendingRequirementsForm(request.POST, prefix = "form16")
                    
                    # Process each form if valid
                    if form2.is_valid():
                        responseregistration, created = UserDetail.objects.get_or_create(user=selected_user)
                        responseregistration.user = selected_user
                        responseregistration.First_Name = form2.cleaned_data['First_Name']
                        responseregistration.Middle_Name = form2.cleaned_data['Middle_Name']
                        responseregistration.Last_Name = form2.cleaned_data['Last_Name']
                        responseregistration.Affiliation = form2.cleaned_data['Affiliation']
                        responseregistration.User_Email = form2.cleaned_data['User_Email']
                        responseregistration.Company_Website = form2.cleaned_data['Company_Website']
                        responseregistration.Business_Adress = form2.cleaned_data['Business_Adress']
                        responseregistration.Business_Phone = form2.cleaned_data['Business_Phone']
                        responseregistration.Mobile_Phone = form2.cleaned_data['Mobile_Phone']
                        responseregistration.Special_Programs = form2.cleaned_data['Special_Programs']
                        responseregistration.save()
                    
                    if form3.is_valid():
                        responsestage, created = EQuestions1.objects.get_or_create(user=selected_user)
                        selected_option = form3.cleaned_data['selected_option']
                        option_values = {
                            'Idea': 0, 'Formation': 0, 'Start Up': 0, 'Growth': 0,
                            'M & A': 0, 'Preparing for Public': 0, 'Distressed': 0,
                        }
                        option_values[selected_option] = 1 
                        responsestage.user = selected_user
                        responsestage.Idea = option_values['Idea']
                        responsestage.Formation = option_values['Formation']
                        responsestage.Start_Up = option_values['Start Up']
                        responsestage.Growth = option_values['Growth']
                        responsestage.M_And_A = option_values['M & A']
                        responsestage.Preparing_For_Public = option_values['Preparing for Public']
                        responsestage.Distressed = option_values['Distressed']
                        responsestage.Selected_Option = selected_option
                        responsestage.save()
                    
                    if form4.is_valid():
                        responseentity, created = EQuestions2.objects.get_or_create(user=selected_user)
                        selected_option_form4 = form4.cleaned_data['selected_option']
                        option_values = {
                            'None (To be Determined)': 0, 'Sole Proprietorship': 0, 'LLC': 0,
                            'LP': 0, 'GP': 0, 'S Corporation': 0, 'C Corp': 0, 'Other': 0,
                        }
                        option_values[selected_option_form4] = 1
                        responseentity.user = selected_user
                        responseentity.Selected_Option = form4.cleaned_data['selected_option']
                        responseentity.Business_Name = form4.cleaned_data['Business_Name']
                        responseentity.Registration_Region = form4.cleaned_data['Registration_Region']
                        responseentity.No_Business = option_values['None (To be Determined)']
                        responseentity.Sole_Proprietorship = option_values['Sole Proprietorship']
                        responseentity.LLC = option_values['LLC']
                        responseentity.LP = option_values['LP']
                        responseentity.GP = option_values['GP']
                        responseentity.S_Corporation = option_values['S Corporation']
                        responseentity.C_Corp = option_values['C Corp']
                        responseentity.Other = option_values['Other']
                        responseentity.save()
                    
                    if form5.is_valid():
                        responseprecapital, created = EQuestions3.objects.get_or_create(user=selected_user)
                        selected_option_form5 = form5.cleaned_data['selected_option']
                        option_values = {
                            'Less than $25,000': 0, '$26,000 to $100,000': 0, '$101,000 to $250,000': 0,
                            '$251,000 to $500,000': 0, '$501,000 to $1,000,000': 0, '$1,000,001 to $2,000,000': 0,
                            '$2,000,001 to $5,000,000': 0, '$5,000,001 to $10,000,000': 0, 'More than $10,000,000': 0,
                        }
                        option_values[selected_option_form5] = 1
                        responseprecapital.user = selected_user
                        responseprecapital.Selected_Option = selected_option_form5
                        responseprecapital.Less_25k = option_values['Less than $25,000']
                        responseprecapital.More_25K_Less_100k = option_values['$26,000 to $100,000']
                        responseprecapital.More_100k_Less_250K = option_values['$101,000 to $250,000']
                        responseprecapital.More_250k_Less_500K = option_values['$251,000 to $500,000']
                        responseprecapital.More_500K_Less_1M = option_values['$501,000 to $1,000,000']
                        responseprecapital.More_1M_Less_2M = option_values['$1,000,001 to $2,000,000']
                        responseprecapital.More_2M_Less_5M = option_values['$2,000,001 to $5,000,000']
                        responseprecapital.More_5M_Less_10M = option_values['$5,000,001 to $10,000,000']
                        responseprecapital.More_10M = option_values['More than $10,000,000']
                        responseprecapital.save()
                    
                    if form6.is_valid():
                        responsepremarket, created = EQuestions4.objects.get_or_create(user=selected_user)
                        selected_options_list_form6 = form6.cleaned_data['Market']
                        option_values = {
                            'Accelerator': 0, 'Bonds': 0, 'Commercial Banks': 0, 'Cryptocurrency': 0,
                            'EB5 Immigration': 0, 'Enterprise Zones': 0, 'Factoring': 0, 'Grants': 0,
                            'Hedge Funds': 0, 'Incubator': 0, 'Investment Banking': 0, 'Other (Owner Equity)': 0,
                            'Private Debt (Officer Loans to Startup)': 0, 'Private Equity Securities': 0,
                            'Public Offering': 0, 'Real State': 0, 'Royalty Financing': 0,
                            'Small Business Administration (SBA)': 0, 'Venture Capital': 0, 'Unsure/Do not Know': 0
                        }
                        for selected_option_form6 in selected_options_list_form6:
                            option_values[selected_option_form6] = 1
                        responsepremarket.user = selected_user
                        responsepremarket.Selected_Options = selected_options_list_form6
                        responsepremarket.Accelerator = option_values['Accelerator']
                        responsepremarket.Bonds = option_values['Bonds']
                        responsepremarket.Comercial_Banking = option_values['Commercial Banks']
                        responsepremarket.Cryptocurrency = option_values['Cryptocurrency']
                        responsepremarket.EB5_Immigration = option_values['EB5 Immigration']
                        responsepremarket.Enterprise_Zones = option_values['Enterprise Zones']
                        responsepremarket.Factoring = option_values['Factoring']
                        responsepremarket.Grants = option_values['Grants']
                        responsepremarket.Hedge_Funds = option_values['Hedge Funds']
                        responsepremarket.Incubator = option_values['Incubator']
                        responsepremarket.Investment_Banking = option_values['Investment Banking']
                        responsepremarket.Other_Owner_Equity = option_values['Other (Owner Equity)']
                        responsepremarket.Private_Debt = option_values['Private Debt (Officer Loans to Startup)']
                        responsepremarket.Private_Equity = option_values['Private Equity Securities']
                        responsepremarket.Public_Offereing = option_values['Public Offering']
                        responsepremarket.Real_Estate = option_values['Real State']
                        responsepremarket.Royalty_Financing = option_values['Royalty Financing']
                        responsepremarket.Small_Business_Administration = option_values['Small Business Administration (SBA)']
                        responsepremarket.Venture_Capital = option_values['Venture Capital']
                        responsepremarket.Unsure = option_values['Unsure/Do not Know']
                        responsepremarket.save()
                    
                    if form7.is_valid():
                        responseplannedraise, created = EQuestions5.objects.get_or_create(user=selected_user)
                        selected_option_form7 = form7.cleaned_data['selected_option']
                        option_values = {
                            'Less than $25,000': 0, '$25,000 to $100,000': 0, '$100,000 to $249,999': 0,
                            '$250,000 to $499,999': 0, '$500,000 to $999,999': 0, '$1,000,000 to $1,349,999': 0,
                            '$1,350,000 to $1,999,999': 0, '$2,000,000 to $4,999,999': 0, '$5,000,000 to $9,999,999': 0,
                            '$10,000,000 to $19,999,999': 0, 'More Than $20 Million': 0, 'Unsure/Do not Know/TBD': 0,
                        }
                        option_values[selected_option_form7] = 1
                        responseplannedraise.user = selected_user
                        responseplannedraise.Selected_Option = selected_option_form7
                        responseplannedraise.Less_25k = option_values['Less than $25,000']
                        responseplannedraise.More_25K_Less_100k = option_values['$25,000 to $100,000']
                        responseplannedraise.More_100k_Less_250K = option_values['$100,000 to $249,999']
                        responseplannedraise.More_250k_Less_500K = option_values['$250,000 to $499,999']
                        responseplannedraise.More_500K_Less_1M = option_values['$500,000 to $999,999']
                        responseplannedraise.More_1M_Less_1_35M = option_values['$1,000,000 to $1,349,999']
                        responseplannedraise.More_1_35M_Less_2M = option_values['$1,350,000 to $1,999,999']
                        responseplannedraise.More_2M_Less_5M = option_values['$2,000,000 to $4,999,999']
                        responseplannedraise.More_5M_Less_10M = option_values['$5,000,000 to $9,999,999']
                        responseplannedraise.More_10M_Less_20M = option_values['$10,000,000 to $19,999,999']
                        responseplannedraise.More_20M = option_values['More Than $20 Million']
                        responseplannedraise.Unsure = option_values['Unsure/Do not Know/TBD']
                        responseplannedraise.save()
                    
                    if form8.is_valid():
                        responserounds, created = EQuestions6.objects.get_or_create(user=selected_user)
                        selected_options_list_form8 = form8.cleaned_data['capital_market']
                        selected_option_2_form8 = form8.cleaned_data['selected_option']
                        option_values = {
                            'Founders_Round': 0, 'Pre_Seed': 0, 'Seed': 0, 'Series_A': 0,
                            'Series_B': 0, 'Series_C': 0, 'Pre_Ipo': 0, 'Ipo': 0, 'Unsure': 0,
                        }
                        for selected_option_form8 in selected_options_list_form8:
                            option_values[selected_option_form8] = 1
                        option_values2 = {'One': 0, 'Two': 0, 'TBD': 0}
                        option_values2[selected_option_2_form8] = 1
                        responserounds.user = selected_user
                        responserounds.Selected_Options = selected_options_list_form8
                        responserounds.Selected_Option = selected_option_2_form8
                        responserounds.Founders_Round = option_values['Founders_Round']
                        responserounds.Pre_Seed = option_values['Pre_Seed']
                        responserounds.Seed = option_values['Seed']
                        responserounds.Series_A = option_values['Series_A']
                        responserounds.Series_B = option_values['Series_B']
                        responserounds.Series_C = option_values['Series_C']
                        responserounds.Pre_Ipo = option_values['Pre_Ipo']
                        responserounds.Ipo = option_values['Ipo']
                        responserounds.Unsure = option_values['Unsure']
                        responserounds.One = option_values2['One']
                        responserounds.Two = option_values2['Two']
                        responserounds.TBD = option_values2['TBD']
                        responserounds.save()
                    
                    if form9.is_valid():
                        responseuseoffunds, created = EQuestions7.objects.get_or_create(user=selected_user)
                        selected_options_list_form9 = form9.cleaned_data['selected_uses']
                        option_values = {
                            'Startup -Working': 0, 'Growth Scalability': 0, 'Marketing & Sales': 0,
                            'Cash Flow Capital': 0, 'Human Capital': 0, 'Equipment': 0,
                            'Merger & Acquitions': 0, 'Inventory': 0, 'Real Estate': 0,
                            'Other': 0, 'Do not Know/Unsure/TBD': 0,
                        }
                        for selected_option_form9 in selected_options_list_form9:
                            option_values[selected_option_form9] = 1
                        responseuseoffunds.user = selected_user
                        responseuseoffunds.Selected_Options = selected_options_list_form9
                        responseuseoffunds.Start_Up = option_values['Startup -Working']
                        responseuseoffunds.Growth_Scalabitlity = option_values['Growth Scalability']
                        responseuseoffunds.Marketing_and_Sales = option_values['Marketing & Sales']
                        responseuseoffunds.Cash_FLow_Capital = option_values['Cash Flow Capital']
                        responseuseoffunds.Human_Capital = option_values['Human Capital']
                        responseuseoffunds.Equipment = option_values['Equipment']
                        responseuseoffunds.Merger_and_Acquistions = option_values['Merger & Acquitions']
                        responseuseoffunds.Inventory = option_values['Inventory']
                        responseuseoffunds.Real_State = option_values['Real Estate']
                        responseuseoffunds.Other = option_values['Other']
                        responseuseoffunds.Unsure = option_values['Do not Know/Unsure/TBD']
                        responseuseoffunds.save()
                    
                    if form10.is_valid():
                        responserisk, created = EQuestions8.objects.get_or_create(user=selected_user)
                        selected_option1_form10 = form10.cleaned_data['selected_option1']
                        selected_option2_form10 = form10.cleaned_data['selected_option2']
                        option_values1 = {
                            'Low Risk Tolerance (Very Low Risk tolerance, expect to at least recoup principle)': 0,
                            'Medium Risk Tolerance (Can lose some or most of the funding)': 0,
                            'High Risk Tolerance (Can lose most or all of the funding)': 0,
                        }
                        option_values1[selected_option1_form10] = 1
                        option_values2 = {
                            'Low Cost of Capital (1-4%)': 0, 'Medium Cost of Capital (5-10%)': 0,
                            'High Cost of Capital (11-18%)': 0, 'Very High Cost of Capital (19%+)': 0,
                            'As long as the enterprise receives the net amount it needs, the cost is immaterial': 0,
                        }
                        option_values2[selected_option2_form10] = 1
                        responserisk.user = selected_user
                        responserisk.Selected_Option = selected_option1_form10
                        responserisk.Selected_Option2 = selected_option2_form10
                        responserisk.Low_Risk_Tolerance = option_values1['Low Risk Tolerance (Very Low Risk tolerance, expect to at least recoup principle)']
                        responserisk.Medium_Risk_Tolerance = option_values1['Medium Risk Tolerance (Can lose some or most of the funding)']
                        responserisk.High_Risk_Tolerance = option_values1['High Risk Tolerance (Can lose most or all of the funding)']
                        responserisk.Low_Cost_Capital = option_values2['Low Cost of Capital (1-4%)']
                        responserisk.Medium_Cost_Capital = option_values2['Medium Cost of Capital (5-10%)']
                        responserisk.High_Cost_Capital = option_values2['High Cost of Capital (11-18%)']
                        responserisk.Very_High_Cost_Capital = option_values2['Very High Cost of Capital (19%+)']
                        responserisk.Immaterial_Cost_Capital = option_values2['As long as the enterprise receives the net amount it needs, the cost is immaterial']
                        responserisk.save()
                    
                    if form11.is_valid():
                        responseupfrontcost, created = EQuestions.objects.get_or_create(user=selected_user)
                        selected_option_form11 = form11.cleaned_data['upfrontcost']
                        option_values = {
                            'Minimum $0 - Maximum $499': 0, 'Minimum $500 - Maximum $999': 0,
                            'Minimum $1000 - Maximum $2499': 0, 'Minimum $2500 - Maximum $4999': 0,
                            'Minimum $5000 - Maximum $9999': 0, 'Minimum $10000 - Maximum $24999': 0,
                            'Minimum $25000 -  Maximum $49999': 0, 'More than $50000+': 0,
                        }
                        option_values[selected_option_form11] = 1
                        responseupfrontcost.user = selected_user
                        responseupfrontcost.Selected_Option = selected_option_form11
                        responseupfrontcost.RC_zero_to_499 = option_values['Minimum $0 - Maximum $499']
                        responseupfrontcost.RC_500_to_999 = option_values['Minimum $500 - Maximum $999']
                        responseupfrontcost.RC_1000_to_2499 = option_values['Minimum $1000 - Maximum $2499']
                        responseupfrontcost.RC_2500_to_4999 = option_values['Minimum $2500 - Maximum $4999']
                        responseupfrontcost.RC_5000_to_9999 = option_values['Minimum $5000 - Maximum $9999']
                        responseupfrontcost.RC_10000_to_24999 = option_values['Minimum $10000 - Maximum $24999']
                        responseupfrontcost.RC_25000_to_49999 = option_values['Minimum $25000 -  Maximum $49999']
                        responseupfrontcost.RC_More_Than_50000 = option_values['More than $50000+']
                        responseupfrontcost.save()
                    
                    if form12.is_valid():
                        responsetiming, created = EQuestions.objects.get_or_create(user=selected_user)
                        selected_option_form12 = form12.cleaned_data['timming']
                        option_values = {
                            '1 Day to 1 Week': 0, '1 Week to 2 Weeks': 0, '2 Weeks to 4 Weeks': 0,
                            '1 Month to 2 Months': 0, '2 Months to 3 Months': 0, '3 Months to 6 Months': 0,
                            '6 Months to 12 Months': 0, 'More than 1 year': 0,
                        }
                        option_values[selected_option_form12] = 1
                        responsetiming.user = selected_user
                        responsetiming.Selected_Option2 = form12.cleaned_data['timming']
                        responsetiming.RT_1D_to_1W = option_values['1 Day to 1 Week']
                        responsetiming.RT_1W_to_2W = option_values['1 Week to 2 Weeks']
                        responsetiming.RT_2W_to_4W = option_values['2 Weeks to 4 Weeks']
                        responsetiming.RT_1M_to_2M = option_values['1 Month to 2 Months']
                        responsetiming.RT_2M_to_3M = option_values['2 Months to 3 Months']
                        responsetiming.RT_3M_to_6M = option_values['3 Months to 6 Months']
                        responsetiming.RT_6M_to_12M = option_values['6 Months to 12 Months']
                        responsetiming.RT_More_Than_a_Year = option_values['More than 1 year']
                        responsetiming.save()
                    
                    if form13.is_valid():
                        responsedocumentsprepared, created = DocumentsPrepared.objects.get_or_create(user=selected_user)
                        responsedocumentsprepared.user = selected_user
                        responsedocumentsprepared.summary_of_offering = form13.cleaned_data['summary_of_offering']
                        responsedocumentsprepared.financial_forecast = form13.cleaned_data['financial_forecast']
                        responsedocumentsprepared.lean_business_model = form13.cleaned_data['lean_business_model_canvas']
                        responsedocumentsprepared.presentation_deck = form13.cleaned_data['presentation_deck']
                        responsedocumentsprepared.leadership_overview = form13.cleaned_data['leadership_overview']
                        responsedocumentsprepared.exit_strategy = form13.cleaned_data['exit_strategy']
                        responsedocumentsprepared.offering_documents = form13.cleaned_data['offering_documents']
                        responsedocumentsprepared.ai_generated_deep_dive = form13.cleaned_data['ai_generated_deep_dive']
                        responsedocumentsprepared.virtual_data_room = form13.cleaned_data['virtual_data_room']
                        responsedocumentsprepared.save()
                    
                    if form14.is_valid():
                        responsecapitalranks, created = Letter_Response.objects.get_or_create(user=selected_user)
                        rankone = form14.cleaned_data['rankone']
                        ranktwo = form14.cleaned_data['ranktwo']
                        rankthree = form14.cleaned_data['rankthree']
                        rankfour = form14.cleaned_data['rankfour']
                        rankfive = form14.cleaned_data['rankfive']
                        status_manual = form14.cleaned_data['status']
                        top_6_capital = [rankone, ranktwo, rankthree, rankfour, rankfive, status_manual]
                        responsecapitalranks.top_6_name_output = top_6_capital
                        responsecapitalranks.top_6_name = top_6_capital
                        responsecapitalranks.cm1name = rankone
                        responsecapitalranks.cm2name = ranktwo
                        responsecapitalranks.cm3name = rankthree
                        responsecapitalranks.cm4name = rankfour
                        responsecapitalranks.cm5name = rankfive
                        responsecapitalranks.save()

                    if form15.is_valid():
                        responsereferral, created = ReferalResponse.objects.get_or_create(user=selected_user)
                        responsereferral.referral_source = form15.cleaned_data['referral_source']
                        responsereferral.referrer_name = form15.cleaned_data['referrer_name']
                        responsereferral.referral_other = form15.cleaned_data['referral_other']
                        responsereferral.save()
                    
                    if form16.is_valid():
                        responselending, created = LendingRequirements.objects.get_or_create(user=selected_user)
                        responselending.collateral_status = form16.cleaned_data['collateral_status']
                        responselending.credit_score = form16.cleaned_data['credit_score']
                        responselending.criminal_history = form16.cleaned_data['criminal_history']
                        responselending.save()
                    
                    # Redirect after successful unified form submission
                    if 'selected_user_id' in request.session:
                        del request.session['selected_user_id']
                    dashboard_url = reverse('master-review')
                    return HttpResponse(f"""Success!<a href='{dashboard_url}'> Back to Dashboard</a>""")

                except User.DoesNotExist:
                    del request.session['selected_user_id']
                    selected_user = None
        if selected_user:
            try:
                form2 = RegistrationFormOne(initial=initial_dataregistration_stage,prefix="form2") #from2=registrationfrom
            except:
                form2 = RegistrationFormOne(request.POST,prefix="form2")
            try:    
                form3 = EQuestions1Form(initial=initial_data_stage,prefix="form3") #form3=stageform
            except:
                form3 = EQuestions1Form(request.POST,prefix="form3")
            try:    
                form4 = EQuestions2Form(initial=initial_data_entity,prefix="form4") #form4=Entity
            except:
                form4 = EQuestions2Form(request.POST,prefix="form4")
            try:    
                form5 = EQuestions3Form(initial=initial_data_precapital,prefix="form5") #form5=precapital
            except:
                form5 =  EQuestions3Form(request.POST,prefix="form5")
            try:    
                form6 = EQuestions4Form(initial=initial_data_premarket,prefix="form6") #form6=premarket
            except:
                 form6 = EQuestions4Form(request.POST,prefix="form6")
            try:
                form7 = EQuestions5Form(initial=initial_data_plannedraise,prefix="form7") #form7=Plannedraise
            except:
                form7 = EQuestions5Form(request.POST,prefix="form7")
            try:    
                form8 = EQuestions6Form(initial=initial_data_rounds,prefix="form8") #form8=rounds of capital
            except:
                form8 = EQuestions6Form(request.POST,prefix="form8")
            try:    
                form9 = EQuestions7Form(initial=initial_data_useoffunds,prefix="form9") #form9 = use of funds
            except:
                form9 = EQuestions7Form(request.POST,prefix="form9")
            try:    
                form10 = EQuestions8Form(initial=initial_data_risk,prefix="form10") #form10 = riskassessment and capital cost
            except:
                form10 = EQuestions8Form(request.POST,prefix="form10")
            try:    
                form11 = EQuestionsForma(initial= initial_data_upfrontcost,prefix="form11") #form11 = Up Front Costs
            except:
                form11 = EQuestionsForma(request.POST,prefix="form11")
            try:    
                form12 = EQuestionsFormb(initial=initial_data_timing,prefix="form12") #form12 = Timing
            except:
                form12 = EQuestionsFormb(request.POST,prefix="form12")
            try:    
                form13 = DocumentsPreparedForm(initial=initial_data_documentsprepared,prefix="form13") #form13 = Documents prepared 
            except:
                form13 = DocumentsPreparedForm(request.POST,prefix="form13")
            try:
                form14 =manualCapitalTypeform(initial=initial_data_capitaltype,prefix="form14")
            except:
                form14 =manualCapitalTypeform(request.POST,prefix="form14")   
            try:
                form15 = ReferralResponseForm(initial=initial_data_referral, prefix="form15")
            except:
                form15 = ReferralResponseForm(request.POST,prefix="form15")
            try:
                form16 = LendingRequirementsForm(initial=initial_data_lending, prefix="form16")
            except:
                form16 = LendingRequirementsForm(request.POST,prefix="form16")                

        #responses = UserDetail.objects.filter(user=selected_user)
        letter = Match_Data.objects.filter(user=selected_user).first()
        if letter:
            letter_content = letter.html
    else:
        form = UserSelectionForm()
        if selected_user:
            try:
                responseregistration = UserDetail.objects.get(user=selected_user)
                initial_dataregistration_stage = {
                    'user':selected_user,
                    'First_Name':responseregistration.First_Name,
                    'Middle_Name': responseregistration.Middle_Name,
                    'Last_Name':responseregistration.Last_Name,
                    'Affiliation':responseregistration.Affiliation,
                    'User_Email':responseregistration.User_Email,
                    'Company_Website':responseregistration.Company_Website,
                    'Business_Adress': responseregistration.Business_Adress,
                    'Business_Phone':responseregistration.Business_Phone,
                    'Mobile_Phone':responseregistration.Mobile_Phone,
                    'Special_Programs':responseregistration.Special_Programs,
                }
                form2 = RegistrationFormOne(initial=initial_dataregistration_stage,prefix="form2")                           
            except UserDetail.DoesNotExist:
                responseregistration =UserDetail(user=selected_user)
                form2 = RegistrationFormOne(prefix="form2")
            try:    
                responsestage = EQuestions1.objects.get(user=selected_user)
                initial_data_stage = {
                    'user':selected_user,
                    'selected_option':responsestage.Selected_Option,
                }
                form3 = EQuestions1Form(initial=initial_data_stage,prefix="form3")
            except EQuestions1.DoesNotExist:    
                responsestage = EQuestions1(user=selected_user)
                form3 = EQuestions1Form(prefix="form3")
            try:
                responseentity = EQuestions2.objects.get(user=selected_user)
                initial_data_entity ={
                            'Business_Name':responseentity.Business_Name,
                            'selected_option':responseentity.Selected_Option,
                            'Registration_Region':responseentity.Registration_Region,
                }
                form4 = EQuestions2Form(initial=initial_data_entity,prefix="form4")
            except EQuestions2.DoesNotExist:    
                responseentity =EQuestions2(user=selected_user)
                form4 = EQuestions2Form(prefix="form4")
        
            try:
                responseprecapital = EQuestions3.objects.get(user=selected_user)
                initial_data_precapital={
                    'selected_option':responseprecapital.Selected_Option,
                }
                form5 = EQuestions3Form(initial=initial_data_precapital,prefix="form5")
            except EQuestions3.DoesNotExist:    
                responseprecapital = EQuestions3(user=selected_user)
                form5 = EQuestions3Form(prefix="form5")
            try:    
                responsepremarket = EQuestions4.objects.get(user=selected_user)
                initial_data_premarket = {
                    'Market':responsepremarket.Selected_Options,
                }
                form6 = EQuestions4Form(initial=initial_data_premarket,prefix="form6")
            except EQuestions4.DoesNotExist:    
                responsepremarket = EQuestions4(user=selected_user)
                form6 = EQuestions4Form(prefix="form6")
            try:                                     
                responseplannedraise = EQuestions5.objects.get(user=selected_user)
                initial_data_plannedraise ={
                    'selected_option':responseplannedraise.Selected_Option,
                }
                form7 = EQuestions5Form(initial=initial_data_plannedraise,prefix="form7")            
            except EQuestions5.DoesNotExist:    
                responseplannedraise = EQuestions5(user=selected_user)
                form7 = EQuestions5Form(prefix="form7")                
            try:    
                responserounds = EQuestions6.objects.get(user=selected_user)
                initial_data_rounds = {
                    'capital_market':responserounds.Selected_Options,
                    'selected_option':responserounds.Selected_Option
                }
                form8 = EQuestions6Form(initial=initial_data_rounds,prefix="form8")
            except EQuestions6.DoesNotExist:    
                responserounds = EQuestions6(user=selected_user)
                form8 = EQuestions6Form(prefix="form8")
        
            try:
                responseuseoffunds = EQuestions7.objects.get(user=selected_user)
                initial_data_useoffunds = {
                    'selected_uses':responseuseoffunds.Selected_Options,
                }
                form9 = EQuestions7Form(initial=initial_data_useoffunds,prefix="form9")
            except EQuestions7.DoesNotExist:    
                responseuseoffunds = EQuestions7(user=selected_user)
                form9 = EQuestions7Form(prefix="form9")
            try:                                                    
                responserisk = EQuestions8.objects.get(user=selected_user)
                initial_data_risk={
                    'selected_option1':responserisk.Selected_Option,
                    'selected_option2':responserisk.Selected_Option2,
                }
                form10 = EQuestions8Form(initial=initial_data_risk,prefix="form10")
            except EQuestions8.DoesNotExist:    
                responserisk = EQuestions8(user=selected_user)
                form10 = EQuestions8Form(prefix="form10")
            try:
                responseupfrontcost = EQuestions.objects.get(user=selected_user)
                initial_data_upfrontcost = {
                    'upfrontcost':responseupfrontcost.Selected_Option,
                }
                form11= EQuestionsForma(initial=initial_data_upfrontcost,prefix="form11")
            except EQuestions.DoesNotExist:    
                responseupfrontcost = EQuestions(user=selected_user)
                form11 = EQuestionsForma(prefix="form11")
            try:        
                responsetiming = EQuestions.objects.get(user=selected_user)
                initial_data_timing={
                    'timming':responsetiming.Selected_Option2,                    
                }
                form12 = EQuestionsFormb(initial=initial_data_timing,prefix="form12")
            except EQuestions.DoesNotExist:    
                responsetiming = EQuestions(user=selected_user)
                form12 = EQuestionsFormb(prefix="form12")
            try:
                responsedocumentsprepared = DocumentsPrepared.objects.get(user=selected_user)
                initial_data_documentsprepared = {
                    'summary_of_offering':responsedocumentsprepared.summary_of_offering,
                    'financial_forecast':responsedocumentsprepared.financial_forecast,
                    'lean_business_model_canvas':responsedocumentsprepared.lean_business_model,
                    'presentation_deck': responsedocumentsprepared.presentation_deck,
                    'leadership_overview': responsedocumentsprepared.leadership_overview,
                    'exit_strategy':responsedocumentsprepared.exit_strategy,
                    'offering_documents': responsedocumentsprepared.offering_documents,
                    'ai_generated_deep_dive':responsedocumentsprepared.ai_generated_deep_dive,
                    'virtual_data_room':responsedocumentsprepared.virtual_data_room
                }                 
                form13 = DocumentsPreparedForm(initial=initial_data_documentsprepared,prefix="form13")
            except DocumentsPrepared.DoesNotExist:    
                responsedocumentsprepared = DocumentsPrepared(user=selected_user)
                form13 = DocumentsPreparedForm(prefix="form13")
            
            try:
                responsereferral = ReferalResponse.objects.get(user=selected_user)
                initial_data_referral = {
                    'referral_source':responsereferral.referral_source,
                    'referrer_name':responsereferral.referrer_name,
                    'referral_other':responsereferral.referral_other,
                }
                form15 = ReferralResponseForm(initial=initial_data_referral, prefix="form15")
            except ReferalResponse.DoesNotExist:
                responsereferral = ReferalResponse(user=selected_user)
                form15 = ReferralResponseForm(prefix="form15")    
            
            try:
                responselending = LendingRequirements.objects.get(user=selected_user)
                initial_data_lending = {
                    'collateral_status':responselending.collateral_status,
                    'credit_score':responselending.credit_score,
                    'criminal_history':responselending.criminal_history,
                }
                form16 = LendingRequirementsForm(initial=initial_data_lending, prefix="form16")
            except LendingRequirements.DoesNotExist:
                responsereferral = LendingRequirements(user=selected_user)
                form16 =LendingRequirementsForm(prefix="form16")

            try:
                responsecapitalranks = Letter_Response.objects.get(user=selected_user)
                initial_data_capitaltype = {
                    'rankone' : responsecapitalranks.top_6_name_output[0],
                    'ranktwo' : responsecapitalranks.top_6_name_output[1],
                    'rankthree' : responsecapitalranks.top_6_name_output[2],
                    'rankfour' : responsecapitalranks.top_6_name_output[3],
                    'rankfive' : responsecapitalranks.top_6_name_output[4],
                    'status' : responsecapitalranks.top_6_name_output[5],
                }
            except IndexError:
                responsecapitalranks = Letter_Response.objects.get(user=selected_user)
                try:
                    rankone = responsecapitalranks.top_6_name_output[0]
                except:
                    rankone = 'Accelerator - Private (925)'
                try:
                    ranktwo = responsecapitalranks.top_6_name_output[1]
                except:
                    ranktwo = 'Accelerator - Private (925)'
                try:
                    rankthree = responsecapitalranks.top_6_name_output[2]
                except:
                    rankthree = 'Accelerator - Private (925)'
                try:
                    rankfour = responsecapitalranks.top_6_name_output[3]
                except:
                    rankfour = 'Accelerator - Private (925)'
                try:
                    rankfive = responsecapitalranks.top_6_name_output[4]
                except:
                    rankfive = 'Accelerator - Private (925)'                        
                initial_data_capitaltype = {
                    'rankone' :rankone,
                    'ranktwo' : ranktwo,
                    'rankthree' : rankthree,
                    'rankfour' : rankfour,
                    'rankfive' : rankfive,
                    'status' : False,               
                }
            except Letter_Response.DoesNotExist:
                responsecapitalranks = Letter_Response(user=selected_user)
                form14 = manualCapitalTypeform(prefix="form14")

    context = {
        'form': form,
        'form2':form2,
        'form3':form3,
        'form4':form4,
        'form5':form5,
        'form6':form6,
        'form7':form7,
        'form8':form8,
        'form9':form9,
        'form10':form10,
        'form11':form11,
        'form12':form12,
        'form13': form13,
        'form14':form14,
        'form15':form15,
        'form16':form16,
        'selected_user': selected_user, 
        'responses': responses,
        'stage':stage,
        'entity_name':entity_name,
        'entity_state':entity_state,
        'letter_content':letter_content,
    }
    return render(request, 'master_review.html', context)
