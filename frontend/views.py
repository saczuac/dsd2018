from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "list.html"
