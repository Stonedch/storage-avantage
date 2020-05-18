from . import models

from django.shortcuts import render
from django.views.generic import View


class ProductListView(View):
    def get(self, request):
        products = models.Product.objects.all()

        context = {
            "product_list": products,
        }

        return render(request, "storage/index.html", context)
