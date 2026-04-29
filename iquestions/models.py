from django.db import models
from registration.models import UserDetail
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
#Prefered Capital Market
class IQuestions1(models.Model): # Create a UserDetail TABLE in Database
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
        ('Technical_Writer','Technical_Writer'),
        ('Content_Creator','Content_Creator'),
        ('Business_Consultant','Business_Consultant'),
        ('Marketing_Analyst','Marketing_Analyst'),
        ('Business_Plan_Writer','Business_Plan_Writer'),
        ('Business_Attorney','Business_Attorney'),
        ('Exempt Securities','Exempt Securities'),
        ('Researcher','Researcher'),
        ('Subject_Matter_Expert','Subject_Matter_Expert'),
        ('Business_Analyst','Business_Analyst'),
        ('Data_Entry','Data_Entry'),
        ('Financial_Analyst','Financial_Analyst'),
        ('Accountant','Accountant'),
        ('CPA','CPA'),
        ('Financial Modeler','Financial Modeler'),
        ('Valuation_Analyst','Valuation_Analyst'),
        ('Banker','Banker'),
        ('Web_Developer','Web_Developer'),
        ('Marketing_Consultant','Marketing_Consultant'),
        ('Transfer_Agency','Transfer_Agency'),
        ('Graphic_Designer','Graphic_Designer'),
        ('Hr_Due_Diligence','Hr_Due_Diligence'),
        ('Management_Consultant','Management_Consultant'),
        ('Hr_Consultant','Hr_Consultant'),
        ('Culture_Subject_Matter_Expert','Culture_Subject_Matter_Expert'),
        ('Broker_Agency','Broker_Agency'),
        ('Platform','Platform'),
        ('Securities_Attorney','Securities_Attorney'),
        ('Paralegal','Paralegal'),
        ('Intelectual_Property_Attorney','Intelectual_Property_Attorney'),
        ('Legal_Assistant','Legal_Assistant'),
        ('Risk_Analyst','Risk_Analyst'),
        ('Underwritter','Underwritter'),                               
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    #Added new fields for matching
    First_Name = models.CharField(blank=False,max_length=200)
    Last_Name = models.CharField(blank=False,max_length=200)
    Company_Name = models.CharField(blank=False,max_length=200)
    Primary_Phone = models.CharField(blank=False,max_length=200)
    Secondary_Phone = models.CharField(blank=False,max_length=200)
    Alternate_Phone = models.CharField(blank=False,max_length=200)
    Email = models.EmailField(blank=False,max_length=200)
    Adress = models.CharField(blank=False,max_length=200)
    City = models.CharField(blank=False,max_length=200)
    State = models.CharField(blank=False,max_length=200,choices=CHOICES_STATE)
    Zip_Code = models.CharField(blank=False,max_length=200)
    I_Type = models.CharField(blank=False,max_length=200,choices=CHOICES_CM)

    Prefered_CM = models.JSONField()
    Specialized_Industry = models.JSONField()
    Regions_Served = models.JSONField()
    Selected_Options = models.JSONField()    

    # Recording options of intermediaries in different columns for matching algorithm
    #Technical_Writer = models.IntegerField(default=0)
    #Content_Creator = models.IntegerField(default=0)
    #Business_Consultant = models.IntegerField(default=0)
    #Marketing_Analyst = models.IntegerField(default=0)
    #Business_Plan_Writer = models.IntegerField(default=0)
    #Business_Attorney = models.IntegerField(default = 0)
    #Researcher = models.IntegerField(default=0)
    #Subject_Matter_Expert = models.IntegerField(default=0)
    #Business_Analyst = models.IntegerField(default=0)
    #Data_Entry = models.IntegerField(default=0)
    #Financial_Analyst = models.IntegerField(default=0)  
    #Accountant = models.IntegerField(default=0)
    #CPA = models.IntegerField(default=0)
    #Financial_Modeler = models.IntegerField(default=0)
    #Valuation_Analyst = models.IntegerField(default=0)
    #Banker = models.IntegerField(default=0)
    #Web_Developer = models.IntegerField(default=0)
    #Marketing_Consultant = models.IntegerField(default=0)
    #Transfer_Agency = models.IntegerField(default=0)
    #Graphic_Designer = models.IntegerField(default=0)
    #Hr_Due_Diligence = models.IntegerField(default=0)
    #Management_Consultant = models.IntegerField(default=0)
    #Hr_Consultant = models.IntegerField(default=0)
    #Culture_Subject_Matter_Expert = models.IntegerField(default=0)
    #Broker_Agency = models.IntegerField(default=0)
    #Platform = models.IntegerField(default=0)
    #Securities_Attorney = models.IntegerField(default=0)
    #Paralegal = models.IntegerField(default=0)
    #Intelectual_Property_Attorney = models.IntegerField(default=0)
    #Legal_Assistant = models.IntegerField(default=0)
    #Risk_Analyst = models.IntegerField(default=0)
    #Underwritter = models.IntegerField(default=0) #Total 33 fields of expertise for now.

    def __str__(self):
        return (f'{self.user}')

#For Pricing 
class IQuestions2(models.Model):
    TYPE_CHOICES = [
        ('Hourly', 'Hourly'),
        ('Fixed Price', 'Fixed Price'),
        ('Commission', 'Commission'),
        ('Royalty', 'Royalty'),
        ('By the Project', 'By the Project'),
        ('Success Fees', 'Success Fees'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    Explanation = models.TextField(max_length=1000, blank=True, null=True)
    Rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        try:
            return f'{self.user}{self.Type} - {self.Rate}'
        
        except:
            return f'{self.Type} - {self.Rate}'
        