from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    """
    Model to place an order
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ordered_product", null=True)
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.fname} {self.lname}"