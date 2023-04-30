from django.urls import path

from choose_service.views import ChooseServiceView

app_name = 'choose_service'

urlpatterns = [
    path('', ChooseServiceView.as_view(), name='choose_service'),
]
