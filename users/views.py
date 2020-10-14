from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassLoginView(LoginView):
    template_name = 'users/login.html'


class ClassLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'
