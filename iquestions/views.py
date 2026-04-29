from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import IQuestions1Form,IQuestions2Form
from .models import IQuestions1,UserDetail,IQuestions2
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def iquestion1_form(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = IQuestions1.objects.get(user=request.user)

        initial_data = {
            'user':request.user,
            'prefered_cm': response.Prefered_CM,
            'specialized_industry':response.Specialized_Industry,
            'regions_served': response.Regions_Served,
            'intermediaries_expertise':response.Selected_Options,
        }
    except IQuestions1.DoesNotExist:
        response = IQuestions1(user=request.user)
        initial_data = {}
    if request.method == 'POST':
        form = IQuestions1Form(request.POST)
        if form.is_valid():
            selected_options_list = form.cleaned_data['intermediaries_expertise']

            # Create a dictionary to hold the values
            option_values = {
                'option1': 0,
                'option2': 0,
                'option3': 0,
                'option4': 0,
                'option5': 0,
                'option6': 0,
                'option7': 0,
                'option8': 0,
                'option9': 0,
                'option10': 0,
                'option11': 0,
                'option12': 0,
                'option13': 0,
                'option14': 0,
                'option15': 0,
                'option16': 0,
                'option17': 0,
                'option18': 0,
                'option19': 0,
                'option20': 0,
                'option21': 0,
                'option22': 0,
                'option23': 0,
                'option24': 0,
                'option25': 0,
                'option26': 0,
                'option27': 0,
                'option28': 0,
                'option29': 0,
                'option30': 0,
                'option31': 0,
                'option32': 0,
                'option33': 0,
            }
            #Set the seleceted options to 1
            for selected_option in selected_options_list:
                option_values[selected_option] =1
            
            response.user=request.user
            response.Prefered_CM=form.cleaned_data['prefered_cm']
            response.Specialized_Industry=form.cleaned_data['specialized_industry']
            response.Regions_Served = form.cleaned_data['regions_served']
            response.Technical_Writer = option_values['option1']
            response.Content_Creator = option_values['option2']
            response.Business_Consultant =option_values['option3']
            response.Marketing_Analyst = option_values['option4']
            response.Business_Plan_Writer = option_values['option5']
            response.Business_Attorney = option_values['option6']
            response.Researcher = option_values['option7']
            response.Subject_Matter_Expert = option_values['option8']
            response.Business_Analyst = option_values['option9']
            response.Data_Entry = option_values['option10']
            response.Financial_Analyst = option_values['option11']
            response.Accountant = option_values['option12']
            response.CPA = option_values['option13']
            response.Financial_Modeler = option_values['option14']
            response.Valuation_Analyst = option_values['option15']
            response.Banker = option_values['option16']
            response.Web_Developer = option_values['option17']
            response.Marketing_Consultant = option_values['option18']
            response.Transfer_Agency = option_values['option19']
            response.Graphic_Designer = option_values['option20']
            response.Hr_Due_Diligence = option_values['option21']
            response.Management_Consultant = option_values['option22']
            response.Hr_Consultant = option_values['option23']
            response.Culture_Subject_Matter_Expert = option_values['option24']
            response.Broker_Agency = option_values['option25']
            response.Platform = option_values['option26']
            response.Securities_Attorney = option_values['option27']
            response.Paralegal = option_values['option28']
            response.Intelectual_Property_Attorney = option_values['option29']
            response.Legal_Assistant = option_values['option30']
            response.Risk_Analyst = option_values['option31']
            response.Underwritter = option_values['option32']
            response.Selected_Options = selected_options_list
            response.save()

            
            return redirect('iquestion2')  # Redirect to a success page or another page
    else:
        form = IQuestions1Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'forms.html', context)

@login_required
def iquestion2_form(request):
    # Retrieve the existing survey response for the logged-in user
    try:
        response = IQuestions2.objects.get(user=request.user)

        initial_data = {
            'user':request.user,
            'pay_type': response.Type,
            'explanation':response.Rate,
            'rate': response.Rate,
        }
    except IQuestions2.DoesNotExist:
        response = IQuestions2(user=request.user)
        initial_data = {}

    if request.method == 'POST':
        form = IQuestions2Form(request.POST)
        if form.is_valid():
            response.user = request.user
            response.Type = form.cleaned_data['pay_type']
            response.Explanation = form.cleaned_data['explanation']
            response.Rate = form.cleaned_data['rate']
            response.save()
            return redirect('home')
    else:
        form = IQuestions2Form(initial=initial_data)

    context = {'form': form}
    return render(request, 'forms.html', context)
        
