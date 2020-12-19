from django.shortcuts import render
from django.http import HttpResponse
from .models import EmpLogin, EmpDetails

# Create your views here.
def emp_mng_view(request):
    x, y = EmpLogin.objects.all(), EmpDetails.objects.all()
    data = {
        'emp_emails':[i.emp_email for i in x],
        'emp_details':[i for i in y]   
    }
    print(f"Data = {data['emp_details'][0] }")
    return render(request, 'empManager/index.html', data)

def add_emp_view(request):
    return HttpResponse("This is Add Employee Django view!!!!!")

def view_emp_view(request):
    return HttpResponse("This is View Employee Django view!!!!!")
