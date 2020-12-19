from django import forms
from django.core import validators

from .models import EmpDetails

class EmpDetailsForm(forms.Form):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    MSTAT_CHOICES = (('Married', 'Married'),('Single', 'Single'),)
    email = forms.CharField(label="Email ID",required=True, validators=[validators.EmailValidator()])
    fname = forms.CharField(label="Employee First Name", max_length=256,required=True)
    midname = forms.CharField(label="Employee Middle Name",max_length=256,required=True)
    lastname = forms.CharField(label="Employee Last Name",max_length=256,required=True)
    gender = forms.ChoiceField(label="Gender",widget=forms.Select, choices=GENDER_CHOICES,required=True)
    dob = forms.DateInput()
    mob_no = forms.CharField(label="Mobile Number",max_length=10,required=True,
     validators=[validators.RegexValidator(regex='\d{10}',message="Enter a valid 10 digit Mobile Number")])
    alt_mob_no = forms.CharField(label="Alternate Mobile Number(Optional)",max_length=10,required=False)
    marital_stat = forms.ChoiceField(label="Marital Status", widget=forms.Select,choices=MSTAT_CHOICES,required=True)
    blood_grp = forms.CharField(label="Blood Group", max_length=5,required=True)
