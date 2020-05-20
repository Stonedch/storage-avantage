from . import models

from django import forms
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "name",
            "image",
            "category",
            "price",
            "amount",
            "size",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("name").verbose_name }),
            # "image": forms.ClearableFileInput(),
            "price": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("price").verbose_name }),
            "amount": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("amount").verbose_name }),
            "size": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("size").verbose_name }),
        }
