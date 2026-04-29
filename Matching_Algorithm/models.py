from django.db import models
from django.contrib.auth.models import User


class allCapitalMatchValues(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    percentage = models.JSONField(default=dict)

    def __str__(self):
        return (f'{self.user} : {self.percentage}')


class Capital_Matches(models.Model): 
    class Meta:
        verbose_name = "Capital Match Percentages"
        verbose_name_plural = "Capital Match Percentages"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    RCF_1 = models.FloatField(default=0, verbose_name="Regulation Crowdfunding")
    RAP_2 = models.FloatField(default=0, verbose_name="Regulation A+")
    PE_3 = models.FloatField(default=0, verbose_name="Private Equity")
    SBA_504B_4 = models.FloatField(default=0, verbose_name="SBA 504(b) Loan")
    LOCACD_5 = models.FloatField(default=0, verbose_name="Line of Credit - Accounts Receivable")
    RD_506B_6 = models.FloatField(default=0, verbose_name="Regulation D 506(b)")
    ES_7 = models.FloatField(default=0, verbose_name="Equity Shares")
    S_SAFE_8 = models.FloatField(default=0, verbose_name="Simple Agreement for Future Equity (SAFE)")
    BA_9 = models.FloatField(default=0, verbose_name="Bank Financing")
    BI_10 = models.FloatField(default=0, verbose_name="Bond Issuance")
    SBAML_11 = models.FloatField(default=0, verbose_name="Small Business Administration Microloan")

    def __str__(self):
        return f"{self.user}"

class Matches_Purchased(models.Model):
    class Meta:
        verbose_name = "Purchased number of matches"
        verbose_name_plural = "Purchased number of matches"      
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_matches = models.TextField(max_length=3000)
    total_num = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    balance_due = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    match_id_cm = models.JSONField(default=list)
    match_id_i = models.JSONField(default=list)


    def __str__(self):
        return (f'{self.user}')    

class Letter_Response(models.Model):
    class Meta:
        verbose_name = "JSON output for fields required in letter"
        verbose_name_plural = "JSON output for fields required in letter"    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255,default='')
    lastname = models.CharField(max_length=255,default='')
    address = models.CharField(max_length=255,default='')
    phone = models.CharField(max_length=255,default='')
    email = models.EmailField()
    businessname = models.CharField(max_length=255,default='')
    count = models.CharField(max_length=255,default='')
    fundgoal = models.CharField(max_length=255,default='')
    totalnum = models.IntegerField(default=0)
    cm1name = models.CharField(max_length=255,default='')
    cm2name = models.CharField(max_length=255,default='')
    cm3name = models.CharField(max_length=255,default='')
    cm4name = models.CharField(max_length=255,default='')
    cm5name = models.CharField(max_length=255,default='')
    cm6name = models.CharField(max_length=255,default='')
    cm1no = models.IntegerField(default=0)
    cm2no = models.IntegerField(default=0)
    cm3no = models.IntegerField(default=0)
    cm4no = models.IntegerField(default=0)
    cm5no = models.IntegerField(default=0)
    cm6no = models.IntegerField(default=0)
    intermediaries = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    totalprice = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    balancedue = models.IntegerField(default=0)
    top_6_name = models.JSONField()
    top_6_name_output = models.JSONField()
    infocm1 = models.TextField(max_length=100000,default='')
    infocm2 = models.TextField(max_length=100000,default='')
    infocm3 = models.TextField(max_length=100000,default='')
    infocm4 = models.TextField(max_length=100000,default='')
    infocm5 = models.TextField(max_length=100000,default='')
    infocm6 = models.TextField(max_length=100000,default='')

    def __str__(self):
        return (f'{self.user} : {self.cm1name} : {self.cm2name} : {self.cm3name}') 

class Purchases(models.Model):
    class Meta:
        verbose_name = "Purchased number of matches"
        verbose_name_plural = "Purchased number of matches"     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cm1purchase = models.IntegerField(default=0)
    cm2purchase = models.IntegerField(default=0)
    cm3purchase = models.IntegerField(default=0)
    cm4purchase = models.IntegerField(default=0)
    cm5purchase = models.IntegerField(default=0)
    cm6purchase = models.IntegerField(default=0)
    ipurchase = models.IntegerField(default=0)
    cm_matches = models.JSONField(default=list)
    


    def __str__(self):
        return (f'{self.user}')    
