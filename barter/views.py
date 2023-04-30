from django.views.generic.base import TemplateView


class BarterItemsView(TemplateView):
    template_name = 'barter/items.html'
