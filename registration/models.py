from django.db import models
from django.contrib.auth.models import User 

from django.contrib.auth.models import AbstractUser
from django.db import models

# Creat your models here.
class UserDetail(models.Model): # Create a UserDetail TABLE in Database
    class Meta:
        verbose_name = "A. Contact Information (UserDetails)"
        verbose_name_plural = "A. Contact Information (UserDetails)"

    CHOICES = [
        ('Advisory Board member','Advisory Board member'),
        ('Board member','Board member'),
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

    CHOICES2 = [
        ('Minority Owned Business','Minority Owned Business'),
        ('Veteran Owned Business','Veteran Owned Business'),
        ('Woman Owned Business', 'Woman Owned Business'),
        ('Tax Benefit Business (Opportunity Zone/Other)','Tax Benefit Business (Opportunity Zone/Other)'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    First_Name = models.CharField(max_length=200)
    Middle_Name = models.CharField(max_length=200,blank=True)
    Last_Name = models.CharField(max_length=200)
    Affiliation = models.JSONField(blank=True,default=list,help_text="Leave this blank as it may cause error.") # This field would store all selected kinds of affiliations
    User_Email = models.EmailField()
    Company_Website = models.CharField(max_length=200,blank=True)
    Business_Adress = models.CharField(blank=True,max_length=200)
    Business_Phone = models.CharField(blank=True,max_length=200)
    Mobile_Phone = models.CharField(blank=True,max_length=200)
    Special_Programs = models.JSONField(null=False,blank=True,default=dict,help_text="Leave this blank as it may cause error.")

    def __str__(self):
        return (f'{self.user}')

class UserDetail2(models.Model):
    class Meta:
        verbose_name = "B. Account Setup (UserDetails2)"
        verbose_name_plural = "B. Account Setup (UserDetails2)"

    CHOICES = [
        ('Capital Market','Capital Market'),
        ('Enterprise/Business','Enterprise/Business'),
        ('Intermediary','Intermediary'),
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

    CHOICES3 = [
        ('Silver','Silver'),
        ('Gold','Gold'),
        ('Platinum','Platinum')
    ]    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Account_Type = models.CharField(max_length=200,choices=CHOICES)
    Primary_Purpose = models.JSONField(blank=True,default=dict,choices=CHOICES2,help_text="Leave this blank as it may cause error.") #This field would store all selected reasons of using FINFIRE
    Billing_Option = models.CharField(blank=True,max_length=200,choices=CHOICES3)

    def __str__(self):
        return (f'{self.user} : {self.Billing_Option}')    