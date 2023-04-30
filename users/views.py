from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
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


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.request.user.pk)
        return user

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.username,))
