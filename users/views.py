from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:confirm')


class ConfirmRegistrationView(TemplateView):
    template_name = 'users/confirm_registration.html'
