from django import forms
from .models import IQuestions1,IQuestions2

#Create Forms here
class IQuestions1Form(forms.Form):
    CHOICES_CM = [
        ('option1','Accelerator'),
        ('option2', 'Bonds'),
        ('option3', 'Commercial Banks'),
        ('option4', 'Cryptocurrency'),
        ('option5','EB5 Immigration'),
        ('option6','Enterprise Zones'),
        ('option7','Factoring'),
        ('option8','Grants'),
        ('option9','Hedge Funds'),
        ('option10','Incubator'),
        ('option11','Investment Banking'),
        ('option12','Other (Owner Equity)'),
        ('option13','Private Debt (Officer Loans to Startup)'),
        ('option14','Private Equity Securities '),
        ('option15','Public Offering'),
        ('option16','Real State'),
        ('option17','Royalty Financing'),
        ('option18','Small Business Administration (SBA)'),
        ('option19','Venture Capital'),
    ]

    CHOICES_I =[
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

    CHOICES_R =[
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
    CHOICE_EXPERTISE = [
        ('Technical Writer','Technical Writer'),
        ('Content Creator', 'Content Creator'),
        ('Business Consultant', 'Business Consultant'),
        ('Maketing Analyst', 'Maketing Analyst'),
        ('Business Plan writter','Business Plan writter'),
        ('Business Attorney','Business Attorney'),
        ('Researcher','Researcher'),
        ('Subject Matter Expert','Subject Matter Expert'),
        ('Business Analyst','Business Analyst'),
        ('Data Entry','Data Entry'),
        ('Financial Analyst','Financial Analyst'),
        ('Accountant','Accountant'),
        ('CPA','CPA'),
        ('Financial Modeler','Financial Modeler'),
        ('Valuation Analyst','Valuation Analyst'),
        ('Banker','Banker'),
        ('Web Developer','Web Developer'),
        ('Marketing Consultant','Marketing Consultant'),
        ('Transfer Agency','Transfer Agency'),
        ('Graphic Designer','Graphic Designer'),
        ('HR Due Diligence','HR Due Diligence'),
        ('Management Consultant','Management Consultant'),
        ('HR Consultant','HR Consultant'),
        ('Culture Subject Matter Expert','Culture Subject Matter Expert'),
        ('Broker Agency','Broker Agency'),
        ('Platform','Platform'),
        ('Securities Attorney','Securities Attorney'),
        ('Paralegal','Paralegal'),
        ('Intelectual Property Attorney','Intelectual Property Attorney'),
        ('Legal Assistant','Legal Assistant'),
        ('Risk Analyst','Risk Analyst'),
        ('Underwritter','Underwritter'),
    ]

    intermediaries_expertise = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,\
                    choices=CHOICE_EXPERTISE,label='What is your Document Subject Matter Expertise? (Select All That Apply)')

    specialized_industry = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = CHOICES_I,label ='What Industry (s) do you Specialize In? (Select All That Apply)')
    
    prefered_cm = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES_CM,\
                                       label ='What is your prefered Capital Market?\
                                          (Choose All That Apply)')
    
    regions_served = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = CHOICES_R,label='What Geographic Region Do You Serve?  (Select All That Apply)')

class IQuestions2Form(forms.Form):
    CHOICES_T = [
        ('Hourly','Hourly'),
        ('Fixed Price','Fixed Price'),
        ('Commision','Commision'),
        ('Royalty','Royalty'),
        ('By the Project','By the Project'),
        ('Success Fees','Success Fees'),
        ('Others','Others'),
    ]

    pay_type = forms.ChoiceField(choices=CHOICES_T, label ='What is Your Fee Schedule?')
    rate = forms.IntegerField(min_value=0,label='Enter your rate (Min value for rate is 0)')
    explanation = forms.CharField(label= 'Please write some explanation for the rate',required=True)

