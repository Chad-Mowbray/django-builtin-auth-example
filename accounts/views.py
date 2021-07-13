from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login/'


class CustomLogoutView(LogoutView):
    next_page = "/accounts/login/"