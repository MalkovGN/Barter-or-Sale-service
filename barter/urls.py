from django.urls import path

from barter.views import BarterItemsView

app_name = 'barter'

urlpatterns = [
    path('items/', BarterItemsView.as_view(), name='items'),
]
