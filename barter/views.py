from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from barter.models import ItemModel
from barter.forms import CreateAnnouncementForm


class BarterItemsView(TemplateView):
    template_name = 'barter/items.html'


class CreateAnnouncementView(CreateView):
    template_name = 'barter/create_announcement.html'
    model = ItemModel
    form_class = CreateAnnouncementForm
    success_url = reverse_lazy('barter:items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAnnouncementView, self).form_valid(form)
