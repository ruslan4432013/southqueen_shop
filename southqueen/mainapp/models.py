from uuid import uuid4

from django.db import models


class ProductCategory(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class Product(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название товара')
    image = models.ImageField(upload_to='products_images', blank=True)  # 480 x 480
    short_desc = models.CharField(max_length=60, blank=True, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена продукта')
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
