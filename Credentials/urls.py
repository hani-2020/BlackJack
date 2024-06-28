""""
put your Credential Urls here
"""
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('signup/', CustomSignupView, name='signup'),
]