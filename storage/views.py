from . import models
from . import forms

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic import View


class ProductListView(View):
    def get(self, request):
        categories = models.Category.objects.all()
        search_query = request.GET.get("search", "")

        if search_query:
            products = models.Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(category__name=search_query))
        else:
            products = models.Product.objects.all()

        context = {
            "categories": categories,
            "product_list": products,
            "search": search_query
        }

        return render(request, "storage/index.html", context)

class ProductAddView(View):
    def get(self, request):
        context = {
            "form": forms.ProductForm(),
        }

        return render(request, "storage/product-add.html", context)

    def post(self, request):
        product = forms.ProductForm(request.POST, request.FILES)

        if product.is_valid():
            product.save()

        return redirect(reverse("product_list_url"))


class ProductUpdateView(View):
    def get(self, request, vendor_code):
        product = get_object_or_404(models.Product, vendor_code__iexact=vendor_code)
        form = forms.ProductForm(instance=product)

        context = {
            "form": form,
        }

        return render(request, "storage/product-update.html", context)
    
    def post(self, request, vendor_code):
        product = models.Product.objects.get(vendor_code__iexact=vendor_code)
        form = forms.ProductForm(request.POST, request.FILES, instance=product)

        print(form.data)

        if form.is_valid():
            form.save()

        return redirect(reverse("product_list_url"))


class ProductDetailView(View):
    def get(self, request, vendor_code):
        product = get_object_or_404(models.Product, vendor_code__iexact=vendor_code)

        context = {
            "product": product,
        }

        return render(request, "storage/product-detail.html", context)


class ProductDeleteView(View):
    def get(self, request, vendor_code):
        product = models.Product.objects.get(vendor_code__iexact=vendor_code)
        product.delete()

        return redirect(reverse("product_list_url"))
