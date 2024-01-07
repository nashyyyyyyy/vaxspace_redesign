from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Register, Vaccine
from django import forms





class CreateUserForm(UserCreationForm):
    role = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    contact = forms.IntegerField()  # Change to IntegerField

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role', 'address', 'contact']
         
