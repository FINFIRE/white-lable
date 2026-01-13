from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from .models import ReferalResponse,LendingRequirements

class EQuestionsForma(forms.Form):
    RADIO_CHOICES1 = [
        ('Minimum $0 - Maximum $499','Minimum $0 - Maximum $499'),
        ('Minimum $500 - Maximum $999','Minimum $500 - Maximum $999'),
        ('Minimum $1000 - Maximum $2499','Minimum $1000 - Maximum $2499'),
        ('Minimum $2500 - Maximum $4999','Minimum $2500 - Maximum $4999'),
        ('Minimum $5000 - Maximum $9999','Minimum $5000 - Maximum $9999'),
        ('Minimum $10000 - Maximum $24999','Minimum $10000 - Maximum $24999'),
        ('Minimum $25000 - Maximum $49999','Minimum $25000 - Maximum $49999'),
        ('More than $50000+','More than $50000+')
    ]
    upfrontcost = forms.ChoiceField(
        choices=RADIO_CHOICES1, 
        widget=forms.RadioSelect,
        label=mark_safe("<b><u>Please define the range of your expectation of costs associated with raising capital including the hiring of intermediaries, financing fees, and other 'UP FRONT Costs of Capital' considerations (Choose one of the following)<br>Range of Cost is</u></b>"))    

    
    #For range of time
class EQuestionsFormb(forms.Form):   
    RADIO_CHOICES1 = [
        ('1 Day to 1 Week','1 Day to 1 Week'),
        ('1 Week to 2 Week','1 Week to 2 Week'),
        ('2 Weeks to 4 Weeks','2 Weeks to 4 Weeks'),
        ('1 Month to 2 Months','1 Month to 2 Months'),
        ('2 Months to 3 Months','2 Months to 3 Months'),
        ('3 Months to 6 Months','3 Months to 6 Months'),
        ('6 Months to 12 Months','6 Months to 12 Months'),
        ('More than 1 year','More than 1 year')
    ]
    timming = forms.ChoiceField(
        choices=RADIO_CHOICES1, 
        widget=forms.RadioSelect,
        label=mark_safe("<b><u>The timing of finance is also a critical factor in determining capital type (How long will the process take from application to capital).  From start to finish, what time-frame will be acceptable to complete the application, interviews, forms, due diligence, presentation materials, supporting materials, data room creation, review, analysis, introduction to capital markets & Capitalization (Choose One Option)</u></b>"))       
 

class EQuestions1Form(forms.Form):
    RADIO_CHOICES = [
        ('Idea', mark_safe('Idea <span class="tooltip">ℹ️<span class="tooltip-text">Business & Company Not Yet Formed</span></span>')),
        ('Formation', mark_safe('Formation <span class="tooltip">ℹ️<span class="tooltip-text">Entity Created, Business & Financial Models Defined, & Market Identified</span></span>')),
        ('Start Up', mark_safe('Start Up <span class="tooltip">ℹ️<span class="tooltip-text">Formation Phase Complete Plus Operating Entity & Post Proof of Concept</span></span>')),
        ('Growth', mark_safe('Growth <span class="tooltip">ℹ️<span class="tooltip-text">Startup Phase Complete Plus Post Revenue (Pre or Post Profit) & Growing</span></span>')),
        ('M & A', mark_safe('M & A <span class="tooltip">ℹ️<span class="tooltip-text">Growth Company Preparing to Acquire, be Acquired or Merge</span></span>')),
        ('Preparing for Public', mark_safe('Preparing for Public <span class="tooltip">ℹ️<span class="tooltip-text">Preparing for IPO, Reverse Merger, Form S1- Filing, or be Acquired by a PubCo</span></span>')),
        ('Distressed', mark_safe('Distressed <span class="tooltip">ℹ️<span class="tooltip-text">Cash Flow Problems, Preparing for Wind-Up, BK, or Emergency Capital Required</span></span>'))
    ]
    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES, 
        widget=forms.RadioSelect,
        label=mark_safe("""<b><u>What is the Stage of Business Development?</u><br><br>Choose one option by marking the radio button</b>"""))

