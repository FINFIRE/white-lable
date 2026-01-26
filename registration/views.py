from django.shortcuts import render, redirect
from .forms import RegistrationFormOne, RegistrationFormTwo ,RegistrationFormInitial
from .models import UserDetail, UserDetail2
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from iquestions.models import IQuestions1,IQuestions2
from CM_Market.models import VQuestion1
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from django.contrib.auth.models import User
from django.core.mail import send_mail # is required if we are sending email confirmation during registration from prototype, currently we are not using it.
from django.utils.http import  urlsafe_base64_decode
from django.utils.encoding import  force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.authtoken.models import Token

def home(request):
    try:
        response = UserDetail2.objects.get(user=request.user) #tried to redirect to different link but for now this works
        if response.Account_Type == 'Capital Market':
            link = 'registration_form_view'
        elif response.Account_Type == 'Enterprise/Business':
            link = 'registration_form_view'
        else:
            link = 'registration_form_view'    
    except:
        link = 'registration_form_view'


    
    return render (request,'index.html',{'link':link})

def register(request):
    if request.method == 'POST':
        form = RegistrationFormInitial(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active=True
            user.save()
            
            # Code are hashed here as we are not sending email verification to users from prototype
            #create token
            #token = default_token_generator.make_token(user)
            #uid = urlsafe_base64_encode(force_bytes(user.pk))
            #current_site = get_current_site(request)
            #verification_link = reverse('activate',kwargs={'uidb64': uid, 'token': token})
            #activate_url = f'http://{current_site.domain}{verification_link}'

            #send email
            #email_subject = 'Activate Your Account'
            #email_body = render_to_string('email_verification.html',{
            #    'user':user,
            #    'activate_url':activate_url
            #})
            #send_mail(email_subject, email_body, 'romin8985@gmail.com', [user.email])            
            login(request,user)
            return redirect('home')
    else:
        form = RegistrationFormInitial()

    return render(request,'registration1.html',{'form':form})

# No test created for activate as it is not in use
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        # Generate or get the user's token
        #token_obj, created = Token.objects.get_or_create(user=user)
        # Redirect to your frontend with the token as a query parameter
        #frontend_url = f"https://finfireapp.flutterflow.app/dashboard?token={token_obj.key}"
        #return redirect(frontend_url)
    else:
        return HttpResponse("Activation link is invalid.")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(home)
    else:
        form = AuthenticationForm()
    return render (request,'login.html',{'form':form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login_view')

@login_required
def registration_form_view(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = UserDetail.objects.get(user=request.user)
        initial_data = {
            'user':request.user,
            'First_Name':response.First_Name,
            'Middle_Name': response.Middle_Name,
            'Last_Name':response.Last_Name,
            'Affiliation':response.Affiliation,
            'User_Email':response.User_Email,
            'Company_Website':response.Company_Website,
            'Business_Adress': response.Business_Adress,
            'Business_Phone':response.Business_Phone,
            'Mobile_Phone':response.Mobile_Phone,
            'Special_Programs':response.Special_Programs,
        }
    except UserDetail.DoesNotExist:
        response = UserDetail(user=request.user)
        initial_data = {
            'User_Email':request.user.email,
        }

    if request.method == 'POST':
        form = RegistrationFormOne(request.POST)
        if form.is_valid():
            # Save the form data to the model
            first_name = form.cleaned_data['First_Name']
            middle_name = form.cleaned_data['Middle_Name']
            last_name = form.cleaned_data['Last_Name']
            affiliation = form.cleaned_data['Affiliation']
            user_email = form.cleaned_data['User_Email']
            company_website = form.cleaned_data['Company_Website']
            business_adress = form.cleaned_data['Business_Adress']
            business_phone = form.cleaned_data['Business_Phone']
            mobile_phone = form.cleaned_data['Mobile_Phone']
            special_programs = form.cleaned_data['Special_Programs']
            
            response.user = request.user
            response.First_Name=first_name
            response.Middle_Name=middle_name
            response.Last_Name=last_name
            response.Affiliation=affiliation
            response.User_Email=user_email
            response.Company_Website=company_website
            response.Business_Adress=business_adress
            response.Business_Phone=business_phone
            response.Mobile_Phone=mobile_phone
            response.Special_Programs=special_programs
            response.save()
            
            return redirect('registration_form_view2')  # Use the name of the view or URL pattern name
    
    else:
        form = RegistrationFormOne(initial=initial_data)

    context = {'form': form}
    return render(request, 'forms.html', context)

@login_required
def registration_form_view2(request):
    try:
        response = UserDetail2.objects.get(user=request.user)
        initial_data = {
            'user':request.user,
            'Account_Type':response.Account_Type,
            'Primary_Purpose': response.Primary_Purpose,
            #'Billing_Option':response.Billing_Option,
        }
    except UserDetail2.DoesNotExist:
        response = UserDetail2(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = RegistrationFormTwo(request.POST)
        if form.is_valid():
            # Save the form data to the model
            account_type = form.cleaned_data['Account_Type']
            primary_purpose = form.cleaned_data['Primary_Purpose']
            #billing_option = form.cleaned_data['Billing_Option']
            
            response.user = request.user
            response.Account_Type=account_type

            # to handle a bug for duplicate responses when user can have data for intermediary,enterprise and Capital market
            if account_type == 'Enterprise/Business':
                try:
                    IQuestions1.objects.filter(user=request.user).delete()
                    IQuestions2.objects.filter(user=request.user).delete()
                    VQuestion1.objects.filter(user=request.user).delete()

                except (IQuestions1.DoesNotExist,VQuestion1.DoesNotExist,IQuestions2.DoesNotExist):
                    pass

            if account_type == 'Capital Market':
                try:
                    IQuestions1.objects.filter(user=request.user).delete()
                    IQuestions2.objects.filter(user=request.user).delete()
                    EQuestions.objects.filter(user=request.user).delete()
                    EQuestions1.objects.filter(user=request.user).delete()
                    EQuestions2.objects.filter(user=request.user).delete()
                    EQuestions3.objects.filter(user=request.user).delete()
                    EQuestions4.objects.filter(user=request.user).delete()
                    EQuestions5.objects.filter(user=request.user).delete()
                    EQuestions6.objects.filter(user=request.user).delete()
                    EQuestions7.objects.filter(user=request.user).delete()
                    EQuestions8.objects.filter(user=request.user).delete()
                    EQuestions9.objects.filter(user=request.user).delete()
                    EQuestions10.objects.filter(user=request.user).delete()
                    EQuestions11.objects.filter(user=request.user).delete()
                    EQuestions12.objects.filter(user=request.user).delete()
                    EQuestions13.objects.filter(user=request.user).delete()
                    EQuestions14.objects.filter(user=request.user).delete()
                    DocumentsPrepared.objects.filter(user=request.user).delete()

                except (
                    IQuestions1.DoesNotExist,
                    IQuestions2.DoesNotExist,
                    EQuestions1.DoesNotExist,
                    EQuestions2.DoesNotExist,
                    EQuestions3.DoesNotExist,
                    EQuestions4.DoesNotExist,
                    EQuestions5.DoesNotExist,
                    EQuestions6.DoesNotExist,
                    EQuestions7.DoesNotExist,
                    EQuestions8.DoesNotExist,
                    EQuestions9.DoesNotExist,
                    EQuestions10.DoesNotExist,
                    EQuestions11.DoesNotExist,
                    EQuestions12.DoesNotExist,
                    EQuestions13.DoesNotExist,
                    EQuestions14.DoesNotExist,
                    EQuestions.DoesNotExist,
                    DocumentsPrepared.DoesNotExist,
                    ):
                    pass

            if account_type == 'Intermediary':
                try:
                    VQuestion1.objects.filter(user=request.user).delete()
                    EQuestions.objects.filter(user=request.user).delete()
                    EQuestions1.objects.filter(user=request.user).delete()
                    EQuestions2.objects.filter(user=request.user).delete()
                    EQuestions3.objects.filter(user=request.user).delete()
                    EQuestions4.objects.filter(user=request.user).delete()
                    EQuestions5.objects.filter(user=request.user).delete()
                    EQuestions6.objects.filter(user=request.user).delete()
                    EQuestions7.objects.filter(user=request.user).delete()
                    EQuestions8.objects.filter(user=request.user).delete()
                    EQuestions9.objects.filter(user=request.user).delete()
                    EQuestions10.objects.filter(user=request.user).delete()
                    EQuestions11.objects.filter(user=request.user).delete()
                    EQuestions12.objects.filter(user=request.user).delete()
                    EQuestions13.objects.filter(user=request.user).delete()
                    EQuestions14.objects.filter(user=request.user).delete()
                    DocumentsPrepared.objects.filter(user=request.user).delete()

                except (
                    VQuestion1.DoesNotExist,
                    EQuestions.DoesNotExist,
                    EQuestions1.DoesNotExist,
                    EQuestions2.DoesNotExist,
                    EQuestions3.DoesNotExist,
                    EQuestions4.DoesNotExist,
                    EQuestions5.DoesNotExist,
                    EQuestions6.DoesNotExist,
                    EQuestions7.DoesNotExist,
                    EQuestions8.DoesNotExist,
                    EQuestions9.DoesNotExist,
                    EQuestions10.DoesNotExist,
                    EQuestions11.DoesNotExist,
                    EQuestions12.DoesNotExist,
                    EQuestions13.DoesNotExist,
                    EQuestions14.DoesNotExist,
                    DocumentsPrepared.DoesNotExist,
                    ):
                    pass

            response.Primary_Purpose=primary_purpose
            #response.Billing_Option=billing_option
            response.save()
            
            if account_type == 'Capital Market':
                return redirect('vquestion1')
            
            elif account_type == 'Enterprise/Business':
                return redirect('equestion1')
            
            else:
                return redirect('iquestion1')
        

    else:
        form = RegistrationFormTwo(initial=initial_data)     

    context = {'form': form}
    return render(request, 'accountsetup.html', context)
