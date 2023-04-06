from django.urls import path

from users.views import ConfirmRegistrationView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('confirm/', ConfirmRegistrationView.as_view(), name='confirm'),
]
