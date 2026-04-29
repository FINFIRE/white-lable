from django.db import models
from registration.models import UserDetail
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
#New Entrepreneurial Variable
class EQuestions(models.Model):
    class Meta:
        verbose_name = "J. Cost & Timming (Equestions 10 & 11)"
        verbose_name_plural = "Cost & Timming (Equestions 10 & 11)"

    RADIO_CHOICES1 = [
        ('Minimum $0 - Maximum $499','Minimum $0 - Maximum $499'),
        ('$500 - $999','$500 - $999'),
        ('$1000 - $2499','$1000 - $2499'),
        ('$2500 - $4999','$2500 - $4999'),
        ('$5000 - $9999','$5000 - $9999'),
        ('$10000 - $24999','$10000 - $24999'),
        ('$25000 - $49999','$25000 - $49999'),
        ('$50000+','$50000+')
    ]

    RADIO_CHOICES2 = [
        ('1 Day to 1 Week','1 Day to 1 Week'),
        ('1 Week to 2 Weeks','1 Week to 2 Weeks'),
        ('2 Weeks to 4 Weeks','2 Weeks to 4 Weeks'),
        ('1 Month to 2 Months','1 Month to 2 Months'),
        ('2 Months to 3 Months','2 Months to 3 Months'),
        ('3 Months to 6 Months','3 Months to 6 Months'),
        ('6 Months to 12 Months','6 Months to 12 Months'),
        ('More than 1 year','More than 1 year')
    ]
    # For Up front cost of capital
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0,help_text="Give value from 1 to 10 for all the fields for up front cost of capital")
    RC_zero_to_499 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_500_to_999 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_1000_to_2499 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_2500_to_4999 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_5000_to_9999 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_10000_to_24999 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_25000_to_49999 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RC_More_Than_50000 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    Selected_Option = models.CharField(max_length=200,choices=RADIO_CHOICES1,help_text="Select same option as chosen above.")

    #For timing for process 
    RT_1D_to_1W = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0,help_text="Give value from 1 to 10 for all the fields for required timing for process")
    RT_1W_to_2W = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_2W_to_4W = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_1M_to_2M = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_2M_to_3M = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_3M_to_6M = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_6M_to_12M = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    RT_More_Than_a_Year = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1)],default=0)
    Selected_Option2 = models.CharField(max_length=200,choices=RADIO_CHOICES2,help_text="Select same option as chosen above.")

    def __str__(self):
        return f'{self.user} : {str(self.Selected_Option)}, {str(self.Selected_Option2)}'
    
#FOR STAGE
class EQuestions1(models.Model): # Create a UserDetail TABLE in Database
    class Meta:
        verbose_name = "A. Stage (Equestions1)"
        verbose_name_plural = "A. Stage (Equestions1)"

    RADIO_CHOICES = [
        ('Idea', 'Idea'),
        ('Formation', 'Formation'),
        ('Start Up', 'Start Up'),
        ('Growth', 'Growth'),
        ('M & A', 'M & A'),
        ('Preparing for Public', 'Preparing for Public'),
        ('Distressed', 'Distressed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="This is a radio select question.So enter 1 for only one option that should be chosen and leave other option as 0.")
    Idea = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Formation = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Start_Up = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Growth = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    M_And_A = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Preparing_For_Public = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Distressed = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=RADIO_CHOICES,help_text="Choose the same option as selected above.")

    def __str__(self):
        return (f"{self.user} : {self.Selected_Option}")   

#FOR ENTITY
class EQuestions2(models.Model):
    class Meta:
        verbose_name = "B. Entity, (Equestions2)"
        verbose_name_plural = "B. Entity, (Equestions2)"    
    RADIO_CHOICES = [
        ('None (To be Determined)', 'None (To be Determined)'),
        ('Sole Proprietorship', 'Sole Proprietorship'),
        ('LLC', 'LLC'),
        ('LP', 'LP'),
        ('GP', 'GP'),
        ('S Corporation', 'S Corporation'),
        ('C Corp', 'C Corp'),
        ('Other', 'Other'),
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

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    Business_Name = models.CharField(max_length=200)
    Registration_Region = models.CharField(max_length=200,choices=COUNTRY_STATES_CHOICES)
    No_Business = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)],help_text="This is a radio select question.So enter 1 for only one option that should be chosen and leave other option as 0.")
    Sole_Proprietorship = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    LLC = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    LP = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    GP = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    S_Corporation = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    C_Corp = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Other = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=RADIO_CHOICES,help_text="Choose the same option as chosen above.")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Option}')

#FOR PRE-CAPITAL
class EQuestions3(models.Model):
    class Meta:
        verbose_name = "C. PRE CAPITAL (Equestions3)"
        verbose_name_plural = "C. PRE CAPITAL (Equestions3)"    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="How Much Total Capital has Been Raised till Date? (Choose the Option That Best Defines the Amount):enter 1 for only one option that should be chosen and leave other option as 0.")
    Less_25k = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1),])
    More_25K_Less_100k = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_100k_Less_250K = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_250k_Less_500K = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_500K_Less_1M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_1M_Less_2M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_2M_Less_5M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_5M_Less_10M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_10M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=RADIO_CHOICES,help_text="Select same option as chosen above.")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Option}')

