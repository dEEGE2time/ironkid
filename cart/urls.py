from . import views
from django.urls import path


urlpatterns = [
    path('', views.cart_current, name="cart_current"),
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('update/', views.cart_update, name="cart_update"),
]