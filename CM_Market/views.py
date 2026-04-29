from django.shortcuts import render,redirect,get_object_or_404
from .forms import VQuestion1Form
from .models import VQuestion1,UserDetail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def vquestion1_form(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = VQuestion1.objects.get(user=request.user)

        initial_data = {
            'user':request.user,
            'first_name': response.First_Name,
            'last_name':response.Last_Name,
            'company_name':response.Company_Name,
            'primary_phone': response.Primary_Phone,
            'secondary_phone':response.Secondary_Phone,
            'alternate_phone':response.Alternate_Phone,
            'email':response.Email,
            'adress':response.Adress,
            'city':response.City,
            'state':response.State,
            'zip_code':response.Zip_Code,
            'cm_type':response.CM_Type,
        }
    except VQuestion1.DoesNotExist:
        response = VQuestion1(user=request.user)
        initial_data = {}
    #user_id = request.session.get('user_id') I think this code is not required now, I must have missed to remove it. 

    if request.method == 'POST':
        form = VQuestion1Form(request.POST)
        if form.is_valid():
            response.user=request.user
            response.First_Name=form.cleaned_data['first_name']
            response.Last_Name=form.cleaned_data['last_name']
            response.Company_Name=form.cleaned_data['company_name']
            response.Primary_Phone=form.cleaned_data['primary_phone']
            response.Secondary_Phone=form.cleaned_data['secondary_phone']
            response.Alternate_Phone=form.cleaned_data['alternate_phone']
            response.Email=form.cleaned_data['email']
            response.Adress = form.cleaned_data['adress']
            response.City = form.cleaned_data['city']
            response.State = form.cleaned_data['state']
            response.Zip_Code =form.cleaned_data['zip_code']
            response.CM_Type  = form.cleaned_data['cm_type']
            response.Capital_Amount = form.cleaned_data['capital_amount']
            response.Dry_Powder = form.cleaned_data['dry_powder']
            response.save()            
            return redirect('home')  # Redirect to a success page or another page
    else:
        form = VQuestion1Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'forms.html', context)