#FOR PRE-MARKET
class EQuestions4(models.Model):
    class Meta:
        verbose_name = "D. Pre Market (Equestions4)"
        verbose_name_plural = "D. Pre Market (Equestions4)"    
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

    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text=" Which Capital Markets Have Been Utilized till Date? (Choose All That Apply): add value of 1 for every options you would like to mark and leave the option 0 for items that are not to be ticked.")
    Accelerator = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Bonds = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Comercial_Banking = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Cryptocurrency = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    EB5_Immigration = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Enterprise_Zones = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Factoring =  models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Grants = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Hedge_Funds = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Incubator = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Investment_Banking = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Other_Owner_Equity = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Private_Debt = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Private_Equity = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Public_Offereing = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Real_Estate = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Royalty_Financing = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Small_Business_Administration = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Venture_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Unsure =  models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Options = models.JSONField(blank=True,default=list,help_text="Please do not edit this field as it may lead to error.")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Options}')

#FOR RAISE
class EQuestions5(models.Model):
    class Meta:
        verbose_name = "E. Ammount of Planned Raise (Equestions5)"
        verbose_name_plural = "E. Ammount of Planned Raise (Equestions5)"

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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="How Much Total Capital is to be Raised in the Next 12 Months? (Choose One Range) by putting value 1 for selected option and 0 for other.")
    Less_25k = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_25K_Less_100k = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_100k_Less_250K = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_250k_Less_500K = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_500K_Less_1M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_1M_Less_1_35M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_1_35M_Less_2M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_2M_Less_5M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_5M_Less_10M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_10M_Less_20M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    More_20M = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Unsure = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=RADIO_CHOICES,help_text="Please select the option as selected above.")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Option}')

#FOR ROUNDS
class EQuestions6(models.Model):
    class Meta:
        verbose_name = "F. Rounds of Capital (Equestions6)"
        verbose_name_plural = "F. Rounds of Capital (Equestions6)"

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

    CHOICES2 = [
        ('One','One'),
        ('Two','Two'),
        ('TBD','TBD'),    
    ]

    #Columns for What round of capital is the Business Engaged in Now?
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text=" What Round of Capital is the Business Engaged in Now?(Select all that apply): add value of 1 for every options you would like to mark and leave the option 0 for items that are not to be ticked.")
    Founders_Round = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Pre_Seed = models.IntegerField(default =0, validators=[MinValueValidator(0),MaxValueValidator(1)])
    Seed = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Series_A = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Series_B = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Series_C = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Pre_Ipo = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Ipo = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Unsure = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Options = models.JSONField(default=list,blank=True,help_text="Please Don't Edit this Option, it may cause error")

    #How many rounds of capital would be raised in the next 12 months?
    One = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)],help_text="How many Tranches/Rounds of capital will be raised in the next 12 months:Choose One by putting value 1 for selected option and 0 for other.")
    Two = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    TBD = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=CHOICES2,help_text="You can select the same option picked above here")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Options} : {self.Selected_Option}')

#FOR USE of FUNDS
class EQuestions7(models.Model):
    class Meta:
        verbose_name = "G. Use of Funds (Equestions7)"
        verbose_name_plural = "G. Use of Funds (Equestions7)" 

    #Columns for What are the primary uses of funds?
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text=" What Are the Primary Uses of Funds? (Choose All That Apply): by adding value 1 for every options you would like to mark and leave the option 0 for items that are not to be ticked.")
    Start_Up = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Growth_Scalabitlity = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Marketing_and_Sales = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Cash_FLow_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Human_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Equipment = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Merger_and_Acquistions = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Inventory = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Real_State = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Other = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Unsure = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Options = models.JSONField(blank=True,default=list,max_length=200,help_text="Please Don't Edit this,It might lead to an error.")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Options}')

#FOR RISK
class EQuestions8(models.Model):
    class Meta:
        verbose_name = "H. RISK ASSESMENT (Equestions8)"
        verbose_name_plural = "H. RISK ASSESMENT (Equestions8)"

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
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="What level of Capital Risk Tolerance of the Lender and/or Investor is required? Choose only one by adding value of 1 for only one option you would like to mark and leave the option 0 for items that are not to be marked.")

    #Columns for first questions founder
    Low_Risk_Tolerance = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Medium_Risk_Tolerance = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    High_Risk_Tolerance = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option = models.CharField(max_length=200,choices=CHOICES1,help_text="You can select the same option picked above here")

    #Columns for Second Questions regarding Risk for Investor
    Low_Cost_Capital = models.IntegerField(default=0, help_text=" What is the level of Capital Cost Tolerance of the Founder/Entrepreneur/Principle: Choose only one by adding value of 1 for only one option you would like to mark and leave the option 0 for items that are not to be marked.")
    Medium_Cost_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    High_Cost_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Very_High_Cost_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Immaterial_Cost_Capital = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    Selected_Option2 = models.CharField(max_length=200,choices=CHOICES2,help_text="You can select the same option picked above here")

    def __str__(self):
        return (f'{self.user} : {self.Selected_Option} : {self.Selected_Option2}')