class EQuestions2Form(forms.Form):
    RADIO_CHOICES = [
        ('None (To be Determined)', mark_safe('None (To be Determined) <span class="tooltip">ℹ️<span class="tooltip-text">Company Not Yet Formed</span></span>')),
        ('Sole Proprietorship', mark_safe('Sole Proprietorship <span class="tooltip">ℹ️<span class="tooltip-text">Individual Owns the Business; No Entity Formed</span></span>')),
        ('LLC', mark_safe('LLC <span class="tooltip">ℹ️<span class="tooltip-text">Limited Liability Company; Formed Under the Rules of a Specific State</span></span>')),
        ('LP', mark_safe('LP <span class="tooltip">ℹ️<span class="tooltip-text">Limited Partnership (Fund, Professional Corp)</span></span>')),
        ('GP', mark_safe('GP <span class="tooltip">ℹ️<span class="tooltip-text">General Partnership (Fund, Management Company)</span></span>')),
        ('S Corporation', mark_safe('S Corporation <span class="tooltip">ℹ️<span class="tooltip-text">Small Corporation Registered as an "S" Corp with Tax Exceptions</span></span>')),
        ('C Corp', mark_safe('C Corp <span class="tooltip">ℹ️<span class="tooltip-text">Corporation</span></span>')),
        ('Other', mark_safe('Other <span class="tooltip">ℹ️<span class="tooltip-text">International, 3CP, Non-Profit</span></span>')),
    ]
    
    COUNTRY_STATES_CHOICES = [
        ('Alabama', 'Alabama'),
        ('Alaska', 'Alaska'),
        ('Arizona', 'Arizona'),
        ('Arkansas', 'Arkansas'),
        ('California', 'California'),
        ('Colorado', 'Colorado'),
        ('Connecticut', 'Connecticut'),
        ('Delaware', 'Delaware'),
        ('Florida', 'Florida'),
        ('Georgia', 'Georgia'),
        ('Hawaii', 'Hawaii'),
        ('Idaho', 'Idaho'),
        ('Illinois', 'Illinois'),
        ('Indiana', 'Indiana'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Louisiana', 'Louisiana'),
        ('Maine', 'Maine'),
        ('Maryland', 'Maryland'),
        ('Massachusetts', 'Massachusetts'),
        ('Michigan', 'Michigan'),
        ('Minnesota', 'Minnesota'),
        ('Mississippi', 'Mississippi'),
        ('Missouri', 'Missouri'),
        ('Montana', 'Montana'),
        ('Nebraska', 'Nebraska'),
        ('Nevada', 'Nevada'),
        ('New Hampshire', 'New Hampshire'),
        ('New Jersey', 'New Jersey'),
        ('New Mexico', 'New Mexico'),
        ('New York', 'New York'),
        ('North Carolina', 'North Carolina'),
        ('North Dakota', 'North Dakota'),
        ('Ohio', 'Ohio'),
        ('Oklahoma', 'Oklahoma'),
        ('Oregon', 'Oregon'),
        ('Pennsylvania', 'Pennsylvania'),
        ('Rhode Island', 'Rhode Island'),
        ('South Carolina', 'South Carolina'),
        ('South Dakota', 'South Dakota'),
        ('Tennessee', 'Tennessee'),
        ('Texas', 'Texas'),
        ('Utah', 'Utah'),
        ('Vermont', 'Vermont'),
        ('Virginia', 'Virginia'),
        ('Washington', 'Washington'),
        ('West Virginia', 'West Virginia'),
        ('Wisconsin', 'Wisconsin'),
        ('Wyoming', 'Wyoming'),
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('North Korea', 'North Korea'),
        ('South Korea', 'South Korea'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Timor-Leste', 'Timor-Leste'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')
    ]

    Business_Name = forms.CharField(max_length=200,required=True,label=mark_safe('<u><b>What Type of Business Entity?<br><br></b></u>Fill in: What is the Name of the Business Entity?(Type "None" If Not Created)<span class="tooltip">ℹ️<span class="tooltip-text">Include Full Name (Including Commas & Periods, Where Applicable)</span></span>'))
    Registration_Region = forms.ChoiceField(choices=COUNTRY_STATES_CHOICES,\
    label=mark_safe("<b>Pull Down Menu:  State of Entity Registration (Or, Country if Outside the USA)</b>"))
    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES, 
        widget=forms.RadioSelect,
        label="Choose One Answer by Marking the Radio Button"
    )
