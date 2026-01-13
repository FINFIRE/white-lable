from registration.models import UserDetail, UserDetail2
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,\
EQuestions14,DocumentsPrepared,ReferalResponse,PreRating
from iquestions.models import IQuestions1,IQuestions2
from CM_Market.models import VQuestion1
from connections.models import Match_Data,pay_load_string
from Matching_Algorithm.models import Letter_Response,Purchases
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.fields import CharField, EmailField,IntegerField

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


#For Contact in Front end
class UserDetailSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='Last_Name')
    companyAffiliation = serializers.ListField(child=serializers.CharField(), required=True, source='Affiliation')  # Use actual model field name
    email = serializers.EmailField(required=True, source='User_Email')
    companyWebsite = serializers.CharField(source='Company_Website')
    primaryBusinessAddress = serializers.CharField(source='Business_Adress') 
    businessPhone = serializers.CharField(source='Business_Phone')
    mobilePhone = serializers.CharField(source='Mobile_Phone')
    specialPrograms = serializers.ListField(child=serializers.CharField(), required=True, source='Special_Programs')  # Use actual model field

    class Meta:
        model = UserDetail
        fields = [
            'display_name',
            'companyAffiliation',
            'email',
            'companyWebsite',
            'primaryBusinessAddress',
            'businessPhone',
            'mobilePhone',
            'specialPrograms'
        ]

# For Account in Front end
class UserDetail2Serializer(serializers.ModelSerializer):
    primaryAppUse = serializers.ListField(
        child=serializers.CharField(max_length=200),source='Primary_Purpose'
    )

    #Accouunt_Type & Billing_Option not mapped yet in front end
    class Meta:
        model = UserDetail2
        fields = ['primaryAppUse']

class EQuestionsSerializer(serializers.ModelSerializer):
    rangeofCost = serializers.CharField(max_length=200,source='Selected_Option')
    timing = serializers.CharField(max_length=200,source='Selected_Option2')
    class Meta:
        model = EQuestions
        fields = [
            'rangeofCost',
            'timing',
        ]

#For Stage in front end
class EQuestions1Serializer(serializers.ModelSerializer):
    stageofCompany = serializers.CharField(source='Selected_Option')

    class Meta:
        model = EQuestions1
        fields = [
            'stageofCompany',
        ]

#For Entity in front end
class EQuestions2Serializer(serializers.ModelSerializer):
    entityType = serializers.CharField(source='Selected_Option')
    entityName = serializers.CharField(source='Business_Name')
    entityStateofRegistration = serializers.CharField(source='Registration_Region')
    class Meta:
        model = EQuestions2
        fields = [
            'entityType',
            'entityName',
            'entityStateofRegistration',
        ]

#For Pre-Capital in front end
class EQuestions3Serializer(serializers.ModelSerializer):
    preCapitalRaise = serializers.CharField(source='Selected_Option')
    class Meta:
        model = EQuestions3
        fields = [
            'preCapitalRaise'
        ]

# For Pre-Market in front end
class EQuestions4Serializer(serializers.ModelSerializer):
    capitalPreMarkets = serializers.ListField(child=serializers.CharField(max_length=200),source='Selected_Options')
    class Meta:
        model = EQuestions4

        fields = [
            'capitalPreMarkets'
        ]

# For Planned Raise in front end 
class EQuestions5Serializer(serializers.ModelSerializer):
    plannedRaise = serializers.CharField(max_length=200,source='Selected_Option')
                
    class Meta:
        model = EQuestions5 
        fields = [
            'plannedRaise'
        ]

#For Rounds in front end 
class EQuestions6Serializer(serializers.ModelSerializer):
    currentRounds = serializers.ListField(child=serializers.CharField(max_length=200),source='Selected_Options')
    howManyRounds = serializers.CharField(max_length=200,source='Selected_Option')
    class Meta:
        model = EQuestions6    
        fields = [
            'currentRounds',
            'howManyRounds'
        ]

#For use of funds in front end
class EQuestions7Serializer(serializers.ModelSerializer):
    fundsUse = serializers.ListField(child=serializers.CharField(max_length=200),source='Selected_Options')
    class Meta:
        model = EQuestions7 
        fields = [
            'fundsUse'
        ]
        
