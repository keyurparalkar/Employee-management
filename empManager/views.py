from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.urls import reverse

from .models import EmpLogin, EmpDetails
from .forms import EmpDetailsForm

# Create your views here.
def emp_mng_view(request):
    try:
        data = {
            'emp_emails':[i.emp_email for i in EmpLogin.objects.all()],
            'emp_details':[i for i in EmpDetails.objects.all()]   
        }
    except EmpLogin.DoesNotExist:
        raise Http404("Employee Login does not exists")
    except EmpDetails.DoesNotExist:
        raise Http404("Employee Details not found")
    
    return render(request, 'empManager/index.html', data)

def add_emp_view(request):
    if(request.method == "POST"):
        form = EmpDetailsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(f"CLEANDED DATA  = {cleaned_data}")
            return HttpResponseRedirect(reverse("thankyou_view"))
    else:
        form = EmpDetailsForm()

    return render(request, "empManager/add_view.html", {'form': form})

def thankyou_view(request):
    return render(request, "empManager/thankyou.html")

def display_emp_view(request, id):
    try:
        emp_info = EmpDetails.objects.get(pk=id)
        info = {'emp_info': emp_info}
    except EmpDetails.DoesNotExist:
        raise HttpResponse("Employee Details does not exists")

    return render(request, "empManager/display_details.html", info)
