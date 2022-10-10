from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView)

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/registration.html'
    success_url = '/login/'

class LogInView(BaseLoginView):
    template_name = 'users/login.html'
    redirect_field_name = 'next'
    next_page = '/profile/'

class LogOutView(BaseLogoutView):
    redirect_field_name = 'next'

class ProfileView(TemplateView):
    template_name = 'users/profile.html'