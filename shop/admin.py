from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Register the Product model
    with the custom admin options
    """
    list_filter = ("category", "status")
    list_display = ("name", "slug", "status")
    search_fields = ["name", "description"]
    summernote_fields = "description"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category)