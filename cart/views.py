from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Product
from .forms import ContactSellerForm


def cart_current(request, product_slug):
    """
    Get product with specified slug,
    return 404 page if not found
    Render html along with product information
    """
    product = get_object_or_404(Product, slug=product_slug)

    return render(request, "cart_current.html", {"product": product})


class ContactSeller(generic.CreateView):
    """
    Contact seller view to buy
    a product
    """

    template_name = "contact_seller.html"
    form_class = ContactSellerForm
    success_url = "/"

    def get_product(self):
        product_slug = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=product_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = self.get_product()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = self.get_product()
        form.instance.customer = self.request.user
        return super(ContactSeller, self).form_valid(form)