# For Risk Assesment in front end
class EQuestions8Serializer(serializers.ModelSerializer):
    riskToleranceInvestor = serializers.CharField(max_length=200,source='Selected_Option')
    riskToleranceFounder = serializers.CharField(max_length=200,source='Selected_Option2')
    class Meta:
        model = EQuestions8
        fields = [
            'riskToleranceInvestor',
            'riskToleranceFounder',
        ]

#UP-Front Cost
class DocumentsPreparedSerializer(serializers.ModelSerializer):
    summaryofOffering = serializers.BooleanField(source='summary_of_offering')
    financialForecast = serializers.BooleanField(source='financial_forecast')
    leanBusinessModelCanvas = serializers.BooleanField(source='lean_business_model')
    presentationDeck = serializers.BooleanField(source='presentation_deck')
    leadershipOverview = serializers.BooleanField(source='leadership_overview')
    exitStrategy = serializers.BooleanField(source='exit_strategy')
    offeringDocuments = serializers.BooleanField(source='offering_documents')
    aiGeneratedDeepDive = serializers.BooleanField(source='ai_generated_deep_dive')
    virtualDataroom = serializers.BooleanField(source='virtual_data_room')

    class Meta:
        model = DocumentsPrepared
        fields = [
            'summaryofOffering',
            'financialForecast',
            'leanBusinessModelCanvas',
            'presentationDeck',
            'leadershipOverview',
            'exitStrategy',
            'offeringDocuments',
            'aiGeneratedDeepDive',
            'virtualDataroom',
        ]


#UP-Front Timming



# For Documents Prepared in front end
class EQuestions9Serializer(serializers.ModelSerializer):
    onePageTearSheet = serializers.CharField(max_length=200,source='One_Page_Tear_Sheet')
    elevatorPitch = serializers.CharField(max_length=200,source='Elevator_Peach')
    businessPlan = serializers.CharField(max_length=200,source='Business_Plan')
    corporateIdentityDueDiligence = serializers.CharField(max_length=200,source='DD_Corporate_Identity')
    technologyDueDiligence = serializers.CharField(max_length=200,source='DD_Technology')
    executiveSummary = serializers.CharField(max_length=200,source='Executive_Summary')
    virtualPortal = serializers.CharField(max_length=200,source='Virtual_Portal')
    class Meta:
        model = EQuestions9
        fields = [
            'onePageTearSheet',
            'elevatorPitch',
            'businessPlan',
            'corporateIdentityDueDiligence',
            'technologyDueDiligence',
            'executiveSummary',
            'virtualPortal'
        ]

#for Financials prepared in front end
class EQuestions10Serializer(serializers.ModelSerializer):
    assumptionsWorksheets = serializers.CharField(max_length=200,source='Assumption_Worksheets')
    capitalSourceStructure = serializers.CharField(max_length=200,source='Capital_Structure_Plan')
    capitalizationTable = serializers.CharField(max_length=200,source='Capitalization_Table')
    financialModelingFixedCosts = serializers.CharField(max_length=200,source='Financial_Modeling_FC')
    financialModelingRevenuesCosts = serializers.CharField(max_length=200,source='Financial_Modeling_RC')
    financialModelingSummaryPage = serializers.CharField(max_length=200,source='Financial_Modeling_SP')
    sourcesUses = serializers.CharField(max_length=200,source='Sources_Uses')
    valuationSpreadsheets = serializers.CharField(max_length=200,source='Valuation_Spreadsheets')
    valuationLetterFinal = serializers.CharField(max_length=200,source='Valuation_OLFVW')

    class Meta:
        model = EQuestions10
        fields = [
            'assumptionsWorksheets',
            'capitalSourceStructure',
            'capitalizationTable',
            'financialModelingFixedCosts',
            'financialModelingRevenuesCosts',
            'financialModelingSummaryPage',
            'sourcesUses',
            'valuationSpreadsheets',
            'valuationLetterFinal'
        ]

