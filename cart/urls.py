from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('current/<slug:product_slug>/', views.cart_current, name="cart_current"),
]