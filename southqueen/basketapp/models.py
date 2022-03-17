from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)

    def product_cost(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        return sum(map(lambda x: x.quantity, Basket.objects.filter(user=self.user)))

    def total_cost(self):
        return sum(map(lambda x: x.product_cost(), Basket.objects.filter(user=self.user)))