class EQuestions3Form(forms.Form):
    RADIO_CHOICES = [
        ('Less than $25,000', 'Less than $25,000'),
        ('$26,000 to $100,000', '$26,000 to $100,000'),
        ('$101,000 to $250,000', '$101,000 to $250,000'),
        ('$251,000 to $500,000', '$251,000 to $500,000'),
        ('$501,000 to $1,000,000', '$501,000 to $1,000,000'),
        ('$1,000,001 to $2,000,000', '$1,000,001 to $2,000,000'),
        ('$2,000,001 to $5,000,000', '$2,000,001 to $5,000,000'),
        ('$5,000,001 to $10,000,000', '$5,000,001 to $10,000,000'),
        ('More than $10,000,000','More than $10,000,000')
    ]
    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES, 
        widget=forms.RadioSelect,
        label=mark_safe("<u><b>How Much Total Capital has Been Raised to Date? (Choose the Option That Best Defines the Amount)</b></u>")
    )

class EQuestions4Form(forms.Form):
    CHOICES = [
        ('Accelerator','Accelerator'),
        ('Bonds', 'Bonds'),
        ('Commercial Banks', 'Commercial Banks'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('EB5 Immigration','EB5 Immigration'),
        ('Enterprise Zones','Enterprise Zones'),
        ('Factoring','Factoring'),
        ('Grants','Grants'),
        ('Hedge Funds','Hedge Funds'),
        ('Incubator','Incubator'),
        ('Investment Banking','Investment Banking'),
        ('Other (Owner Equity)','Other (Owner Equity)'),
        ('Private Debt (Officer Loans to Startup)','Private Debt (Officer Loans to Startup)'),
        ('Private Equity Securities','Private Equity Securities'),
        ('Public Offering','Public Offering'),
        ('Real Estate','Real Estate'),
        ('Royalty Financing','Royalty Financing'),
        ('Small Business Administration (SBA)','Small Business Administration (SBA)'),
        ('Venture Capital','Venture Capital'),
        ('Unsure/Do not Know','Unsure/Do not Know')
    ]
    Market = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES,\
                                       label =mark_safe('<b><u>Which Capital Markets Have Been Utilized To Date? (Choose All That Apply)</u></b>'))

class EQuestions5Form(forms.Form):
    RADIO_CHOICES = [
        ('Less than $25,000', 'Less than $25,000'),
        ('$25,000 to $100,000', '$25,000 to $100,000'),
        ('$100,000 to $249,999', '$100,000 to $249,999'),
        ('$250,000 to $499,999', '$250,000 to $499,999'),
        ('$500,000 to $999,999', '$500,000 to $999,999'),
        ('$1,000,000 to $1,349,999', '$1,000,000 to $1,349,999'),
        ('$1,350,000 to $1,999,999', '$1,350,000 to $1,999,999'),
        ('$2,000,000 to $4,999,999', '$2,000,000 to $4,999,999'),
        ('$5,000,000 to $9,999,999','$5,000,000 to $9,999,999'),
        ('$10,000,000 to $19,999,999','$10,000,000 to $19,999,999'),
        ('More Than $20 Million','More Than $20 Million'),
        ('Unsure/Do not Know/TBD','Unsure/Do not Know/TBD'),
    ]    
    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES, 
        widget=forms.RadioSelect,
        label=mark_safe('<b><u>How Much Total Capital is to be Raised in the Next 12 Months? (Choose One Range)</b></u>')
    )

class EQuestions6Form(forms.Form):
    CHOICES = [
        ('Founders Round','Founders Round'),
        ('Pre-Seed', 'Pre-Seed'),
        ('Seed', 'Seed'),
        ('Series A', 'Series A'),
        ('Series B','Series B'),
        ('Series C','Series C'),
        ('Pre-IPO','Pre-IPO'),
        ('IPO','IPO'),
        ('Unsure/Do not Know/TBD','Unsure/Do not Know/TBD'),
    ]
    capital_market = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,\
                    choices=CHOICES,label=mark_safe('<b><u>What Round of Capital Is the Business Engaged In Now?</b></u>'))

    CHOICES2 = [
        ('One','One'),
        ('Two','Two'),
        ('TBD','TBD'),    
    ]

    selected_option = forms.ChoiceField(
        choices=CHOICES2, 
        widget=forms.RadioSelect,
        label=mark_safe("<b><u>How Many Tranches/Rounds of Capital Will Be Raised in the Next 12 Months?</b></u>")
    )

