""""
put your Credential Urls here
"""
from django.urls import path
from .views import Profile, CustomSignupView

urlpatterns = [
    path("profile/", Profile, name='profile'),
]