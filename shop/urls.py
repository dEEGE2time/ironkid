from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProductList.as_view(), name='shop'),
    path('<slug:slug>/', views.ProductDetails.as_view(), name='product_detail'),
]