class EQuestions7Form(forms.Form):
    CHOICES = [
        ('Startup/Working','Startup/Working'),
        ('Growth Scalability', 'Growth Scalability'),
        ('Marketing & Sales', 'Marketing & Sales'),
        ('Cash Flow Capital', 'Cash Flow Capital'),
        ('Human Capital','Human Capital'),
        ('Equipment','Equipment'),
        ('Merger & Acquitions','Merger & Acquitions'),
        ('Inventory','Inventory'),
        ('Real Estate','Real Estate'),
        ('Other','Other'),
        ('Do not Know/Unsure/TBD','Do not Know/Unsure/TBD'),
    ]
    selected_uses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES,\
                                       label = mark_safe('<b><u>What Are the Primary Uses of Funds? (Choose All That Apply)</b></u>'))

class EQuestions8Form(forms.Form):
    CHOICES1 = [
        ('Very Low/Low Risk Tolerance (Expect to at least recoup principle)', 'Very Low/Low Risk Tolerance (Expect to at least recoup principle)'),
        ('Medium Risk Tolerance (Can lose some or most of the funding)', 'Medium Risk Tolerance (Can lose some or most of the funding)'),
        ('High Risk Tolerance (Can lose most or all of the funding)', 'High Risk Tolerance (Can lose most or all of the funding)'),
    ]

    CHOICES2 = [
        ('Low Cost of Capital (1-4%)', 'Low Cost of Capital (1-4%)'),
        ('Medium Cost of Capital (5-10%)', 'Medium Cost of Capital (5-10%)'),
        ('High Cost of Capital (11-18%)', 'High Cost of Capital (11-18%)'),
        ('Very High Cost of Capital (19%+)', 'Very High Cost of Capital (19%+)'),
        ('As long as the enterprise receives the net amount it needs, the cost is immaterial', 'As long as the enterprise receives the net amount it needs, the cost is immaterial'),
    ]

    selected_option1 = forms.ChoiceField(
        choices=CHOICES1, 
        widget=forms.RadioSelect,
        label=mark_safe("<b><u>What level of Capital Risk Tolerance of the Lender and/or Investor is required?</b></u>")
    )

    selected_option2 = forms.ChoiceField(
        choices=CHOICES2, 
        widget=forms.RadioSelect,
        label=mark_safe("<b><u>What is the level of Capital Cost Tolerance of the Founder/Entrepreneur/Principle?</b></u>")
    )

class DocumentsPreparedForm(forms.Form):
    SWITCH_CHOICES = [(1, 'Yes'), (0, 'No')]  # Choices for the switch

    summary_of_offering = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Summary of Offering <span class="tooltip">ℹ️<span class="tooltip-text">A 1-page summary of the business and its offering - value proposition, business model, financial model, the capital ask, contact information, logo.</span></span></b></u>'),
    )
    
    financial_forecast = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Financial Forecasts, Pro forma with Valuation - Opinion Letter & Final Valuation Write-Up <span class="tooltip">ℹ️<span class="tooltip-text">Individual and combined worksheets showing revenue, payroll, marketing, general administrative worksheets, variable expenses, cost of goods. Worksheets merged with cash flow, profit & loss, equity, and use of funds all in one worksheet. Connected to valuation.</span></span></b></u>'),
    )

    lean_business_model_canvas = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Lean Business Model Canvas <span class="tooltip">ℹ️<span class="tooltip-text">Customer segments, value propositions, channels, customer relationships, revenue streams, key activities, key resources, key partners, cost structure.</span></span></u></b>'),
    )
    
    presentation_deck = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Presentation Deck <span class="tooltip">ℹ️<span class="tooltip-text">12-15-Page graphical summary: (1) Pitch/Opportunity;  (2) Company; (3) Problem/Solution; (4) Business Model; (5) Financial Model; Market Size (TAM, SAM, SOM); Pro forma forecast; Valuation; Management Team of the business plan, strategic plan, tactical plan</span></span></b></u>'),
    )
    
    leadership_overview = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Leadership Overview <span class="tooltip">ℹ️<span class="tooltip-text">Summary write up of executive team resumes, bios, organizational chart, staffing.  Background checks on the management team, executives, If applicable:  define advisors, consultants, board members, attorneys, accountants, and other industry professionals.  If applicabel, a description of Staff duties, responsibilities & Job Descriptions; Leadership Style, urgency, timeliness, teamwork, work environment</span></span></b></u>'),
    )
    
    exit_strategy = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Exit Strategy <span class="tooltip">ℹ️<span class="tooltip-text">Definition of liquidity events, M & A strategy, succession plan, convertible note.</span></span></b></u>'),
    )

    offering_documents = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Offering Documents <span class="tooltip">ℹ️<span class="tooltip-text">1st pre-legal review draft of the offering documents outlining the opportunity, summary of the offering, subscription process.</span></span></b></u>'),
    )

    ai_generated_deep_dive = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>AI Generated Deep Dive <span class="tooltip">ℹ️<span class="tooltip-text">Does the Company have a corporate video presentation, Does the company have an AI generated podcast that summarizes the deal (Either in video or audio format)?</span></span></b></u>'),
    )
        
    virtual_data_room = forms.ChoiceField(
        choices=SWITCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'switch-input'}),
        label=mark_safe('<b><u>Virtual Data Room <span class="tooltip">ℹ️<span class="tooltip-text">Documents updated, re-dated as necessary, minor updates to presentation materials, updates to investor access levels.  We call this the Managed Virtual Portal (MVP).</span></span></b></u>'),
    )

