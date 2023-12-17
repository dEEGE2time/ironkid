from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form to add a Product
    """

    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "size",
            "description",
            "price",
            "featured_image",
            "status",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "name": "Product Name",
            "category": "Category",
            "size": "Size",
            "description": "Product Description",
            "price": "Price",
            "featured_image": "Image of Product",
            "status": "Status",
        }
