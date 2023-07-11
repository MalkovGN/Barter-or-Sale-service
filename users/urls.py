from django.urls import path

from users.views import (ConfirmRegistrationView, UserLoginView,
                         UserProfileView, UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<uuid:user_code>/', ConfirmRegistrationView.as_view(), name='confirm')
]