class RatingForm(forms.Form):
    financial_model_forecast_pro_forma = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Financial Model, forecast, pro forma <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    finfire_report_capital_type = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Finfire Report - Capital Type <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    due_diligence_checklist_documents = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Due Diligence Checklist Documents <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    historical_financials = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Historical Financials (P & L, BS, CF, Aging) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    tax_returns = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Tax Returns (Up to 2 years, if applicable) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    business_valuation_equity_only = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Business Valuation (Equity only) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    cap_table_use_of_funds_and_capitalization_plan = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Cap Table, Use of Funds, & Capitalization Plan <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    business_model_canvas = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Business Model Canvas <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    offering_documents_rating = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Offering Documents <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    presentation_video_ai_deep_dive = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Presentation Video (From the AI Deep Dive) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    application_if_applicable = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Application (If Applicable) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    resume_of_founder_ceo_primary_leader = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Resume of Founder/CEO Primary Leader <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    presentation_deck_rating = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Presentation Deck <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    executive_summary_including_exit_strategy = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Executive Summary Including Exit Strategy <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    quality_assurance_checklist_including_ai = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Quality Assurance Checklist (Including AI) <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    capital_match_list_generated = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Capital Match List Generated <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    investor_marketing_campaign = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Investor Marketing Campaign <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    investor_relations = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Investor Relations <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )

    progress_reports = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 10}),
        initial=0,
        label=mark_safe('Progress Reports <span class="tooltip">ℹ️<span class="tooltip-text">Rate the completion of this task on a scale of 0–10. 10 indicates the task is fully completed with no further work required; 0 indicates the task has not been initiated.</span></span>'),
    )
    
class EQuestions9Form(forms.Form):
    onepagetearsheet = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='A 1-page summary of the business and its offering -\
                                              value proposition, business model, financial model, the capital ask, contact information, logo.',
                                        label ='One Page Tear Sheet',
                                        )
    
    elevetorpitch = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Define the elevator pitch - mission, strategic-tactics.',
                                       label= 'Elevator Pitch',
                                       )
    
    businesplan = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text='Purpose, pitch, offering summary, company, business model, financial model, marketing plan, operational plan, management team, exit strategy',
                                     label = 'Business Plan',
                                     )
    
    duediligenceci = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='Entity standing, state registration, organizational document review, meeting minutes, corporate governance report.',
                                        label='Due Diligence - Corporate Identity',
                                        )
    
    dueilgencet = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'Report on technology, due diligence on competition known or unknown, validation of technology claims.',
                                     label='Due Diigence - Technology',
                                     )
    
    executivesummary = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='A 5-7-page written summary of the marketing plan, strategic plan, tactical plan, 1-page financial summary, summary of the offering.',
                                          label= 'Executive Summary',
                                          )
    
    virtualportal = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Documents updated, re-dated as necessary, minor updates to presentation materials, updates to investor access levels.  We call this the Managed Virtual Portal (MVP).',
                                       label = 'Virtual Portal (Data Room)',
                                       )

