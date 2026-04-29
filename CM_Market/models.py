from typing import Any
from django.db import models
from registration.models import UserDetail
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your models here.
class VQuestion1(models.Model):
    class Meta:
        verbose_name = "Capital Markets Database"
        verbose_name_plural = "Capital Markets Database" 

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
        ('66- Private Equity Securities - Regulation CF Tittle III','66- Private Equity Securities - Regulation CF Tittle III'),
        ('65- Private Equity Securities - Regulation A','65- Private Equity Securities - Regulation A'), #GOOD
        ('1- Private Equity','1- Private Equity'),
        ('77- Small Business Administration (SBA) - SBA 504B','77- Small Business Administration (SBA) - SBA 504B'), #GOOD
        ('21- Commercial Banking - Line of Credit','21- Commercial Banking - Line of Credit'),
        ('Regulation D 506B','Regulation D 506B'),   #Naming Convention remaining
        ('Exempt Securities','Exempt Securities'),  #Naming Convention remaining
        ('75- Private Equity Securities - Simple Agreement Future Equity','75- Private Equity Securities - Simple Agreement Future Equity'),          #Naming Convention remaining
        ('Business Accelerator','Business Accelerator'), #Naming Convention remaining
        ('Business Incubator','Business Incubator'),  #Naming Convention remaining
        ('79- Small Business Administration (SBA) - SBA Micro Lender','79- Small Business Administration (SBA) - SBA Micro Lender'), #GOOD
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

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
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
    CM_Type = models.CharField(blank=False,max_length=200,choices=CHOICES_CM)
    Capital_Amount = models.CharField(max_length=200,choices=CHOICES_DP,null=True,blank=False)
    Dry_Powder = models.CharField(max_length=200,choices=CHOICES_DP,default=None,null=True,blank=False)
    #Added amount of capital,Dry Powder,Fees

    def __str__(self):
        return f'{self.First_Name} from {self.Company_Name}'