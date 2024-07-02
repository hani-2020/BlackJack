"""Create your views here."""
from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView(SignupView):
    """To make custom signup view"""
    form_class = CustomSignupForm()

def profile(request):
    """For displaying user profile"""
    return render(request, "account/profile.html")
