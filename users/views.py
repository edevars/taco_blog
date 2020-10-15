from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from users.forms import SignupForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Profile


class ClassLoginView(LoginView):
    template_name = 'users/login.html'


class ClassLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['picture','website']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        return reverse('blog:home')


class SignUpView(FormView):
    """Users signup view"""
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.save()

        username = form['username'].value()
        password = form['password'].value()

        user = authenticate(
            self.request, username=username, password=password)

        if user:
            login(self.request, user)
            return redirect('blog:home')
        else:
            return redirect('users:login')
