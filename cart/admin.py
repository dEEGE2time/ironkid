from django.contrib import admin
from .models import Order
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    list_display = ("lname", "fname", "email", "get_product_name", "get_product_status")
    search_fields = ["fname", "lname"]
    
    def get_product_name(self, obj):
        return obj.product.name if obj.product else None
    
    def get_product_status(self, obj):
        return obj.product.get_status_display() if obj.product else None
    
    get_product_name.short_description = "Product Name"
    get_product_status.short_description = "Status"