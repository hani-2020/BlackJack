"""write your forms here"""
from django import forms
from allauth.account.forms import SignupForm, LoginForm

class CustomSignupForm(SignupForm):
    """Custom signup form which will have first name, last name and other details"""
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birthday = forms.DateField()
    email = forms.EmailField(max_length=254, required=True)

class CustomLoginForm(LoginForm):
    """Custom login form to take in email and password from user"""
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
