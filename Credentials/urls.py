""""
put your Credential Urls here
"""
from django.urls import path
from .views import Profile

urlpatterns = [
    path("profile/", Profile, name='profile')
]