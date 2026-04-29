from django.shortcuts import render, redirect, get_object_or_404,HttpResponse

from .forms import EQuestionsForma,EQuestionsFormb,EQuestions1Form, EQuestions2Form,EQuestions3Form,EQuestions4Form,\
    EQuestions5Form,EQuestions6Form,EQuestions7Form,EQuestions8Form,EQuestions9Form, \
    EQuestions10Form,EQuestions11Form,EQuestions12Form,EQuestions13Form, EQuestions14Form,DocumentsPreparedForm,RatingForm, ReferralResponseForm,LendingRequirementsForm

from .models import EQuestions,EQuestions1, EQuestions2,EQuestions3,EQuestions4,EQuestions5,EQuestions6,\
    EQuestions7,EQuestions8, EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,\
    EQuestions14,DocumentsPrepared,PreRating, ReferalResponse, LendingRequirements

from registration.models import UserDetail
from django.contrib.auth.decorators import login_required


@login_required
def equestion_forma(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = EQuestions.objects.get(user=request.user)

        initial_data = {
            'upfrontcost':response.Selected_Option,
        }
    except EQuestions.DoesNotExist:
        response = EQuestions(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestionsForma(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['upfrontcost']

            # Create a dictionary to hold the values
            option_values = {
                'Minimum $0 - Maximum $499': 0,
                'Minimum $500 - Maximum $999': 0,
                'Minimum $1000 - Maximum $2499': 0,
                'Minimum $2500 - Maximum $4999': 0,
                'Minimum $5000 - Maximum $9999': 0,
                'Minimum $10000 - Maximum $24999': 0,
                'Minimum $25000 - Maximum $49999': 0,
                'More than $50000+':0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option = form.cleaned_data['upfrontcost'] # this is to retrieve data
            response.RC_zero_to_499 = option_values['Minimum $0 - Maximum $499']
            response.RC_500_to_999 = option_values['Minimum $500 - Maximum $999']
            response.RC_1000_to_2499=option_values['Minimum $1000 - Maximum $2499']
            response.RC_2500_to_4999=option_values['Minimum $2500 - Maximum $4999']
            response.RC_5000_to_9999=option_values['Minimum $5000 - Maximum $9999']
            response.RC_10000_to_24999=option_values['Minimum $10000 - Maximum $24999']
            response.RC_25000_to_49999=option_values['Minimum $25000 - Maximum $49999']
            response.RC_More_Than_50000 = option_values['More than $50000+']
            response.save()

            return redirect('equestionb')  # Redirect to a  another entreprise question3
    else:
        form = EQuestionsForma(initial=initial_data)

    context = {'form': form}
    return render(request, 'upfrontcost.html', context)

@login_required
def equestion_formb(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = EQuestions.objects.get(user=request.user)

        initial_data = {
            'timming':response.Selected_Option2,
        }
    except EQuestions.DoesNotExist:
        response = EQuestions(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestionsFormb(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['timming']

            # Create a dictionary to hold the values
            option_values = {
                '1 Day to 1 Week': 0,
                '1 Week to 2 Weeks': 0,
                '2 Weeks to 4 Weeks': 0,
                '1 Month to 2 Months': 0,
                '2 Months to 3 Months': 0,
                '3 Months to 6 Months': 0,
                '6 Months to 12 Months': 0,
                'More than 1 year':0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option2 = form.cleaned_data['timming'] # this is to retrieve data
            response.RT_1D_to_1W = option_values['1 Day to 1 Week']
            response.RT_1W_to_2W = option_values['1 Week to 2 Weeks']
            response.RT_2W_to_4W=option_values['2 Weeks to 4 Weeks']
            response.RT_1M_to_2M=option_values['1 Month to 2 Months']
            response.RT_2M_to_3M=option_values['2 Months to 3 Months']
            response.RT_3M_to_6M=option_values['3 Months to 6 Months']
            response.RT_6M_to_12M=option_values['6 Months to 12 Months']
            response.RT_More_Than_a_Year = option_values['More than 1 year']
            response.save()

            return redirect('documents')  # Redirect to a  another entreprise question3
    else:
        form = EQuestionsFormb(initial=initial_data)

    context = {'form': form}
    return render(request, 'timming.html', context)


@login_required
def equestion1_form(request):
    
    # Retrieve the existing survey response for the logged-in user
    try:
        response = EQuestions1.objects.get(user=request.user)

        initial_data = {
            'user':request.user,
            'selected_option':response.Selected_Option,
        }
    except EQuestions1.DoesNotExist:
        response = EQuestions1(user=request.user)
        initial_data = {}
        
    if request.method == 'POST':
        form = EQuestions1Form(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['selected_option']

            # Create a dictionary to hold the values
            option_values = {
                'Idea': 0,
                'Formation': 0,
                'Start Up': 0,
                'Growth': 0,
                'M & A': 0,
                'Preparing for Public': 0,
                'Distressed': 0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Idea=option_values['Idea']
            response.Formation=option_values['Formation']
            response.Start_Up=option_values['Start Up']
            response.Growth=option_values['Growth']
            response.M_And_A=option_values['M & A']
            response.Preparing_For_Public = option_values['Preparing for Public']
            response.Distressed = option_values['Distressed']
            response.Selected_Option = selected_option
            response.save()

            return redirect('equestion2')  # Redirect to a success page or another page
    else:
        form = EQuestions1Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'stage.html', context)



@login_required
def equestion2_form(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = EQuestions2.objects.get(user=request.user)

        initial_data = {
            'user':request.user,
            'Business_Name':response.Business_Name,
            'selected_option':response.Selected_Option,
            'Registration_Region':response.Registration_Region,
        }
    except EQuestions2.DoesNotExist:
        response = EQuestions2(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions2Form(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['selected_option']

            # Create a dictionary to hold the values
            option_values = {
                'None (To be Determined)': 0,
                'Sole Proprietorship': 0,
                'LLC': 0,
                'LP': 0,
                'GP': 0,
                'S Corporation': 0,
                'C Corp': 0,
                'Other':0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option = form.cleaned_data['selected_option'] # this is to retrieve data
            response.Business_Name = form.cleaned_data['Business_Name']
            response.Registration_Region = form.cleaned_data['Registration_Region']
            response.No_Business=option_values['None (To be Determined)']
            response.Sole_Proprietorship=option_values['Sole Proprietorship']
            response.LLC=option_values['LLC']
            response.LP=option_values['LP']
            response.GP=option_values['GP']
            response.S_Corporation = option_values['S Corporation']
            response.C_Corp = option_values['C Corp']
            response.Other = option_values['Other']
            response.save()

            return redirect('equestion3')  # Redirect to a  another entreprise question3
    else:
        form = EQuestions2Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'entity.html', context)
  
@login_required  
def equestion3_form(request):
    
    try:
        response = EQuestions3.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'selected_option':response.Selected_Option,
        }
    except EQuestions3.DoesNotExist:
        response = EQuestions3(user=request.user)
        initial_data ={}

    if request.method == 'POST':
        form = EQuestions3Form(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['selected_option']

            # Create a dictionary to hold the values
            option_values = {
                'Less than $25,000': 0,
                '$26,000 to $100,000': 0,
                '$101,000 to $250,000': 0,
                '$251,000 to $500,000': 0,
                '$501,000 to $1,000,000': 0,
                '$1,000,001 to $2,000,000': 0,
                '$2,000,001 to $5,000,000': 0,
                '$5,000,001 to $10,000,000': 0,
                'More than $10,000,000': 0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option = selected_option
            response.Less_25k = option_values['Less than $25,000']
            response.More_25K_Less_100k = option_values['$26,000 to $100,000']
            response.More_100k_Less_250K = option_values['$101,000 to $250,000']
            response.More_250k_Less_500K = option_values['$251,000 to $500,000']
            response.More_500K_Less_1M = option_values['$501,000 to $1,000,000']
            response.More_1M_Less_2M = option_values['$1,000,001 to $2,000,000']
            response.More_2M_Less_5M = option_values['$2,000,001 to $5,000,000']
            response.More_5M_Less_10M = option_values['$5,000,001 to $10,000,000']
            response.More_10M = option_values['More than $10,000,000']
            response.save()

            return redirect('equestion4')  # Redirect to a success page or another page
    else:
        form = EQuestions3Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'precapital.html', context)

@login_required
def equestion4_form(request):
    try:
        response = EQuestions4.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'Market':response.Selected_Options,
        }

    except EQuestions4.DoesNotExist:
        response = EQuestions4(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions4Form(request.POST)
        if form.is_valid():
            selected_options_list = form.cleaned_data['Market']

            # Create a dictionary to hold the values
            option_values = {
                'Accelerator': 0,
                'Bonds': 0,
                'Commercial Banks': 0,
                'Cryptocurrency': 0,
                'EB5 Immigration': 0,
                'Enterprise Zones': 0,
                'Factoring': 0,
                'Grants': 0,
                'Hedge Funds': 0,
                'Incubator': 0,
                'Investment Banking': 0,
                'Other (Owner Equity)': 0,
                'Private Debt (Officer Loans to Startup)': 0,
                'Private Equity Securities': 0,
                'Public Offering': 0,
                'Real State': 0,
                'Royalty Financing': 0,
                'Small Business Administration (SBA)': 0,
                'Venture Capital': 0,
                'Unsure/Do not Know': 0
            }
            for selected_option in selected_options_list:
                option_values[selected_option] =1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Options = selected_options_list
            response.Accelerator = option_values['Accelerator']
            response.Bonds = option_values['Bonds']
            response.Comercial_Banking = option_values['Commercial Banks']
            response.Cryptocurrency = option_values['Cryptocurrency']
            response.EB5_Immigration = option_values['EB5 Immigration']
            response.Enterprise_Zones = option_values['Enterprise Zones']
            response.Factoring = option_values['Factoring']
            response.Grants = option_values['Grants']
            response.Hedge_Funds = option_values['Hedge Funds']
            response.Incubator = option_values['Incubator']
            response.Investment_Banking = option_values['Investment Banking']
            response.Other_Owner_Equity =option_values['Other (Owner Equity)']
            response.Private_Debt = option_values['Private Debt (Officer Loans to Startup)']
            response.Private_Equity = option_values['Private Equity Securities']
            response.Public_Offereing =option_values['Public Offering']
            response.Real_Estate = option_values['Real State']
            response.Royalty_Financing = option_values['Royalty Financing']
            response.Small_Business_Administration = option_values['Small Business Administration (SBA)']
            response.Venture_Capital = option_values['Venture Capital']
            response.Unsure = option_values['Unsure/Do not Know']
            response.save()

            return redirect('equestion5')  # Redirect to a success page or another page
    else:
        form = EQuestions4Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'premarketcapitaltype.html', context)

@login_required
def equestion5_form(request):
    # Retrieve from database
    try:
        response = EQuestions5.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'selected_option':response.Selected_Option,
        }

    except EQuestions5.DoesNotExist:
        response = EQuestions5(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions5Form(request.POST)
        if form.is_valid():
            selected_option = form.cleaned_data['selected_option']

            # Create a dictionary to hold the values
            option_values = {
                'Less than $25,000': 0,
                '$25,000 to $100,000': 0,
                '$100,000 to $249,999': 0,
                '$250,000 to $499,999': 0,
                '$500,000 to $999,999': 0,
                '$1,000,000 to $1,349,999': 0,
                '$1,350,000 to $1,999,999': 0,
                '$2,000,000 to $4,999,999': 0,
                '$5,000,000 to $9,999,999': 0,
                '$10,000,000 to $19,999,999': 0,
                'More Than $20 Million': 0,
                'Unsure/Do not Know/TBD': 0,
            }

            # Set the selected option to 1
            option_values[selected_option] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option = selected_option
            response.Less_25k = option_values['Less than $25,000']
            response.More_25K_Less_100k = option_values['$25,000 to $100,000']
            response.More_100k_Less_250K = option_values['$100,000 to $249,999']
            response.More_250k_Less_500K = option_values['$250,000 to $499,999']
            response.More_500K_Less_1M = option_values['$500,000 to $999,999']
            response.More_1M_Less_1_35M = option_values['$1,000,000 to $1,349,999']
            response.More_1_35M_Less_2M = option_values['$1,350,000 to $1,999,999']
            response.More_2M_Less_5M = option_values['$2,000,000 to $4,999,999']
            response.More_5M_Less_10M = option_values['$5,000,000 to $9,999,999']
            response.More_10M_Less_20M = option_values['$10,000,000 to $19,999,999']
            response.More_20M = option_values['More Than $20 Million']
            response.Unsure = option_values['Unsure/Do not Know/TBD']
            response.save()

            return redirect('equestion6')  # Redirect to a success page or another page
    else:
        form = EQuestions5Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'plannedraise.html', context)

@login_required
def equestion6_form(request):
    # Retrieve from database
    try:
        response = EQuestions6.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'capital_market':response.Selected_Options,
            'selected_option':response.Selected_Option
        }

    except EQuestions6.DoesNotExist:
        response = EQuestions6(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions6Form(request.POST)
        if form.is_valid():
            selected_options_list = form.cleaned_data['capital_market']
            selected_option_2 = form.cleaned_data['selected_option']

            # Create a dictionary to hold the values for first question in form
            option_values = {
                'Founders Round': 0,
                'Pre-Seed': 0,
                'Seed': 0,
                'Series A': 0,
                'Series B': 0,
                'Series C': 0,
                'Pre-IPO': 0,
                'IPO': 0,
                'Unsure/Do not Know/TBD': 0,
            }
            #Set the seleceted options to 1
            for selected_option in selected_options_list:
                option_values[selected_option] =1
            
            # Create a dictionary to hold the values for first question in form
            option_values2 = {
                'One': 0,
                'Two': 0,
                'TBD': 0,
            }
            # Set the selected option to 1 for the second question of form
            option_values2[selected_option_2] = 1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Options = selected_options_list
            response.Selected_Option =selected_option_2
            response.Founders_Round = option_values['Founders Round']
            response.Pre_Seed = option_values['Pre-Seed']
            response.Seed = option_values['Seed']
            response.Series_A = option_values['Series A']
            response.Series_B = option_values['Series B']
            response.Series_C = option_values['Series C']
            response.Pre_Ipo = option_values['Pre-IPO']
            response.Ipo = option_values['IPO']
            response.Unsure = option_values['Unsure/Do not Know/TBD']

                # for second question option_values2
            response.One = option_values2['One']
            response.Two = option_values2['Two']
            response.TBD =option_values2['TBD']
            response.save()

            return redirect('equestion7')  # Redirect to a success page or another page
    else:
        form = EQuestions6Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'rounds.html', context)

@login_required
def equestion7_form(request):
    # Retrieve from database
    try:
        response = EQuestions7.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'selected_uses':response.Selected_Options,
        }

    except EQuestions7.DoesNotExist:
        response = EQuestions7(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions7Form(request.POST)
        if form.is_valid():
            selected_options_list = form.cleaned_data['selected_uses']

            # Create a dictionary to hold the values
            option_values = {
                'Startup/Working': 0,
                'Growth Scalability': 0,
                'Marketing & Sales': 0,
                'Cash Flow Capital': 0,
                'Human Capital': 0,
                'Equipment': 0,
                'Merger & Acquitions': 0,
                'Inventory': 0,
                'Real Estate': 0,
                'Other': 0,
                'Do not Know/Unsure/TBD': 0,
            }
            #Set the seleceted options to 1
            for selected_option in selected_options_list:
                option_values[selected_option] =1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Options =selected_options_list
            response.Start_Up = option_values['Startup/Working']
            response.Growth_Scalabitlity = option_values['Growth Scalability']
            response.Marketing_and_Sales = option_values['Marketing & Sales']
            response.Cash_FLow_Capital = option_values['Cash Flow Capital']
            response.Human_Capital = option_values['Human Capital']
            response.Equipment = option_values['Equipment']
            response.Merger_and_Acquistions = option_values['Merger & Acquitions']
            response.Inventory = option_values['Inventory']
            response.Real_State = option_values['Real Estate']
            response.Other = option_values['Other']
            response.Unsure = option_values['Do not Know/Unsure/TBD']
            response.save()

            return redirect('equestion8')  # Redirect to a success page or another page
    else:
        form = EQuestions7Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'use.html', context)

@login_required
def equestion8_form(request):
    # Retrieve from database
    try:
        response = EQuestions8.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'selected_option1':response.Selected_Option,
            'selected_option2':response.Selected_Option2,
        }

    except EQuestions8.DoesNotExist:
        response = EQuestions8(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions8Form(request.POST)
        if form.is_valid():
            selected_option1 = form.cleaned_data['selected_option1']
            selected_option2 = form.cleaned_data['selected_option2']

            # Create a dictionary to hold the values for first Risk question
            option_values1 = {
                'Low Risk Tolerance (Very Low Risk tolerance, expect to at least recoup principle)': 0,
                'Medium Risk Tolerance (Can lose some or most of the funding)': 0,
                'High Risk Tolerance (Can lose most or all of the funding)': 0,
            }
        
            option_values1[selected_option1] =1
            
            # Create a dictionary to hold the values for second Risk question (Cost of capital)
            option_values2 = {
                'Low Cost of Capital (1-4%)': 0,
                'Medium Cost of Capital (5-10%)': 0,
                'High Cost of Capital (11-18%)': 0,
                'Very High Cost of Capital (19%+)': 0,
                'As long as the enterprise receives the net amount it needs, the cost is immaterial': 0,
            }

            option_values2[selected_option2] =1

            # Create the UserDetail instance with the correct values
            response.user = request.user
            response.Selected_Option = selected_option1
            response.Selected_Option2 = selected_option2
            #Updating First Question's Column in Model 
            response.Low_Risk_Tolerance = option_values1['Low Risk Tolerance (Very Low Risk tolerance, expect to at least recoup principle)']
            response.Medium_Risk_Tolerance = option_values1['Medium Risk Tolerance (Can lose some or most of the funding)']
            response.High_Risk_Tolerance = option_values1['High Risk Tolerance (Can lose most or all of the funding)']
            #Updating Second Question's Column in Model
            response.Low_Cost_Capital = option_values2['Low Cost of Capital (1-4%)']
            response.Medium_Cost_Capital = option_values2['Medium Cost of Capital (5-10%)']
            response.High_Cost_Capital = option_values2['High Cost of Capital (11-18%)']
            response.Very_High_Cost_Capital = option_values2['Very High Cost of Capital (19%+)']
            response.Immaterial_Cost_Capital = option_values2['As long as the enterprise receives the net amount it needs, the cost is immaterial']
            response.save()

            return redirect('equestion')  # Redirect to a success page or another page
    else:
        form = EQuestions8Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'risk.html', context)

@login_required
def documentsprepared_form(request):
    # Retrieve from database
    try:
        response = DocumentsPrepared.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'summary_of_offering':response.summary_of_offering,
            'financial_forecast':response.financial_forecast,
            'lean_business_model_canvas':response.lean_business_model,
            'presentation_deck': response.presentation_deck,
            'leadership_overview': response.leadership_overview,
            'exit_strategy':response.exit_strategy,
            'offering_documents': response.offering_documents,
            'ai_generated_deep_dive':response.ai_generated_deep_dive,
            'virtual_data_room':response.virtual_data_room
        }

    except DocumentsPrepared.DoesNotExist:
        response = DocumentsPrepared(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = DocumentsPreparedForm(request.POST)
        if form.is_valid():
            summary_of_offering = form.cleaned_data['summary_of_offering']
            financial_forecast = form.cleaned_data['financial_forecast']
            lean_business_model_canvas = form.cleaned_data['lean_business_model_canvas']
            presentation_deck = form.cleaned_data['presentation_deck']
            leadership_overview = form.cleaned_data['leadership_overview']
            exit_strategy = form.cleaned_data['exit_strategy']
            offering_documents = form.cleaned_data['offering_documents']
            ai_generated_deep_dive = form.cleaned_data['ai_generated_deep_dive']
            virtual_data_room = form.cleaned_data['virtual_data_room']


            response.user=request.user
            response.summary_of_offering = summary_of_offering
            response.financial_forecast=financial_forecast
            response.lean_business_model=lean_business_model_canvas
            response.presentation_deck=presentation_deck
            response.leadership_overview=leadership_overview
            response.exit_strategy=exit_strategy
            response.offering_documents=offering_documents
            response.ai_generated_deep_dive=ai_generated_deep_dive
            response.virtual_data_room = virtual_data_room
            response.save()
            
            return redirect('pre-ratings')  # Redirect to a success page or another page
    else:
        form = DocumentsPreparedForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'documents.html', context)

@login_required
def preRating(request):
    # Retrieve from database
    try:
        response = PreRating.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'financial_model_forecast_pro_forma':response.preratings['Financial Model, forecast, pro forma'],
            'finfire_report_capital_type':response.preratings['Finfire Report - Capital Type'],
            'due_diligence_checklist_documents':response.preratings['Due Diligence Checklist Documents'],
            'historical_financials': response.preratings['Historical Financials (P & L, BS, CF, Aging)'],
            'tax_returns': response.preratings['Tax Returns (Up to 2 years, if applicable)'],
            'business_valuation_equity_only':response.preratings['Business Valuation (Equity only)'],
            'cap_table_use_of_funds_and_capitalization_plan': response.preratings['Cap Table, Use of Funds, & Capitalization Plan'],
            'business_model_canvas':response.preratings['Business Model Canvas'],
            'offering_documents_rating':response.preratings['Offering Documents'],
            'presentation_video_ai_deep_dive':response.preratings['Presentation Video (From the AI Deep Dive)'],
            'application_if_applicable':response.preratings['Application (If Applicable)'],
            'resume_of_founder_ceo_primary_leader':response.preratings['Resume of Founder/CEO Primary Leader'],
            'presentation_deck_rating':response.preratings['Presentation Deck'],
            'executive_summary_including_exit_strategy':response.preratings['Executive Summary Including Exit Strategy'],
            'quality_assurance_checklist_including_ai':response.preratings['Quality Assurance Checklist (Including AI)'],
            'capital_match_list_generated':response.preratings['Capital Match List Generated'],
            'investor_marketing_campaign':response.preratings['Investor Marketing Campaign'],
            'investor_relations':response.preratings['Investor Relations'],
            'progress_reports':response.preratings['Progress Reports'],
        }

    except PreRating.DoesNotExist:
        response = PreRating(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            financial_model_forecast_pro_forma = form.cleaned_data['financial_model_forecast_pro_forma']
            finfire_report_capital_type = form.cleaned_data['finfire_report_capital_type']
            due_diligence_checklist_documents = form.cleaned_data['due_diligence_checklist_documents']
            historical_financials = form.cleaned_data['historical_financials']
            tax_returns = form.cleaned_data['tax_returns']
            business_valuation_equity_only = form.cleaned_data['business_valuation_equity_only']
            cap_table_use_of_funds_and_capitalization_plan = form.cleaned_data['cap_table_use_of_funds_and_capitalization_plan']
            business_model_canvas = form.cleaned_data['business_model_canvas']
            offering_documents_rating = form.cleaned_data['offering_documents_rating']
            presentation_video_ai_deep_dive = form.cleaned_data['presentation_video_ai_deep_dive']
            application_if_applicable = form.cleaned_data['application_if_applicable']
            resume_of_founder_ceo_primary_leader = form.cleaned_data['resume_of_founder_ceo_primary_leader']
            presentation_deck_rating = form.cleaned_data['presentation_deck_rating']
            executive_summary_including_exit_strategy = form.cleaned_data['executive_summary_including_exit_strategy']
            quality_assurance_checklist_including_ai = form.cleaned_data['quality_assurance_checklist_including_ai']
            capital_match_list_generated = form.cleaned_data['capital_match_list_generated']
            investor_marketing_campaign = form.cleaned_data['investor_marketing_campaign']
            investor_relations = form.cleaned_data['investor_relations']
            progress_reports = form.cleaned_data['progress_reports']


            response.user=request.user
            response.preratings = {
                'Financial Model, forecast, pro forma' : financial_model_forecast_pro_forma,
                'Finfire Report - Capital Type' : finfire_report_capital_type,
                'Due Diligence Checklist Documents' : due_diligence_checklist_documents,
                'Historical Financials (P & L, BS, CF, Aging)' : historical_financials,
                'Tax Returns (Up to 2 years, if applicable)' : tax_returns,
                'Business Valuation (Equity only)' : business_valuation_equity_only,
                'Cap Table, Use of Funds, & Capitalization Plan' : cap_table_use_of_funds_and_capitalization_plan,
                'Business Model Canvas' : business_model_canvas,
                'Offering Documents' : offering_documents_rating,
                'Presentation Video (From the AI Deep Dive)' : presentation_video_ai_deep_dive,
                'Application (If Applicable)' : application_if_applicable,
                'Resume of Founder/CEO Primary Leader' : resume_of_founder_ceo_primary_leader ,
                'Presentation Deck' : presentation_deck_rating,
                'Executive Summary Including Exit Strategy' : executive_summary_including_exit_strategy,
                'Quality Assurance Checklist (Including AI)' : quality_assurance_checklist_including_ai,
                'Capital Match List Generated' : capital_match_list_generated,
                'Investor Marketing Campaign' : investor_marketing_campaign,
                'Investor Relations' : investor_relations,
                'Progress Reports' :  progress_reports, 
            }
            response.save()
            
            return redirect('referral')  # Redirect to a success page or another page
    else:
        form = RatingForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'preratings.html', context)

@login_required
def referral_response_view(request):
    try:
        instance = ReferalResponse.objects.get(user=request.user)
        initial_data = {
            'referral_source': instance.referral_source,
            'referrer_name': instance.referrer_name,
            'referral_other': instance.referral_other,
        }
    except ReferalResponse.DoesNotExist:
        instance = None
        initial_data = {}

    if request.method == 'POST':
        form = ReferralResponseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('lending-requiremetns')
    else:
        form = ReferralResponseForm(initial=initial_data, instance=instance)

    context = {'form': form}
    return render(request, 'referral_response.html', context)

@login_required
def lendig_requirements_views(request):
    # Retrieve from database
    try:
        response = LendingRequirements.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'collateral_status':response.collateral_status,
            'credit_score':response.credit_score,
            'criminal_history':response.criminal_history,
        }

    except LendingRequirements.DoesNotExist:
        response = LendingRequirements(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = LendingRequirementsForm(request.POST,instance=response)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("match")
    else:
        form = LendingRequirementsForm(initial=initial_data,instance=response)

    context = {'form': form}
    return render(request, 'documents.html', context)

@login_required
def equestion9_form(request):
    # Retrieve from database
    try:
        response = EQuestions9.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'onepagetearsheet':response.One_Page_Tear_Sheet,
            'elevetorpitch':response.Elevator_Peach,
            'businesplan':response.Business_Plan,
            'duediligenceci': response.DD_Corporate_Identity,
            'dueilgencet': response.DD_Technology,
            'executivesummary':response.Executive_Summary,
            'virtualportal': response.Virtual_Portal,
        }

    except EQuestions9.DoesNotExist:
        response = EQuestions9(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions9Form(request.POST)
        if form.is_valid():
            onepagetearsheet = form.cleaned_data['onepagetearsheet']
            elevetorpitch = form.cleaned_data['elevetorpitch']
            businesplan = form.cleaned_data['businesplan']
            duediligenceci = form.cleaned_data['duediligenceci']
            dueilgencet = form.cleaned_data['dueilgencet']
            executivesummary = form.cleaned_data['executivesummary']
            virtualportal = form.cleaned_data['virtualportal']

            response.user=request.user
            response.One_Page_Tear_Sheet=onepagetearsheet
            response.Elevator_Peach=elevetorpitch
            response.Business_Plan=businesplan
            response.DD_Corporate_Identity=duediligenceci
            response.DD_Technology=dueilgencet
            response.Executive_Summary=executivesummary
            response.Virtual_Portal=virtualportal
            response.save()
            
            return redirect('equestion10')  # Redirect to a success page or another page
    else:
        form = EQuestions9Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'DDQS.html', context)

@login_required
def equestion10_form(request):
    # Retrieve from database
    try:
        response = EQuestions10.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'assumption_worksheets':response.Assumption_Worksheets,
            'capital_structure_plan':response.Capital_Structure_Plan,
            'capitalization_table':response.Capitalization_Table,
            'financial_modeling_FC': response.Financial_Modeling_FC,
            'financial_modeling_RC': response.Financial_Modeling_RC,
            'financial_modeling_SP':response.Financial_Modeling_SP,
            'sources_uses': response.Sources_Uses,
            'valuation_spreadsheets':response.Valuation_Spreadsheets,
            'valuation_OLFVW':response.Valuation_OLFVW,
        }

    except EQuestions10.DoesNotExist:
        response = EQuestions10(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions10Form(request.POST)
        if form.is_valid():
            AssumptionWorksheets = form.cleaned_data['assumption_worksheets']
            CapitalStructurePlan = form.cleaned_data['capital_structure_plan']
            CapitalizationTable = form.cleaned_data['capitalization_table']
            FinancialModelingFC = form.cleaned_data['financial_modeling_FC']
            FinancialModelingRC = form.cleaned_data['financial_modeling_RC']
            FinancialModelingSP = form.cleaned_data['financial_modeling_SP']
            SourcesUses = form.cleaned_data['sources_uses']
            ValuationSpreadsheets = form.cleaned_data['valuation_spreadsheets']
            ValuationOLFVW = form.cleaned_data['valuation_OLFVW']

            response.user=request.user
            response.Assumption_Worksheets=AssumptionWorksheets
            response.Capital_Structure_Plan=CapitalStructurePlan
            response.Capitalization_Table=CapitalizationTable
            response.Financial_Modeling_FC=FinancialModelingFC
            response.Financial_Modeling_RC=FinancialModelingRC
            response.Financial_Modeling_SP=FinancialModelingSP
            response.Sources_Uses=SourcesUses
            response.Valuation_Spreadsheets= ValuationSpreadsheets
            response.Valuation_OLFVW = ValuationOLFVW
            response.save()
            
            return redirect('equestion11')  # Redirect to a success page or another page
    else:
        form = EQuestions10Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'DDQS.html', context)

@login_required
def equestion11_form(request):
    # Retrieve from database
    try:
        response = EQuestions11.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'business_model_canvas':response.Business_Model_Canvas,
            'company_website_V3':response.Company_Website_V3,
            'website_marketing':response.Website_Marketing,
            'due_diligence_CA': response.Due_Diligence_CA,
            'marketing': response.Marketing,
            'marketing_plan_budget':response.Marketing_Plan_Budget,
            'marketing_research_report': response.Marketing_Research_Report,
            'presentation_deck':response.Presentation_Deck,
            'strategic_tactical_plan':response.Strategic_Tactical_Plan,
        }

    except EQuestions11.DoesNotExist:
        response = EQuestions11(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions11Form(request.POST)
        if form.is_valid():
            BusinessModelCanvas = form.cleaned_data['business_model_canvas']
            CompanyWebsiteV3 = form.cleaned_data['company_website_V3']
            WebsiteMarketing = form.cleaned_data['website_marketing']
            DueDiligenceCA = form.cleaned_data['due_diligence_CA']
            Marketing = form.cleaned_data['marketing']
            MarketingPlanBudget = form.cleaned_data['marketing_plan_budget']
            MarketingResearchReport = form.cleaned_data['marketing_research_report']
            PresentationDeck = form.cleaned_data['presentation_deck']
            StrategicTacticalPlan = form.cleaned_data['strategic_tactical_plan']

            response.user=request.user
            response.Business_Model_Canvas=BusinessModelCanvas
            response.Company_Website_V3=CompanyWebsiteV3
            response.Website_Marketing=WebsiteMarketing
            response.Due_Diligence_CA=DueDiligenceCA
            response.Marketing=Marketing
            response.Marketing_Plan_Budget=MarketingPlanBudget
            response.Marketing_Research_Report=MarketingResearchReport
            response.Presentation_Deck= PresentationDeck
            response.Strategic_Tactical_Plan = StrategicTacticalPlan
            response.save()
            
            return redirect('equestion12')  # Redirect to a success page or another page
    else:
        form = EQuestions11Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'DDQS.html', context)

@login_required
def equestion12_form(request):
    # Retrieve from database
    try:
        response = EQuestions12.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'leadership':response.Leadership,
            'management_experience':response.Management_Experience,
            'consultant_advisor':response.Consultant_Advisor,
            'staff': response.Staff,
            'culture': response.Culture,
        }

    except EQuestions12.DoesNotExist:
        response = EQuestions12(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions12Form(request.POST)
        if form.is_valid():
            LeadershipV = form.cleaned_data['leadership'] #for a single word variable V is added at last 
            ManagementExperience = form.cleaned_data['management_experience']
            ConsultantAdvisor = form.cleaned_data['consultant_advisor']
            StaffV = form.cleaned_data['staff'] #for a single word variable V is added at last
            CultureV = form.cleaned_data['culture'] #for a single word variable V is added at last

            response.user=request.user
            response.Leadership=LeadershipV
            response.Management_Experience=ManagementExperience
            response.Consultant_Advisor=ConsultantAdvisor
            response.Staff=StaffV
            response.Culture=CultureV
            response.save()

            
            return redirect('equestion13')  # Redirect to a success page or another page
    else:
        form = EQuestions12Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'DDQS.html', context)

@login_required
def equestion13_form(request):
    # Retrieve from database
    try:
        response = EQuestions13.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'capital_marketing_plan':response.Capital_Marketing_Plan,
            'capital_offering_documents':response.Capital_Offering_Documents,
            'due_diligence_IP':response.Due_Diligence_IP,
            'due_diligence_LE': response.Due_Diligence_LE,
            'due_diligence_RA': response.Due_Diligence_RA,
            'exit_strategy':response.Exit_Strategy,
        }

    except EQuestions13.DoesNotExist:
        response = EQuestions13(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions13Form(request.POST)
        if form.is_valid():
            CapitalMarketingPlan= form.cleaned_data['capital_marketing_plan'] #for a single word variable V is added at last 
            CapitalOfferingDocuments = form.cleaned_data['capital_offering_documents']
            DueDiligenceIP = form.cleaned_data['due_diligence_IP']
            DueDiligenceLE = form.cleaned_data['due_diligence_LE'] #for a single word variable V is added at last
            DueDiligenceRA = form.cleaned_data['due_diligence_RA'] #for a single word variable V is added at last
            ExitStrategy = form.cleaned_data['exit_strategy']

            response.user=request.user
            response.Capital_Marketing_Plan=CapitalMarketingPlan
            response.Capital_Offering_Documents=CapitalOfferingDocuments
            response.Due_Diligence_IP=DueDiligenceIP
            response.Due_Diligence_LE=DueDiligenceLE
            response.Due_Diligence_RA=DueDiligenceRA
            response.Exit_Strategy = ExitStrategy
            response.save()
            
            return redirect('equestion14')  # Redirect to a success page or another page
    else:
        form = EQuestions13Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'DDQS.html', context)

@login_required
def equestion14_form(request):
    # Retrieve from database
    try:
        response = EQuestions14.objects.get(user=request.user)
        initial_data = {
            'user':response.user,
            'required_intermediaries_region':response.Required_Intermediaries_Region,
            'industry_types':response.Industry_Type,
        }

    except EQuestions14.DoesNotExist:
        response = EQuestions14(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = EQuestions14Form(request.POST)
        if form.is_valid():
                
            response.user=request.user
            response.Required_Intermediaries_Region=form.cleaned_data['required_intermediaries_region']
            response.Industry_Type=form.cleaned_data['industry_types']
            response.save()

            
            return redirect('match')  # Redirect to a success page or another page
    else:
        form = EQuestions14Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'forms.html', context)



