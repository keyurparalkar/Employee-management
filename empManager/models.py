from django.db import models

'''
Models for managing Employee data
'''

class EmpLogin(models.Model):
    emp_email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.emp_email

class EmpDetails(models.Model):
    emp_email = models.ForeignKey(EmpLogin, on_delete=models.CASCADE)
    emp_fname = models.CharField(max_length=256)
    emp_midname = models.CharField(max_length=256)
    emp_lastname = models.CharField(max_length=256)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    mob_no = models.CharField(max_length=10)
    alt_mob_no = models.CharField(max_length=10)
    emp_marital_stat = models.CharField(max_length=10)
    blood_grp = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.emp_fname} \t {self.emp_lastname} \t {self.emp_email}'