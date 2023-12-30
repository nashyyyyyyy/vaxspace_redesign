from django.db import models
from operator import mod
from django.utils import timezone
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Barangay(models.Model):
    name = models.CharField(max_length = 100)
    healthworker = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



class Vaccine(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    dose1 = models.BooleanField(null=True)
    dose2 = models.BooleanField(null=True)
    dose3 = models.BooleanField(null=True)
    created = models.DateTimeField(default=timezone.now)
    recommended_age1 = models.CharField(max_length=50, null=True) 
    recommended_age2 = models.CharField(max_length=50, null=True) 
    recommended_age3 = models.CharField(max_length=50, null=True) 

    def __str__(self):
        return self.name

class Register(models.Model):

    child_name = models.CharField(max_length = 100,null=True)       
    date_of_birth = models.DateField(null=True)     
    place_of_birth = models.CharField(max_length = 100,null=True)  
    address = models.ForeignKey(Barangay, null=True, on_delete=models.CASCADE) 
    contact = models.IntegerField(null=True)  
    mother_name = models.CharField(max_length = 100,null=True)       
    father_name = models.CharField(max_length = 100 , null=True)   
    birth_height = models.IntegerField(null=True) 
    birth_weight = models.IntegerField(null=True) 
    sex = models.CharField(max_length = 10, null=True)
    added_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.child_name

class Vaccine_record(models.Model):
    child = models.ForeignKey(Register, null=True, on_delete=models.SET_NULL)
    vax1 = models.IntegerField(null=True)
    vax1_info = models.TextField(null=True)
    vax2 = models.IntegerField(null=True)
    vax2_info = models.TextField(null=True)
    vax3 = models.IntegerField(null=True)
    vax3_info = models.TextField(null=True)
    vaccination_date = models.DateTimeField()
    date_of_birth = models.TextField(null=True)     
    prev_birth_weight = models.IntegerField(null=True)
    prev_birth_height = models.IntegerField(null=True)
    remarks = models.TextField(default=None)

class Schedule(models.Model):
    child = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)       
    vax_date = models.DateTimeField(null=True)
    brgy = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
    guardian = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_of_birth = models.TextField(null=True)     
    created = models.DateTimeField()
    vax1 = models.IntegerField(null=True)
    vax1_info = models.TextField(null=True)
    vax2 = models.IntegerField(null=True)
    vax2_info = models.TextField(null=True)
    vax3 = models.IntegerField(null=True)
    vax3_info = models.TextField(null=True)
    def __str__(self):
        return self.child

