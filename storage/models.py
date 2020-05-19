from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    vendor_code = models.CharField(max_length=128, verbose_name="Артикул")
    category = models.ForeignKey(
        Category, related_name="products",
        on_delete=models.SET_NULL, null=True,
        verbose_name="Категория")
    price = models.PositiveIntegerField(verbose_name="Цена")
    amount = models.PositiveIntegerField(verbose_name="Количество")
    size = models.PositiveIntegerField(verbose_name="Размер")

    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={"vendor_code": self.vendor_code})
    
    def __str__(self):
        return f"{self.category} - {self.name}"
