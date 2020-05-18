from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    article = models.CharField(max_length=128)
    category = models.ForeignKey(
        Category, related_name="products",
        on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    size = models.PositiveIntegerField()

    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def __str__(self):
        return f"{self.category} - {self.name}"
