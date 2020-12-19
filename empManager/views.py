from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import EmpLogin, EmpDetails

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
    return HttpResponse("This is Add Employee Django view!!!!!")

def display_emp_view(request, id):
    try:
        emp_info = EmpDetails.objects.get(pk=id)
        info = {'emp_info': emp_info}
    except EmpDetails.DoesNotExist:
        raise HttpResponse("Employee Details does not exists")

    return render(request, "empManager/display_details.html", info)