# For Marketing & Presentation Materials in front end
class EQuestions11Serializer(serializers.ModelSerializer):
    businessModelCanvas = serializers.CharField(max_length=200,source='Business_Model_Canvas')
    companyWeb3 = serializers.CharField(max_length=200,source='Business_Model_Canvas')
    #websiteMarketing = serializers.CharField(max_length=200,source='Website_Marketing')
    competitiveAnalysis = serializers.CharField(max_length=200,source='Due_Diligence_CA')
    marketing = serializers.CharField(max_length=200,source='Marketing')
    marketingPlanBudget = serializers.CharField(max_length=200,source='Marketing_Plan_Budget')
    marketResearchReport = serializers.CharField(max_length=200,source='Marketing_Research_Report')
    presentationDeck = serializers.CharField(max_length=200,source='Presentation_Deck')
    strategicTacticalPlan = serializers.CharField(max_length=200,source='Presentation_Deck')

    class Meta:
        model = EQuestions11
        fields = [
            'businessModelCanvas',
            'companyWeb3',
            #'websiteMarketing',
            'competitiveAnalysis',
            'marketing',
            'marketingPlanBudget',
            'marketResearchReport',
            'presentationDeck',
            'strategicTacticalPlan'
        ]

#For People & Culture in front end
class EQuestions12Serializer(serializers.ModelSerializer):
    leadership = serializers.CharField(max_length=200,source='Leadership')
    managementExperience = serializers.CharField(max_length=200,source='Management_Experience')
    consultantsAdvisors = serializers.CharField(max_length=200,source='Consultant_Advisor')
    staff = serializers.CharField(max_length=200,source='Staff')
    culture = serializers.CharField(max_length=200,source='Culture')

    class Meta:
        model = EQuestions12
        fields = [
            'leadership',
            'managementExperience',
            'consultantsAdvisors',
            'staff',
            'culture'
        ]
#For Legal, Offering & Risk in front end
class EQuestions13Serializer(serializers.ModelSerializer):
    capitalMarketPlan = serializers.CharField(max_length=200,source='Capital_Marketing_Plan')
    capitalOfferingDocuments = serializers.CharField(max_length=200,source='Capital_Offering_Documents')
    intellectualPropertyDueDiligence = serializers.CharField(max_length=200,source='Due_Diligence_IP')
    legalDueDiligence = serializers.CharField(max_length=200,source='Due_Diligence_LE')
    riskAssessmentDueDiligence = serializers.CharField(max_length=200,source='Due_Diligence_RA')
    exitStrategy = serializers.CharField(max_length=200,source='Exit_Strategy')

    class Meta:
        model = EQuestions13
        fields = [
            'capitalMarketPlan',
            'capitalOfferingDocuments',
            'intellectualPropertyDueDiligence',
            'legalDueDiligence',
            'riskAssessmentDueDiligence',
            'exitStrategy'
        ]

class EQuestions14Serializer(serializers.ModelSerializer):
    naicsCode = serializers.CharField(max_length=200,source='Industry_Type')
    class Meta:
        model = EQuestions14
        fields = [
            #'Required_Intermediaries_Region',
            'naicsCode'
        ]

class IQuestions1Serializer(serializers.ModelSerializer):
    class Meta:
        model = IQuestions1
        Prefered_CM = serializers.ListField(
        child=serializers.CharField(max_length=200)
        )        
        Specialized_Industry = serializers.ListField(
        child=serializers.CharField(max_length=200)
        )
        Regions_Served = serializers.ListField(
        child=serializers.CharField(max_length=200)
        )
        Selected_Options = serializers.ListField(
        child=serializers.CharField(max_length=200)
        )                 
        fields = [
            'First_Name',
            'Last_Name',
            'Company_Name',
            'Primary_Phone',
            'Secondary_Phone',
            'Alternate_Phone',
            'Email',
            'Adress',
            'City',
            'State',
            "Zip_Code",
            'I_Type',
            'Prefered_CM',
            'Specialized_Industry',
            'Regions_Served',
            'Selected_Options',
            #'Technical_Writer',
            #'Content_Creator',
            #'Business_Consultant',
            #'Marketing_Analyst',
            #'Business_Plan_Writer',
            #'Business_Attorney',
            #'Researcher',
            #'Subject_Matter_Expert',
            #'Business_Analyst',
            #'Data_Entry',
            #'Financial_Analyst',
            #'Accountant',
            #'CPA',
            #'Financial_Modeler',
            #'Valuation_Analyst',
            #'Banker',
            #'Web_Developer',
            #'Marketing_Consultant',
            #'Transfer_Agency',
            #'Graphic_Designer',
            #'Hr_Due_Diligence',
            #'Management_Consultant',
            #'Hr_Consultant',
            #'Culture_Subject_Matter_Expert',
            #'Broker_Agency',
            #'Platform',
            #'Securities_Attorney',
            #'Paralegal',
            #'Intelectual_Property_Attorney',
            #'Legal_Assistant',
            #'Risk_Analyst',
            #'Underwritter'
        ]

