from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField()
    contact_number = forms.CharField(max_length = 15)
    class Meta:
        model = User
        fields = ['name','email', 'username', 'contact_number', 'password1', 'password2']