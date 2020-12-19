from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_mng_view(request):

    return HttpResponse("Hello world this is Employee Management page !!!")

def add_emp_view(request):
    return HttpResponse("This is Add Employee Django view!!!!!")

def view_emp_view(request):
    return HttpResponse("This is View Employee Django view!!!!!")
