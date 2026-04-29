from django import forms
from .models import UserDetail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

#Creating a forrm based on model
class RegistrationFormInitial(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes or classes for JavaScript targeting
        self.fields['password1'].widget.attrs.update({
            'class': 'password-validation',
            'hx-post': '',  # For HTMX if you're using it
            'hx-trigger': 'keyup changed delay:500ms',
            'hx-target': '#password-errors'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'password-confirmation',
            'hx-post': '',  # For HTMX
            'hx-trigger': 'keyup changed delay:500ms',
            'hx-target': '#password-confirmation-errors'
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered. Please use a different email.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        # You can add additional password validation here
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match")
        
        return cleaned_data  

class RegistrationFormOne(forms.Form):
    First_Name = forms.CharField(max_length=200,label="Fill in: First Name")
    Middle_Name = forms.CharField(max_length=200,required=False,label="Fill in: Middle Name")
    Last_Name = forms.CharField(max_length=200,label="Fill in: Last Name")
    CHOICES = [
        ('Advisory Board Member','Advisory Board Member'),
        ('Board Member','Board Member'),
        ('Business Finance Representative','Business Finance Representative'),
        ('Capital Market Representative','Capital Market Representative'),
        ('Consultant','Consultant'),
        ('Director','Director'),
        ('Entrepreneur','Entrepreneur'),
        ('Executive Officer','Executive Officer'),
        ('Founder','Founder'),
        ('Intermediary','Intermediary'),
        ('Other','Other'),
        ('Owner','Owner'),
        ('Responsible for Financial Matters','Responsible for Financial Matters'),
    ]
    Affiliation = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES,label=mark_safe("<b>Affiliation with the Company (Choose All That Apply)</b>")) # This field would store all selected kinds of affiliations
    User_Email = forms.EmailField(label="Fill in: Primary Email Address")
    Company_Website = forms.CharField(max_length=200,required=False,label='Fill in: Company Website Domain')
    Business_Adress = forms.CharField(max_length=200, label= 'Fill in: Primary Business Address')
    Business_Phone = forms.CharField(
        max_length=200,
        label='Fill in: Business Phone Number',
        widget=forms.TextInput(attrs={'id': 'business-phone'})
    )
    Mobile_Phone = forms.CharField(
        max_length=200,
        label='Fill in: Mobile Phone Number',
        widget=forms.TextInput(attrs={'id': 'mobile-phone'})
    )
    CHOICES2 = [
        ('Minority Owned Business','Minority Owned Business'),
        ('Veteran Owned Business','Veteran Owned Business'),
        ('Woman Owned Business', 'Woman Owned Business'),
        ('Tax Benefit Business (Opportunity Zone/Other)','Tax Benefit Business (Opportunity Zone/Other)'),
    ]
    Special_Programs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES2,required = False,label=mark_safe("<b>Special Program Qualifications</b>"))

class RegistrationFormTwo(forms.Form):
    CHOICES = [
        #('Capital Market','Capital Market'),
        ('Enterprise/Business','Enterprise/Business'),
        #('Intermediary','Intermediary'),
    ]

    CHOICES2 = [
        ('Consultant and/or Intermediary Seeking Leads & Providing Advice','Consultant and/or Intermediary Seeking Leads & Providing Advice'),
        ('Cost to Package the Right Capital Type to the Situation','Cost to Package the Right Capital Type to the Situation'),
        ('Education - Learn the Capital Markets & Capital Types Available','Education - Learn the Capital Markets & Capital Types Available'),
        ('I Don’t Know - TBD','I Don’t Know - TBD'),
        ('Identify Documents Required for the Most Probable Capital Type','Identify Documents Required for the Most Probable Capital Type'),
        ('Information - Match the Right Capital to the Situation','Information - Match the Right Capital to the Situation'),
        ('Introductions to Capital Sources Currently Funding','Introductions to Capital Sources Currently Funding'),
        ('Introductions to Qualified Companies Seeking Capital','Introductions to Qualified Companies Seeking Capital'),
        ('Timeline to Capital','Timeline to Capital'),        

    ]
    #CHOICES3 = [
    #    ('Silver',mark_safe('Silver  <span class="tooltip">ℹ️<span class="tooltip-text">The silver package is $199 per month, which includes creation of the data room for the enterprise to save their documents that will be shared with the matches. The silver package includes six matches at no additional charge per month. A discount is applied if the fee is paid in advance, a flat fee of $1,999 paid in advance for 12 months, which includes up to 80 introductions.</span></span>')),
    #    ('Gold',mark_safe('Gold <span class="tooltip">ℹ️<span class="tooltip-text">The gold package is $499 per month which includes the creation of the data room for the enterprise to save their documents to be shared with the matches. The Gold Package includes twelve introductions per month. In addition, Gold Enterprises receive up to two hours of consultation for either (1) Capital Marketing Services (Personal introductions to Capital sources via conference calls or zoom), or, (2) Two hours of business finance document creation (Valuations, pro forma work, 1- page tear sheet, 10-minute podcast, and/or Business model Canvas). If paid in advance for 12 months, the upfront fee is $5,000 (Saving $1,000). The gold package includes up to 200 introductions at no additional cost.</span></span>')),
    #    ('Platinum',mark_safe('Platinum <span class="tooltip">ℹ️<span class="tooltip-text">The platinum package is only available when paid annually. The annual fee is $10,000. The platinum package includes everything from the Gold package plus up to 400 market introductions annually.</span></span>'))
    #]    
    Account_Type = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,label=mark_safe("<b>Choose Account Type</b>"))
    Primary_Purpose = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES2,label=mark_safe("<b>The Primary Purpose of Using the FINFIRE App (Choose All That Apply)</b>"))
    #Billing_Option = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES3,label=mark_safe("<b>Billing Options (Choose One)</b>"))   
