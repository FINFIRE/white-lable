from .forms import ScoreForm
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared,LendingRequirements
from Matching_Algorithm.models import allCapitalMatchValues
from .models import CapitalType,capitalTypes
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CapitalType
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.safestring import mark_safe 
from django.urls import reverse
from django.contrib.auth.models import User

allowed_user = ['tonyfinfire','rominadmin']

@login_required
@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
def capital_viewt(request):
    #time.sleep(5)  # Add 10 second delay
    try:
        collateral_status_check =LendingRequirements.objects.get(user=request.user).collateral_status
        credit_score_check = LendingRequirements.objects.get(user=request.user).credit_score 
        criminal_history_check = LendingRequirements.objects.get(user=request.user).criminal_history        
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
    except:
        survey_url = reverse('registration_form_view')
        return HttpResponse(f"Complete <a href=\"{survey_url}\">Start your matching Survey</a> section inorder to use this section because this section calculates the percentage match for each capital market/capital type for your answers in the survey.")
    # Get all local variables after they have been assigned
    all_variables = locals()
    # Create a list to store the variable values
    values_list = [value for key, value in all_variables.items() if key != 'request'][3:]    
#    C_TYPES =[
#        ('Accelerator', 'Accelerator'),
#        ('Bonds','Bonds'),
#        ('Bootstrapped','Bootstrapped'),
#        ('Commercial Banking','Commercial Banking'),
#        ('Cryptocurrency','Cryptocurrency'),
#        ('Factoring','Factoring'),
#        ('Grants','Grants'),
#        ('Hedge Funds','Hedge Funds'),
#        ('Incubator','Incubator'),
#        ('Investment Banking','Investment Banking'),
#        ('Private Debt','Private Debt'),
#        ('Private Equity Securities','Private Equity Securities'),
#        ('Royalty Financing','Royalty Financing'),
#        ('Small Business Administration (SBA)','Small Business Administration (SBA)'),
#        ('Third Party Corporate Credit','Third Party Corporate Credit'),
#        ('Tokenization','Tokenization'),
#        ('Venture Capital','Venture Capital'),
#    ]
    C_TYPES = [
        ("Owner Debt - Cash Savings", "Owner Debt - Cash Savings"),
        ("Accelerator University", "Accelerator University"),
        ("Incubator - University", "Incubator - University"),
        ("Accelerator - Public", "Accelerator - Public"),
        ("Incubator - Public", "Incubator - Public"),
        ("Small Business Administration (SBA) - SBA Veteran", "Small Business Administration (SBA) - SBA Veteran"),
        ("Royalty Financing - Top Line Revenue", "Royalty Financing - Top Line Revenue"),
        ("Grants - Municipalities", "Grants - Municipalities"),
        ("Owner Debt - Whole Life Insurance", "Owner Debt - Whole Life Insurance"),
        ("Private Equity Securities - SAFE  Simple Agreement Future Equity", "Private Equity Securities - SAFE  Simple Agreement Future Equity"),
        ("Grants - Government", "Grants - Government"),
        ("Owner Debt - Home Equity", "Owner Debt - Home Equity"),
        ("Small Business Administration (SBA) - SBA Express", "Small Business Administration (SBA) - SBA Express"),
        ("Accelerator - Private", "Accelerator - Private"),
        ("Commercial Banking - Equipment Loan", "Commercial Banking - Equipment Loan"),
        ("Commercial Banking - Standby Letter of Credit (SBLC)", "Commercial Banking - Standby Letter of Credit (SBLC)"),
        ("Grants - Education Grants", "Grants - Education Grants"),
        ("Grants - State Agencies", "Grants - State Agencies"),
        ("Incubator - Private", "Incubator - Private"),
        ("Small Business Administration (SBA) - SBIC", "Small Business Administration (SBA) - SBIC"),
        ("Commercial Banking - Line of Credit", "Commercial Banking - Line of Credit"),
        ("Commercial Banking - Real Estate Loan", "Commercial Banking - Real Estate Loan"),
        ("Government Incentives Opportunity Zone Tax Credit Fund", "Government Incentives Opportunity Zone Tax Credit Fund"),
        ("Owner Debt - Retirement (401K) SDI", "Owner Debt - Retirement (401K) SDI"),
        ("Private Equity Securities - Family and Friends", "Private Equity Securities - Family and Friends"),
        ("Small Business Administration (SBA) - SBA 504B", "Small Business Administration (SBA) - SBA 504B"),
        ("Small Business Administration (SBA) - SBA 7A", "Small Business Administration (SBA) - SBA 7A"),
        ("Commercial Banking - Commercial Bank Loan", "Commercial Banking - Commercial Bank Loan"),
        ("Government Incentives - Enterprise Zones", "Government Incentives - Enterprise Zones"),
        ("Commercial Banking - Acquisition Loan", "Commercial Banking - Acquisition Loan"),
        ("Grants - Research Grants", "Grants - Research Grants"),
        ("Owner Debt - Personal Credit Cards", "Owner Debt - Personal Credit Cards"),
        ("Small Business Administration (SBA) - CDC/SBDC", "Small Business Administration (SBA) - CDC/SBDC"),
        ("Commercial Banking - Asset Based Lending", "Commercial Banking - Asset Based Lending"),
        ("Owner Debt - Personal Resources or Loans", "Owner Debt - Personal Resources or Loans"),
        ("Private Debt - Promissory Note", "Private Debt - Promissory Note"),
        ("Commercial Banking - Collateralized Debt", "Commercial Banking - Collateralized Debt"),
        ("Private Debt - Real Estate Loan", "Private Debt - Real Estate Loan"),
        ("Private Equity Securities - Family Offices", "Private Equity Securities - Family Offices"),
        ("Private Debt - Asset Based Lending", "Private Debt - Asset Based Lending"),
        ("Private Debt - Bridge Financing", "Private Debt - Bridge Financing"),
        ("Private Debt - Private Debt", "Private Debt - Private Debt"),
        ("Alternative - Apps (i.e. Cabbage)", "Alternative - Apps (i.e. Cabbage)"),
        ("Commercial Banking - Credit Card", "Commercial Banking - Credit Card"),
        ("Digital Currency - Investment via Crypto Wallet", "Digital Currency - Investment via Crypto Wallet"),
        ("Private Equity Securities - Angel Investors", "Private Equity Securities - Angel Investors"),
        ("Private Equity Securities - Convertible Note", "Private Equity Securities - Convertible Note"),
        ("Grants - Corporate Grants", "Grants - Corporate Grants"),
        ("Private Debt - Acquisition Loan", "Private Debt - Acquisition Loan"),
        ("Private Debt - Hard Money Loan", "Private Debt - Hard Money Loan"),
        ("Alternative - Corporate Credit (Third Party)", "Alternative - Corporate Credit (Third Party)"),
        ("Factoring - Accounts Receivable Loans", "Factoring - Accounts Receivable Loans"),
        ("Factoring - Merchant Account Advances", "Factoring - Merchant Account Advances"),
        ("Bonds - Government Backed", "Bonds - Government Backed"),
        ("Bonds - High Yield Junk", "Bonds - High Yield Junk"),
        ("Bonds - Mortgage Backed", "Bonds - Mortgage Backed"),
        ("Factoring - Purchase Order Loan", "Factoring - Purchase Order Loan"),
        ("Private Debt - Collateralized Debt", "Private Debt - Collateralized Debt"),
        ("Factoring - Invoice Factoring", "Factoring - Invoice Factoring"),
        ("Government Incentives - Gold Star", "Government Incentives - Gold Star"),
        ("Hedge Funds - Public", "Hedge Funds - Public"),
        ("Investment Banking - Mezzanine Financing", "Investment Banking - Mezzanine Financing"),
        ("Private Equity Securities - Regulation D 506(b)", "Private Equity Securities - Regulation D 506(b)"),
        ("Digital Currency - Stable Coins (DAO) - Blockchain", "Digital Currency - Stable Coins (DAO) - Blockchain"),
        ("Bonds - Foreign", "Bonds - Foreign"),
        ("Private Equity Securities - Regulation D 506(c)", "Private Equity Securities - Regulation D 506(c)"),
        ("Private Equity Securities - Rule 144", "Private Equity Securities - Rule 144"),
        ("Alternative - High Yield Business Consumer Loan", "Alternative - High Yield Business Consumer Loan"),
        ("Investment Banking - Investment Banker Debt", "Investment Banking - Investment Banker Debt"),
        ("Private Equity Securities - Regulation D 505", "Private Equity Securities - Regulation D 505"),
        ("Private Equity Securities - Sophisticated Individuals", "Private Equity Securities - Sophisticated Individuals"),
        ("Bonds - Investment Grade", "Bonds - Investment Grade"),
        ("Hedge Funds - Private", "Hedge Funds - Private"),
        ("Private Equity Securities - Regulation D 504", "Private Equity Securities - Regulation D 504"),
        ("Digital Currency - Cryptocurrency", "Digital Currency - Cryptocurrency"),
        ("Government Incentives - EB5 Immigration", "Government Incentives - EB5 Immigration"),
        ("Investment Banking - Broker Syndication", "Investment Banking - Broker Syndication"),
        ("Private Equity Securities - Accredited Investors", "Private Equity Securities - Accredited Investors"),
        ("Venture Capital - Short-Term Bridge Financing", "Venture Capital - Short-Term Bridge Financing"),
        ("Digital Currency - Tokenization", "Digital Currency - Tokenization"),
        ("Private Equity Securities - Private Placement Memorandum", "Private Equity Securities - Private Placement Memorandum"),
        ("Private Equity Securities - Regulation A", "Private Equity Securities - Regulation A"),
        ("Private Equity Securities - Regulation A Plus", "Private Equity Securities - Regulation A Plus"),
        ("Private Equity Securities - Regulation CF Tittle III", "Private Equity Securities - Regulation CF Tittle III"),
        ("Digital Currency - Initial Coin Offering", "Digital Currency - Initial Coin Offering"),
        ("Digital Currency - Initial Exchange Offering", "Digital Currency - Initial Exchange Offering"),
        ("Investment Banking - Broker Dealer Representation", "Investment Banking - Broker Dealer Representation"),
        ("Investment Banking - Equity Sale", "Investment Banking - Equity Sale"),
        ("Private Equity Securities - Broker Dealers", "Private Equity Securities - Broker Dealers"),
        ("Public Securities - Derivatives", "Public Securities - Derivatives"),
        ("Public Securities - SPAC - Special Purpose Acquisition Company", "Public Securities - SPAC - Special Purpose Acquisition Company"),
        ("Venture Capital - Mezzanine Financing", "Venture Capital - Mezzanine Financing"),
        ("Public Securities - Market Maker", "Public Securities - Market Maker"),
        ("Public Securities - Money Market Instruments", "Public Securities - Money Market Instruments"),
        ("Public Securities - PIPE Private Investment in Public Entity", "Public Securities - PIPE Private Investment in Public Entity"),
        ("Venture Capital - Long Term Debt", "Venture Capital - Long Term Debt"),
        ("Public Securities - Initial Public Offering (IPO)", "Public Securities - Initial Public Offering (IPO)"),
        ("Public Securities - OTC Over the Counter", "Public Securities - OTC Over the Counter"),
        ("Venture Capital - Mergers and Acquisitions Financing", "Venture Capital - Mergers and Acquisitions Financing"),
        ("Venture Capital - Equity Sale", "Venture Capital - Equity Sale"),
    ]
    ctype_name = None  # Initialize ctype to avoid UnboundLocalError    
    
    if request.method == "POST":
        ctype_name = request.POST.get('capital-dropdown')
        matrix_weights = request.POST.getlist('matrix_weight')
        counter_list = request.POST.getlist('counter')
        counters = sum([int(a) for a in request.POST.getlist('counter') if a.isdigit()])
        percentages = request.POST.getlist('percentage')
        points = request.POST.getlist('points')

        # Retrieve or create the associated CapitalType
        capital_type = CapitalType.objects.filter(namec__name=ctype_name).first()

        if capital_type:
            capital_type.matrix_weights = matrix_weights
            capital_type.counter = counters
            capital_type.counterlist = counter_list
            capital_type.status = True  # Or use your counter logic
            capital_type.save()
            return render(request,'added.html')
        
    else:  # Handle GET requests
        ctype_name = request.GET.get('capital-dropdown')
        if ctype_name:
            print(f"ctype_name: {ctype_name}")  # Debugging
            capital_type = CapitalType.objects.filter(namec__name=ctype_name).first()
            print(f"capital_type: {capital_type}") 
            matrix_weights = capital_type.matrix_weights if capital_type else [0] * 126
            counter_list = capital_type.counterlist if capital_type else [0] * 126
            status = capital_type.status if capital_type else 0
        else:
            matrix_weights = [0] * 126
            counter_list = [0] * 126
            print("Not working")
            status = False


        context = {
            'scores': values_list,
            'matrix_weights': matrix_weights,
            'counter':counter_list,
            'range_list': list(range(0, 126)),
            'clist': C_TYPES,
            'status': status,
            'options': [
                "Idea", "Formation", "Start-Up", "Growth", "M & A", "Preparing for Public", "Distressed", "None (To be Determined)",
                "Sole Proprietorship", "LLC", "LP", "GP", "S Corporation", "C Corp", "Other", "Less Than $25,000", "$26,000 to $100,000",
                "$101,000 to $250,000", "$251,000 to $500,000", "$501,000 to $1,000,000", "$1,000,001 to $2,000,000", "$2,000,001 to $5,000,000",
                "$5,000,001 to $10,000,000", "More Than $10,000,000", "Accelerator", "Bonds", "Commercial Banking", "Cryptocurrency", "EB5 Immigration",
                "Enterprise Zones", "Factoring", "Grants", "Hedge Funds", "Incubator", "Investment Banking", "Other", "Private Debt", "Private Equity Securities",
                "Public Offering", "Real Estate", "Royalty Financing", "Small Business Administration (SBA)", "Venture Capital", "Unsure/Don't Know",
                "Less Than $25,000", "$26,000 to $99,000", "$100,000 to $249,999", "$250,000 to $499,999", "$500,000 to $999,999",
                "$1,000,000 to $1,349,999", "$1,350,000 to $1,999,999", "$2,000,000 to $4,999,999", "$5,000,000 to $9,999,999", "$10,000,000 to $19,999,999",
                "More Than $20 Million", "Unsure/Don't Know/TBD", "Founder's Round", "Pre-Seed", "Seed", 'Series "A"', 'Series "B"', 'Series "C"', "Pre-IPO", "IPO",
                "Unsure/Don't Know/TBD", "One", "Two", "TBD", "Startup - Working", "Growth Scalability", "Marketing & Sales", "Cash Flow Capital", "Human Capital",
                "Equipment", "Mergers & Acquisitions", "Inventory", "Real Estate", "Other", "Don't Know/Unsure/TBD", "Low Risk Tolerance", "Medium Risk Tolerance",
                "High Risk Tolerance", "Low Cost of Capital (1-4%)", "Medium Cost of Capital (5-10%)", "High Cost of Capital (11-18%)", "Very High Cost of Capital (19%+)",
                "The cost is immaterial", "$0 Minimum up to $499", "$500 Minimum up to $999", "$1,000 Minimum up to $2,499", "$2,500 Minimum up to $4,999", "$5,000 Minimum up to $9,999",
                "$10,000 Minimum up to $24,999", "$25,000 Minimum up to $49,999", "More than $50,000", "1 Day to 1 Week", "1 week to 2 weeks", "2 weeks to 4 weeks", "1 month to 2 months",
                "2 months to 3 months", "3 months to 6 months", "6 months to 12 months", "More than 1 year", "Summary of Offering", "Financials", "Lean Business Model Canvas",
                "Presentation Deck", "Leadership Overview", "Exit strategy", "Offering Documents", "AI Generated Deep Dive", "Virtual Data Room", "Not Applicable","Yes", "No","Unknown","<580",">620",">680",">720",">760",
                "None","Misdemeanor","Felony","Fraud","Securities Violation"
            ]            
        }
        return render(request, 'capital_templatet.html', context)


