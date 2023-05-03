from django.urls import path

from barter.views import BarterItemsView, CreateAnnouncementView, AnnouncementDetailView

app_name = 'barter'

urlpatterns = [
    path('items/', BarterItemsView.as_view(), name='items'),
    path('create_item', CreateAnnouncementView.as_view(), name='create_announcement'),
    path('item/<int:pk>', AnnouncementDetailView.as_view(), name='announcement_detail'),
]
