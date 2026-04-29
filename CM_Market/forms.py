from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator


# Creating Forms here
class VQuestion1Form(forms.Form):
    CHOICES_STATE = [
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
    ]

    CHOICES_CM =[
        ('5- Reg CF','5- Reg CF'),
        ('65- Regulation A','65- Regulation A'), #GOOD
        ('1- Private Equity','1- Private Equity'),
        ('77- SBA 504','77- SBA 504'), #GOOD
        ('13 - Lines of Credit','13 - Lines of Credit'),
        ('Regulation D 506B','Regulation D 506B'),   #Naming Convention remaining
        ('Exempt Securities','Exempt Securities'),  #Naming Convention remaining
        ('75- Private Equity Securities - Simple Agreement Future Equity','75- Private Equity Securities - Simple Agreement Future Equity'),          #Naming Convention remaining
        ('Business Accelerator','Business Accelerator'), #Naming Convention remaining
        ('Business Incubator','Business Incubator'),  #Naming Convention remaining
        ('79- SBA Micro Lender','79- SBA Micro Lender'), #GOOD
    ]
    CHOICES_DP = [
        ('Less Than $25,000','Less Than $25,000'),
        ('$26,000 to $99,000','$26,000 to $99,000'),
        ('$250,000 to $499,999','$250,000 to $499,999'),
        ('$500,000 to $999,999','$500,000 to $999,999'),
        ('$1,000,000 to $1,349,999','$1,000,000 to $1,349,999'),
        ('$1,350,000 to $1,999,999','$1,350,000 to $1,999,999'),
        ('$2,000,000 to $4,999,999','$2,000,000 to $4,999,999'),
        ('$5,000,000 to $9,999,999','$5,000,000 to $9,999,999'),
        ('$10,000,000 to $19,999,999','$10,000,000 to $19,999,999'),
        ('More Than $20 Million','More Than $20 Million'),
        ("Unsure/Don't Know/TBD","Unsure/Don't Know/TBD"),
    ]     

    first_name = forms.CharField(max_length=200,required=True,label ='First Name')
    last_name = forms.CharField(max_length=200,required=True,label ='Last Name')
    company_name = forms.CharField(max_length=200,required=True,label ='Company Name')
    primary_phone = forms.CharField(max_length=200,required=True,label ='Primary Phone')
    secondary_phone = forms.CharField(max_length=200,required=False,label ='Secondary Phone',help_text='(optional)')
    alternate_phone = forms.CharField(max_length=200,required=False,label ='Alternate Phone',help_text='(optional)')
    email = forms.CharField(max_length=200,required=True,label ='Email')
    adress = forms.CharField(max_length=200,required=True,label ='Adress')
    city = forms.CharField(max_length=200,required=True,label ='City')
    state = forms.ChoiceField(choices=CHOICES_STATE,required=True,label ='Select the State:') #Make it Choice field
    zip_code = forms.CharField(max_length=200,required=True,label ='Zip code')
    cm_type = forms.ChoiceField(choices=CHOICES_CM,required=True,label ='Capital Market Type') #Make it Choice Field
    capital_amount = forms.ChoiceField(choices=CHOICES_DP,required=True,label ='How much do you invest into any singular project?')
    dyr_powder = forms.ChoiceField(choices=CHOICES_DP,required=True,label ='Available Dry Powder')
