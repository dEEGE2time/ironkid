from django.shortcuts import render


def cart_current(request, product_slug):
    return render(request, "cart_current.html")


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass