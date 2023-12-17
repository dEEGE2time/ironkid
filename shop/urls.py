from . import views
from django.urls import path


urlpatterns = [
    path("", views.ProductList.as_view(), name="shop"),
    path("add_product/", views.AddProduct.as_view(), name="add_product"),
    path("<slug:slug>/", views.ProductDetails.as_view(), name="product_detail"),
    path("delete/<slug:slug>/", views.DeleteProduct.as_view(), name="delete_product"),
]
