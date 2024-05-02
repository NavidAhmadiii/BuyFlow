from django.db import models
from django.contrib.auth import get_user_model
from product_module.models import Product
from django.conf import settings

# Create your models here.

USER = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    is_payment = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_detail = models.ManyToManyField('OrderDetail', related_name='order-detail+')

    def __str__(self):
        return f"Order for {self.user.username}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()

    def __str__(self):
        return f"OrderDetail: {self.order} - {self.product}"

    def calculate_final_price(self):
        return self.final_price * self.count