class EQuestions10Form(forms.Form):
    assumption_worksheets= forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='Assumption’s worksheets may include key performance indicators (KPIs); industry standard statistics, facts or percentages, cost of goods, price strategies, (TAM), (SAM), (SOM), market penetration modeling, and other growth and revenue assumptions.',
                                        label = 'Assumptions Worksheets'
                                        )
    
    capital_structure_plan = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Type of capital, amount of capital, capital stack and tranches, increases in valuation.',
                                       label= 'Capital Structure Plan',
                                       )
    
    capitalization_table = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text='List of all equity owners, amount paid, and ownership percentage.',
                                     label ='Capitalization Table',
                                     )
    
    financial_modeling_FC = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text = 'Payroll worksheets, marketing worksheets, sales & general administrative worksheets.',
                                        label = 'Financial Modeling - Fixed Costs',
                                        )
    
    financial_modeling_RC = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'Worksheets are built and linked for each revenue streams with direct (variable expenses & cost of goods) and indirect (fixed expenses) costs.',
                                     label = 'Financial Modeling - Revenues & Costs',
                                     )
    
    financial_modeling_SP = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='Worksheets merged between cash flow, profit & loss, equity, and use of funds all in one worksheet (Best presented with 1-page tear sheet or CANVAS).',
                                          label = 'Financial Modeling – Summary Page',
                                          )
    
    sources_uses = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Capital type, amount, and use of funds (With a Timeline).',
                                       label = 'Sources & Uses',
                                       )

    valuation_spreadsheets = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Research for a 409A Valuation with a review of financial statements, company comparisons for market comp, discounted cash flow analysis, capitalization table, value of equity for tax purposes.',
                                       label = 'Valuation - Spreadsheets',
                                       )

    valuation_OLFVW = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Cover letter, qualifications, weighted valuation summary, methodology report, range of company value.',
                                       label = 'Valuation - Opinion Letter & Final Valuation Write-Up'
                                       )    

class EQuestions11Form(forms.Form):
    business_model_canvas= forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='1-page summary - customer segments, value propositions, channels, customer relationships, revenue streams, key activities, key resources, key partners, cost structure.',
                                        label = 'BMC (Business Model Canvas) ',
                                        )
    
    company_website_V3 = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Type of capital, amount of capital, capital stack and tranches, increases in valuation.',
                                       label = 'Company Website - On Web 3.0',
                                       )
    
    website_marketing = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text='Domain name; hosting; Speed; SSL security; SEO friendly; tracking and analytics; social media integration; content; mobile friendly; navigation; branding; typography, layout; about us page; contact us; FAQs; product and services; video content.',
                                     label = 'Website Marketing',
                                     )
    
    due_diligence_CA = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text = 'Total competitive landscape, direct competitive analysis, indirect competitive analysis, comparison chart, market penetration modeling.',
                                        label = 'Due Diligence - Competitive Analysis',
                                        )
    
    marketing = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'TAM - SAM - SOM Report: TAM:  total addressable market SAM: serviceable addressable market SOM:  serviceable obtainable market.',
                                     label = 'Marketing',
                                     )
    
    marketing_plan_budget = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='Includes SEO, TAM/SAM/SOM - SEO/PPC direct expenses, variable expense, budget, CAC, SWOT, pricing strategy, analyze brand, images, website.',
                                          label = 'Marketing Plan & Budget'
                                          )
    
    marketing_research_report = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='Market size, demand, penetration requirements, demographics, prepared written report with references, citations, footnotes.',
                                          label = 'Market Research Report',
                                          )
    presentation_deck = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='12-18-page graphical summary of the business plan, strategic plan, tactical plan, 1-Page Tear Sheet, offering.',
                                          label = 'Presentation Deck',
                                          )
    
    strategic_tactical_plan = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                          help_text='MVP (minimum viable product), value proposition, business model defined, financial model defined, mission statement, vision statement.',
                                          label = 'Strategic & Tactical Plan',
                                          )

class EQuestions12Form(forms.Form):
    leadership= forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='Summary write up of executive team resumes, bios, organizational chart, staffing.',
                                        label = 'Leadership',
                                        )
    
    management_experience = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='Background checks on the management team, executives, confirmation of all material submitted, report prepared',
                                       label = 'Management Experience',
                                       )
    
    consultant_advisor = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text='Due Diligence review of consulting team, Board Members, advisors, attorneys, accountants, professionals, & advisory team',
                                     label = 'Consultants & Advisors',
                                     )
    
    staff = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text = 'Description of Staff duties, responsibilities & Job Descriptions',
                                        label = 'Staff',
                                        )
    
    culture = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'Leadership Style, urgency, timeliness, teamwork, work environment',
                                     label = 'Culture',
                                     )
    
