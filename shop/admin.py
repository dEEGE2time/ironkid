from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_filter = ("category", "status")  # add 'created_on' later
    list_display = ("name", "slug", "status")  # add 'created_on' later
    search_fields = ["name", "description"]
    summernote_fields = "description"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category)