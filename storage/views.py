from . import models

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View


class ProductListView(View):
    def get(self, request):
        products = models.Product.objects.all()

        context = {
            "product_list": products,
        }

        return render(request, "storage/index.html", context)

class ProductAddView(View):
    def get(self, request):
        return render(request, "storage/product-add.html")

    def post(self, request):
        return redirect(reverse("product_list_url"))


class ProductDetailView(View):
    def get(self, request, vendor_code):
        product = get_object_or_404(models.Product, vendor_code__iexact=vendor_code)

        context = {
            "product": product,
        }

        return render(request, "storage/product-detail.html", context)
