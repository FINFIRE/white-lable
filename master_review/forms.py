from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.order_by('-id'),
        label="Select User",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class manualCapitalTypeform(forms.Form):
    C_TYPES =[
        ('Accelerator', 'Accelerator'),
        ('Bonds','Bonds'),
        ('Bootstrapped','Bootstrapped'),
        ('Commercial Banking','Commercial Banking'),
        ('Cryptocurrency','Cryptocurrency'),
        ('Factoring','Factoring'),
        ('Grants','Grants'),
        ('Hedge Funds','Hedge Funds'),
        ('Incubator','Incubator'),
        ('Investment Banking','Investment Banking'),
        ('Private Debt','Private Debt'),
        ('Private Equity Securities','Private Equity Securities'),
        ('Royalty Financing','Royalty Financing'),
        ('Small Business Administration (SBA)','Small Business Administration (SBA)'),
        ('Third Party Corporate Credit','Third Party Corporate Credit'),
        ('Tokenization','Tokenization'),
        ('Venture Capital','Venture Capital'),
    ]    

    rankone = forms.ChoiceField(choices=C_TYPES,label="Rank 1st")
    ranktwo = forms.ChoiceField(choices=C_TYPES,label="Rank 2nd")
    rankthree = forms.ChoiceField(choices=C_TYPES,label="Rank 3rd")
    rankfour = forms.ChoiceField(choices=C_TYPES,label="Rank 4th")
    rankfive = forms.ChoiceField(choices=C_TYPES,label="Rank 5th")
    status = forms.BooleanField(required=False,label=mark_safe("<strong>Do you want manual capital assignment to the selected user?(check mark for yes)</strong>"))