class IQuestions2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IQuestions2
        fields = ['Type', 'Explanation', 'Rate']

class VQuestion1Serializer(serializers.ModelSerializer):
    class Meta:
        model = VQuestion1
        Email = serializers.EmailField(required=True)
        fields = ['First_Name', 'Last_Name', 'Company_Name', 'Primary_Phone', 'Secondary_Phone', 
                  'Alternate_Phone', 'Email', 'Adress', 'City', 'State', 'Zip_Code', 'CM_Type']

class MatchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match_Data
        fields = ['user', 'html']

class MatchDataEfficientSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(max_length=200,source='lastname')
    businessAddress = serializers.CharField(max_length=200,source='address')
    businessPhone = serializers.CharField(max_length=200,source='phone')
    entityName = serializers.CharField(max_length=200,source='businessname')
    plannedRaise = serializers.CharField(max_length=200,source='fundgoal')
    totalMatch = serializers.CharField(max_length=200,source='totalnum')
    topOneName = serializers.CharField(max_length=200,source='cm1name')
    topTwoName = serializers.CharField(max_length=200,source='cm2name')
    topThreeName = serializers.CharField(max_length=200,source='cm3name')
    topFourName = serializers.CharField(max_length=200,source='cm4name')
    topFiveName = serializers.CharField(max_length=200,source='cm5name')
    topSixName = serializers.CharField(max_length=200,source='cm6name')
    topOneNum = serializers.CharField(max_length=200,source='cm1no')
    topTwoNum = serializers.CharField(max_length=200,source='cm2no')
    topThreeNum = serializers.CharField(max_length=200,source='cm3no')
    topFourNum = serializers.CharField(max_length=200,source='cm4no')
    topFiveNum = serializers.CharField(max_length=200,source='cm5no')
    topSixNum = serializers.CharField(max_length=200,source='cm6no')
    totalPrice = serializers.CharField(max_length=200,source='totalprice')
    balanceDue = serializers.CharField(max_length=200,source='balancedue')
    topSixNameList = serializers.ListField(source='top_6_name')
    #topOneInfo = serializers.CharField(max_length=100000,source='infocm1')
    #topTwoInfo = serializers.CharField(max_length=100000,source='infocm2')
    #topThreeInfo = serializers.CharField(max_length=100000,source='infocm3')
    #topFourInfo = serializers.CharField(max_length=100000,source='infocm4')
    #topFiveInfo = serializers.CharField(max_length=100000,source='infocm5')
    #topSixInfo = serializers.CharField(max_length=100000,source='infocm6')    

    class Meta:
        model = Letter_Response
        fields = [
            #'user',
            #'firstname',
            'display_name',
            'businessAddress',
            'businessPhone',
            'entityName',
            'businessname',
            #'count',
            'plannedRaise',
            'totalMatch',
            'topOneName',
            'topTwoName',
            'topThreeName',
            'topFourName',
            'topFiveName',
            'topSixName',
            'topOneNum',
            'topTwoNum',
            'topThreeNum',
            'topFourNum',
            'topFiveNum',
            'topSixNum',
            'intermediaries',
            'price',
            'totalPrice',
            'discount',
            'balanceDue',
            'topSixNameList',
            #'topOneInfo',
            #'topTwoInfo',
            #'topThreeInfo',
            #'topFourInfo',
            #'topFiveInfo',
            #'topSixInfo',
        ]

class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ['user', 'cm1purchase', 'cm2purchase', 'cm3purchase', 'cm4purchase', 'cm5purchase', 'cm6purchase', 'ipurchase', 'cm_matches']
        read_only_fields = ['cm_matches']  # Make cm_matches field read-only

class payLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = pay_load_string
        fields = '__all__'

class referalResponseSerializer(serializers.ModelSerializer):
    referralSource = serializers.CharField(max_length=200,source='referral_source')
    referrerName = serializers.CharField(max_length=200,source='referrer_name')
    referralOther = serializers.CharField(max_length=200,source='referral_other')    
    class Meta:
        model = ReferalResponse
        fields = ['referralSource','referrerName','referralOther']

class preRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreRating
        fields = ['preratings']