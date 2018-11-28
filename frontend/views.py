from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product

from employees.models import Employee


class ProductListView(LoginRequiredMixin, TemplateView):
    template_name = "list.html"


class ProductBuyView(TemplateView):
    template_name = "buy.html"

    def get_context_data(self, **kwargs):
        context = super(ProductBuyView, self).get_context_data(**kwargs)
        product_id = kwargs.get('product_id')
        if product_id:
            product = Product.objects.get(id=product_id)

            is_employee = Employee.objects.filter(user=self.request.user)

            if is_employee:
                product.price = product.cost_price
            else:
                product.price = product.calculate_price()

            context['product'] = product
        return context