@login_required
@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
@require_GET
def fetch_capital_data(request):
    # Retrieve the selected capital from the query parameters
    selected_capital = request.GET.get('capital')
    
    if not selected_capital:
        return JsonResponse({'error': 'Capital not provided'}, status=400)

    try:
        # Get the `capitalTypes` instance with the matching name
        capital_type_instance = capitalTypes.objects.get(name=selected_capital)
        
        # Query the `CapitalType` model using the `namec` foreign key
        capital_data = CapitalType.objects.get(namec=capital_type_instance)

        # Prepare response data
        response_data = {
            'matrix_weights': capital_data.matrix_weights,  # JSONField
            'counterlist':capital_data.counterlist, # JSONField
            'status':capital_data.status, # Boolean
        }

        return JsonResponse(response_data)

    except capitalTypes.DoesNotExist:
        return JsonResponse({'error': 'Capital type not found'}, status=404)
    except CapitalType.DoesNotExist:
        return JsonResponse({'error': 'Capital data not found'}, status=404)

@login_required
@user_passes_test(lambda u: u.username in allowed_user or u.is_staff)
def algorithmInsightDashboard(request):
    # Get all users who have capital match values
    users = User.objects.filter(allcapitalmatchvalues__isnull=False).distinct()
    
    # Get selected user from request
    selected_user_id = request.GET.get('user')
    selected_user = None
    user_data = None
    
    if selected_user_id:
        try:
            selected_user = User.objects.get(id=selected_user_id)
            user_data = allCapitalMatchValues.objects.get(user=selected_user)
        except (User.DoesNotExist, allCapitalMatchValues.DoesNotExist):
            pass

    # Generate HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" href="/static/img/b.png" type="image/x-icon">
        <title>Algorithm Insight Dashboard</title>
        <style>
            /* Global Styles */
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f4f7fa;
                margin: 0;
                padding: 0;
                color: #333;
            }
            
            center {
                padding: 20px;
            }

            /* Navigation Block Styles */
            .nav-block {
                background-color: #ffffff;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }

            .nav-logo {
                margin-bottom: 10px;
            }

            .nav-links {
                display: flex;
                gap: 20px;
                margin-top: 10px;
            }

            .nav-links a {
                padding: 8px 15px;
                background-color: #0077b6;
                color: white;
                border-radius: 5px;
                transition: background-color 0.3s ease;
                text-decoration: none;
            }

            .nav-links a:hover {
                background-color: #005f88;
            }

            /* Dashboard Styles */
            .container {
                max-width: 1200px;
                margin: 40px auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            
            .header {
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 2px solid #e8f0fe;
            }
            
            h1 {
                color: #0077b6;
                font-size: 28px;
                margin: 0;
                padding: 0;
            }
            
            .user-select-container {
                display: flex;
                justify-content: center;
                margin: 30px 0;
            }
            
            .user-select {
                padding: 12px 20px;
                width: 100%;
                max-width: 400px;
                border: 2px solid #dadce0;
                border-radius: 8px;
                font-size: 16px;
                color: #202124;
                background-color: white;
                transition: all 0.3s ease;
            }
            
            .user-select:focus {
                outline: none;
                border-color: #0077b6;
                box-shadow: 0 0 0 2px #e8f0fe;
            }
            
            .data-table {
                width: 100%;
                border-collapse: separate;
                border-spacing: 0;
                margin-top: 30px;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }
            
            .data-table th {
                background-color: #0077b6;
                color: white;
                padding: 16px;
                text-align: left;
                font-weight: 500;
            }
            
            .data-table td {
                padding: 14px 16px;
                border-bottom: 1px solid #dadce0;
            }
            
            .data-table tr:last-child td {
                border-bottom: none;
            }
            
            .data-table tr:hover {
                background-color: #e8f0fe;
            }
            
            .value {
                font-weight: 600;
                color: #0077b6;
            }
            
            .no-data {
                text-align: center;
                padding: 40px;
                color: #5f6368;
                background-color: #e8f0fe;
                border-radius: 8px;
                margin-top: 20px;
            }
            
            .no-data p {
                margin: 0;
                font-size: 16px;
            }
            
            .percentage-bar {
                height: 8px;
                background-color: #e8f0fe;
                border-radius: 4px;
                margin-top: 4px;
                overflow: hidden;
            }
            
            .percentage-bar-fill {
                height: 100%;
                background-color: #0077b6;
                border-radius: 4px;
                transition: width 0.3s ease;
            }
            
            .capital-type {
                font-weight: 500;
                color: #202124;
            }
            
            @media (max-width: 768px) {
                .container {
                    margin: 20px;
                    padding: 20px;
                }
                
                .data-table {
                    display: block;
                    overflow-x: auto;
                }
            }
        </style>
    </head>
    <body>
        <center>
            <div class="nav-block">
                <div class="nav-logo">
                    <a href="/"><img src="/static/img/b.png"></a>
                </div>
                <div class="nav-links">
                    <a href="javascript:history.back()">Go Back</a>
                    <a href="/">Home</a>
                </div>
            </div>
            
            <div class="container">
                <div class="header">
                    <h1>Algorithm Insight Dashboard</h1>
                </div>
                
                <div class="user-select-container">
                    <form method="get">
                        <select name="user" class="user-select" onchange="this.form.submit()">
                            <option value="">Select a user</option>
    """

    # Add user options to dropdown
    for user in users:
        selected = 'selected' if selected_user and user.id == selected_user.id else ''
        html_content += f"""
                            <option value="{user.id}" {selected}>{user.username}</option>
        """

    html_content += """
                        </select>
                    </form>
                </div>
    """

    if user_data and user_data.percentage:
        html_content += """
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Capital Type</th>
                            <th>Match Percentage</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        # Sort the percentage data by value in descending order
        sorted_data = sorted(user_data.percentage.items(), key=lambda x: x[1], reverse=True)
        
        for capital_type, percentage in sorted_data:
            html_content += f"""
                        <tr>
                            <td class="capital-type">{capital_type}</td>
                            <td>
                                <div class="value">{percentage:.2f}%</div>
                                <div class="percentage-bar">
                                    <div class="percentage-bar-fill" style="width: {percentage}%"></div>
                                </div>
                            </td>
                        </tr>
            """

        html_content += """
                    </tbody>
                </table>
        """
    else:
        html_content += """
                <div class="no-data">
                    <p>No data available for the selected user</p>
                </div>
        """

    html_content += """
            </div>
        </center>
    </body>
    </html>
    """

    return HttpResponse(html_content)
