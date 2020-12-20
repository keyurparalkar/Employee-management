from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.urls import reverse
from django.db import transaction, DatabaseError, IntegrityError
import datetime

from .models import EmpLogin, EmpDetails
from .forms import EmpDetailsForm
from .formExceptions import formFieldException

def emp_mng_view(request):
    """
    View for Managing Employee records
    """
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
    """
    View for adding employee into the database
    """
    if(request.method == "POST"):
        form = EmpDetailsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(f"CLEANDED DATA  = {cleaned_data}")
            spid = transaction.savepoint()

            
            try:
                #checks to see if email id already exists:
                all_emails = [em.emp_email for em in EmpLogin.objects.all()]
                if(cleaned_data['email'] in all_emails):
                    raise formFieldException(errors="Email ID Already Exisits")

                #save employee details
                temp_args = {  
                    'emp_fname': cleaned_data['fname'],  
                    'emp_midname': cleaned_data['midname'],  
                    'emp_lastname': cleaned_data['lastname'],  
                    'gender': cleaned_data['gender'],  
                    'dob': datetime.datetime.now(),  
                    'mob_no': cleaned_data['mob_no'],  
                    'emp_marital_stat': cleaned_data['marital_stat'],  
                    'blood_grp': cleaned_data['blood_grp']
                    }     
                #Store the email id of user
                q1 = EmpLogin(emp_email=cleaned_data["email"])
                q1.save()

                temp_args['emp_email_id'] = q1.id

                q2 = EmpDetails(**temp_args)
                q2.save()
                transaction.savepoint_commit(spid)
            
            except formFieldException as e:
                transaction.savepoint_rollback(spid)
                return render(request, "empManager/add_view.html", {'form': form, 'error_message':e.errors})
            except DatabaseError:
                transaction.savepoint_rollback(spid)
                return render(request, "empManager/add_view.html", {'form': form, 'error_message':'Database Error. Please refresh the page.'})
            except IntegrityError:
                transaction.savepoint_rollback(spid)
                return render(request, "empManager/add_view.html", {'form': form, 'error_message':'Internal Database Integrity Error. Please refresh the page.'})



            return HttpResponseRedirect(reverse("thankyou_view"))
    else:
        form = EmpDetailsForm()

    return render(request, "empManager/add_view.html", {'form': form})

def display_emp_view(request, id):
    """
    View for Displaying Employe Data
    """
    try:
        emp_info = EmpDetails.objects.get(pk=id)
        info = {'emp_info': emp_info}
    except EmpDetails.DoesNotExist:
        raise HttpResponse("Employee Details does not exists")

    return render(request, "empManager/display_details.html", info)


def thankyou_view(request):
    """
    View for Displaying thankyou page.
    """
    return render(request, "empManager/thankyou.html")

