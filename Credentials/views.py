"""Create your views here."""
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from .forms import CustomSignupForm, CustomLoginForm

class CustomSignupView(SignupView):
    """To make custom signup view"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomSignupForm()
        return context
    
def Profile(request):
    return render(request, "profile.html")