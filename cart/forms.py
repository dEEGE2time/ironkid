from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import Order


class ContactSellerForm(forms.ModelForm):
    """
    Contact form when buying a product
    """

    class Meta:
        model = Order
        fields = [
            "fname",
            "lname",
            "email",
            "content",
        ]

        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "email": "Email",
            "content": "Message",
        }
