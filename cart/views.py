from django.shortcuts import render, get_object_or_404
from shop.models import Product


def cart_current(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    return render(request, "cart_current.html", {"product": product})