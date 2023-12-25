from . import views
from django.urls import path

app_name = "cart"

urlpatterns = [
    path("current/<slug:product_slug>/", views.cart_current, name="cart_current"),
    path("contact/<slug:slug>/", views.ContactSeller.as_view(), name="contact_seller"),
]
