from django.urls import path

from barter.views import BarterItemsView, CreateAnnouncementView

app_name = 'barter'

urlpatterns = [
    path('items/', BarterItemsView.as_view(), name='items'),
    path('create_item', CreateAnnouncementView.as_view(), name='create_announcement'),
]
