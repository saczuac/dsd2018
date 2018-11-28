from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product


class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "list.html"


class ProductBuyView(TemplateView):
    template_name = "buy.html"

    def get_context_data(self, **kwargs):
        context = super(ProductBuyView, self).get_context_data(**kwargs)
        product_id = kwargs.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)
            context['product'] = product
        return context