class EQuestions13Form(forms.Form):
    capital_marketing_plan= forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text='Email blast to all potential investors to data room, list of investors.',
                                        label = 'Capital Marketing Plan',
                                        )
    
    capital_offering_documents = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                       help_text='1st pre-legal review draft of the offering documents outlining the opportunity, summary of the offering, subscription process.',
                                       label = 'Capital Offering Documents',
                                       )
    
    due_diligence_IP = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text='Summary report of all proposed claims, ownership of property, rights, documentation.',
                                     label='Due Diligence - Intelectual Property',
                                     )
    
    due_diligence_LE = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                        help_text = 'Scrubbed for legal issues, governmental compliance, litigation.',
                                        label = 'Due Diligence - Legal',
                                        )
    
    due_diligence_RA = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'A Risk report - Potential liabilities on product and/or services; risks associated with the industry, entity type, business model.',
                                     label = 'Due Diligence - Risk Assesment'
                                     )   
    
    exit_strategy = forms.IntegerField(validators= [MinValueValidator(0),MaxValueValidator(5)],
                                     help_text= 'Definition of liquidity events, M & A strategy, succession plan, convertible note.',
                                     label= 'Exit Strategy'
                                     )
    
class EQuestions14Form(forms.Form):
    REGION_CHOICES =[
        ('Africa', 'Africa'),
        ('Antarctica', 'Antarctica'),
        ('Asia', 'Asia'),
        ('Australia', 'Australia'),
        ('Canada', 'Canada'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Oceana', 'Oceana'),
        ('South America','South America'),
        ('United States (All 50 States & Territories)','United States (All 50 States & Territories)'),
    ]

    INDUSTRY_CHOICES =[
        ('Administration','Administration'),
        ('Agriculture','Agriculture'),
        ('Arts','Arts'),
        ('Energy/Utilities','Energy/Utilities'),
        ('Entertainmen','Entertainment'),
        ('Finance','Finance'),
        ('High tech','High tech'),
        ('Hospitality, F & B','Hospitality, F & B'),
        ('Info Services','Info Services'),
        ('Manufacturing','Manufacturing'),
        ('Mining','Mining'),
        ('Professional Insurance/Mgmt','Professional Insurance/Mgmt'),
        ('Real State','Real State'),
        ('Science - Health - Medicine','Science - Health - Medicine'),
        ('Sector/Sub-Sector','Sector/Sub-Sector'),
        ('Trades - Construction','Trades - Construction'),
        ('Transportation & Logistics','Transportation & Logistics'),
        ('Waste Management','Waste Management'),
        ('Wholesale & Retail','Wholesale & Retail'),
        ('Other','Other'),
    ]
    required_intermediaries_region = forms.ChoiceField(choices = REGION_CHOICES,label = 'Choose the region you would require intermediaries from:' )
    industry_types = forms.ChoiceField(choices = INDUSTRY_CHOICES,widget=forms.RadioSelect,\
                                       label ='Select the type of Industry you are:')
    

class ReferralResponseForm(forms.ModelForm):
    class Meta:
        model = ReferalResponse
        fields = ['referral_source', 'referrer_name', 'referral_other']
        widgets = {
            'referral_source': forms.Select(attrs={'class': 'form-select'}),
            'referrer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Referrer's Name"}),
            'referral_other': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please specify'}),
        }
        labels = {
            'referral_source': 'How did you hear about us?',
            'referrer_name': "Referrer\'s Name (if any), type None if not applicable",
            'referral_other': 'Other (please specify), type None if not applicable',
        }

    def save(self, user: User, commit: bool = True):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance

class LendingRequirementsForm(forms.ModelForm):
    class Meta:
        model = LendingRequirements
        fields = ['collateral_status','credit_score','criminal_history']
        widgets = {
            'collateral_status': forms.Select(attrs={'class': 'form-select'}),
            'credit_score': forms.Select(attrs={'class': 'form-select', 'placeholder': "Credit Score"}),
            'criminal_history': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'collateral_status': 'Do you have collateral available for lending (Property, Assets, Inventory)?',
            'credit_score': "What is your credit score? Please enter it below:",
            'criminal_history': 'Please select criminal history, if you have any.',
        }
    def save(self, user: User, commit: bool = True):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance        

