from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Product
from .forms import ContactSellerForm


def cart_current(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    return render(request, "cart_current.html", {"product": product})

class ContactSeller(generic.CreateView):
    """
    Contact seller view to buy
    a product
    """
    template_name = './templates/contact_seller.html'
    model = Product
    form_class = ContactSellerForm
    
    success_url ="/"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactSeller, self).form_valid(form)