from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from barter.models import ItemModel
from barter.forms import CreateAnnouncementForm


class BarterItemsView(ListView):
    template_name = 'barter/items.html'
    queryset = ItemModel.objects.all()
    ordering = ('-date_created', )


class CreateAnnouncementView(CreateView):
    template_name = 'barter/create_announcement.html'
    model = ItemModel
    form_class = CreateAnnouncementForm
    success_url = reverse_lazy('barter:items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if len(form.cleaned_data['description']) <= 25:
            form.cleaned_data['description'] += 3 * '\n'
        return super(CreateAnnouncementView, self).form_valid(form)
