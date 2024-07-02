"""Create your views here."""
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from allauth.account.views import SignupView, LoginView
from .forms import CustomSignupForm, CustomLoginForm

class CustomSignupView(SignupView):
    """To make custom signup view"""
    form_class = CustomSignupForm()

    def dispatch(self, request, *args, **kwargs):
        print(request.POST)
        return super().dispatch(request, *args, **kwargs)
    
def Profile(request):
    return render(request, "account/profile.html")