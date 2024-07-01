"""Create your views here."""
from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from .forms import CustomSignupForm, CustomLoginForm

class CustomSignupView(SignupView):
    """To make custom signup view"""
    form_class = CustomSignupForm()

    def form_valid(self, form):
        super().form_valid(form)
        return render(self.request, "account/profile.html")
    
def Profile(request):
    return render(request, "account/profile.html")