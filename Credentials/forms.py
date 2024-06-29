"""write your forms here"""
from django import forms
from allauth.account.forms import SignupForm, LoginForm

class CustomSignupForm(SignupForm):
    """Custom signup form which will have first name, last name and other details"""
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthday = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(max_length=254, required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']
        user.email = self.cleaned_data['email']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    """Custom login form to take in email and password from user"""
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
