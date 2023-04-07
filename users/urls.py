from django.urls import path

from users.views import (ConfirmRegistrationView, UserLoginView,
                         UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('confirm/', ConfirmRegistrationView.as_view(), name='confirm'),
    path('verify/<str:email>/<uuid:user_code>/', ConfirmRegistrationView.as_view(), name='confirm')
]
