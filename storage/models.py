from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_search_url(self):
        return reverse("product_list_url") + "?search=" + self.name
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    image = models.ImageField(
        upload_to="products", default="none/no-image.jpg",
        blank="True",
        verbose_name="Изображение")
    vendor_code = models.CharField(max_length=128, blank=True, unique=True, verbose_name="Внутренний код")
    articul = models.CharField(max_length=128, verbose_name="Артикул")
    category = models.ForeignKey(
        Category, related_name="products",
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Категория")
    price = models.PositiveIntegerField(verbose_name="Цена")
    amount = models.PositiveIntegerField(verbose_name="Количество")
    size = models.PositiveIntegerField(verbose_name="Размер")

    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor_code = self.name[0] + str(self.id) + str(self.size)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={"vendor_code": self.vendor_code})

    def get_update_url(self):
        return reverse("product_update_url", kwargs={"vendor_code": self.vendor_code})

    def get_delete_url(self):
        return reverse("product_delete_url", kwargs={"vendor_code": self.vendor_code})
    
    def __str__(self):
        return f"{self.vendor_code} - {self.name}"
