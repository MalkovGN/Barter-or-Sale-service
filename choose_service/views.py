from django.views.generic.base import TemplateView


class ChooseServiceView(TemplateView):
    template_name = 'choose_service/index.html'
