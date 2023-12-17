from django.contrib import admin
from .models import Product, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_filter = ("category", "status")  # add 'created_on' later
    list_display = ("name", "slug", "status")  # add 'created_on' later
    search_fields = ["name", "description"]
    summernote_fields = "description"
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("approved", "created_on")
    list_display = ("username", "body", "product", "created_on", "approved")
    search_fields = ["username", "email", "body"]
    actions = [
        "approved_comments",
    ]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
