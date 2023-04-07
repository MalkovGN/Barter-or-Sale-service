from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from users.forms import UserRegistrationForm, UserLoginForm
from users.models import EmailVerification, User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class ConfirmRegistrationView(TemplateView):
    template_name = 'users/confirm_registration.html'

    def get(self, request, *args, **kwargs):
        user_code = kwargs['user_code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, user_code=user_code)
        if email_verification.exists():
            user.is_verified_email = True
            user.save()
            return super(ConfirmRegistrationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('users:login'))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        return HttpResponse(reverse('users:profile'))