#FOR DDD1 Add (0 to 5 information) Critical
class DocumentsPrepared(models.Model):
    class Meta:
        verbose_name = "I. Documents Prepared (Equestions 12)"
        verbose_name_plural = "I. Documents Prepared (Equestions 12)"

    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    summary_of_offering = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    financial_forecast = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    lean_business_model = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    presentation_deck = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    leadership_overview = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    exit_strategy = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    offering_documents = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    ai_generated_deep_dive = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    virtual_data_room = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user} : Summary of offering status is {self.summary_of_offering}')

class EQuestions9(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    One_Page_Tear_Sheet = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Elevator_Peach = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Business_Plan = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    DD_Corporate_Identity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    DD_Technology = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    Executive_Summary = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Virtual_Portal = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user} : One Page Tear Sheet status is {self.One_Page_Tear_Sheet}')

# FOR DDD2
class EQuestions10(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    Assumption_Worksheets = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Capital_Structure_Plan = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Capitalization_Table = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Financial_Modeling_FC = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Financial_Modeling_RC = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    Financial_Modeling_SP = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Sources_Uses = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Valuation_Spreadsheets = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Valuation_OLFVW = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user}')

# FOR DDD3
class EQuestions11(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    Business_Model_Canvas = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Company_Website_V3 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Website_Marketing = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Due_Diligence_CA = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Marketing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    Marketing_Plan_Budget = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Marketing_Research_Report = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Presentation_Deck = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Strategic_Tactical_Plan = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user}')

# FOR DDD4
class EQuestions12(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    Leadership = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Management_Experience = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Consultant_Advisor = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Staff = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Culture = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user}')

# FOR DDD5
class EQuestions13(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,help_text="Give Value From 0 to 5 for each box based on Due Diligence.")
    Capital_Marketing_Plan = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Capital_Offering_Documents = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Due_Diligence_IP = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Due_Diligence_LE = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    Due_Diligence_RA = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    Exit_Strategy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)

    def __str__(self):
        return (f'{self.user}')
      
#FOR REGION TO MATCH INTERMEDIARIES
class EQuestions14(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Required_Intermediaries_Region = models.CharField(max_length=200,choices=REGION_CHOICES,help_text="Intermediary region required for you")
    Industry_Type = models.CharField(max_length=200,choices=INDUSTRY_CHOICES,help_text='Select Your Industry Type')

    def __str__(self):
        return (f'{self.user}')

class PreRating(models.Model):
    class Meta:
        verbose_name = "K. Pre Rating"
        verbose_name_plural = "K. Pre Ratings"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preratings = models.JSONField(default=dict)

    def __str__(self):
        return (f'{self.user}')

class ReferalResponse(models.Model):
    class Meta:
        verbose_name = "L. Referal"
        verbose_name_plural = "L. Referals"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    REFERRAL_CHOICES = [
        ("A Friend / Colleague", "A Friend / Colleague"),
        ("Financial Advisor / Consultant", "Financial Advisor / Consultant"),
        ("Social Media", "Social Media"),
        ("Online Search", "Online Search"),
        ("News / Article / Blog", "News / Article / Blog"),
        ("Event / Webinar", "Event / Webinar"),
        ("Other", "Other"),
    ]
    referral_source = models.CharField(
        max_length=255,
        null=True,
        default=None,
        choices=REFERRAL_CHOICES,
        verbose_name="How did you hear about us?"
    )
    referrer_name = models.CharField(
        max_length=255,
        default=None,
        null=True,
        verbose_name="Referrer's Name (if any)"
    )
    referral_other = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        verbose_name="Other (please specify)"
    )
    def __str__(self):
        return (f'User : {self.user} , Referral Source : {self.referral_source} , Referrer Name : {self.referrer_name} , Referral Other : {self.referral_other}')

class LendingRequirements(models.Model):
    COLLATERAL_OPTIONS =[
        ("Not Applicable","Not Applicable"),
        ("Yes","Yes"),
        ("No","No"),
        ("Unknown","Unknown"),
    ]
    CREDIT_SCORE_OPTIONS = [
        ("<580","<580"),
        (">620",">620"),
        (">680",">680"),
        (">720",">720"),
        (">760",">760"),
    ]

    CRIMINAL_HISTORY_OPTIONS = [
        ("None","None"),
        ("Misdemeanor","Misdemeanor"),
        ("Felony","Felony"),
        ("Fraud","Fraud"),
        ("Securities Violation","Securities Violation"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collateral_status = models.CharField(blank=True,max_length=255,choices=COLLATERAL_OPTIONS,help_text='Select your collateral availability option.')
    credit_score = models.CharField(blank=True,max_length=255,choices=CREDIT_SCORE_OPTIONS,help_text='Select your credit score option.')
    criminal_history = models.CharField(max_length=255,choices=CRIMINAL_HISTORY_OPTIONS,help_text='Point out any one of the criminal History from the options if any.')
    
    def __str__(self):
        return (f'{self.user}')       