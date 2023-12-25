from django.contrib import admin
from .models import Order
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):
    """
    Register the Order model
    with the custom admin options
    """
    list_display = ("get_lname", "get_fname", "email", "get_product_name", "get_product_status")
    search_fields = ["fname", "lname"]
    
    def get_lname(self, obj):
        return obj.lname
    
    def get_fname(self, obj):
        return obj.fname
    
    def get_product_name(self, obj):
        return obj.product.name if obj.product else None
    
    def get_product_status(self, obj):
        return obj.product.get_status_display() if obj.product else None
    
    get_lname.short_description = "First Name"
    get_fname.short_description = "Last Name"
    get_product_name.short_description = "Product Name"
    get_product_status.short_description = "Status"