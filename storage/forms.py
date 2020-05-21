from . import models

from django import forms
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "name",
            "image",
            "articul",
            "category",
            "price",
            "amount",
            "size",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("name").verbose_name }),
            "articul": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("articul").verbose_name }),
            "price": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("price").verbose_name }),
            "amount": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("amount").verbose_name }),
            "size": forms.TextInput(attrs={"placeholder": models.Product._meta.get_field("size").verbose_name }),
        }
