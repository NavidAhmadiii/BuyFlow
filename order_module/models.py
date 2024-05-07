from django.db import models
from django.contrib.auth import get_user_model
from product_module.models import Product
from user_module.models import CustomUser

# Create your models here.

USER = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    is_payment = models.DateField(null=True, blank=True)
    order_detail = models.ManyToManyField('OrderDetail', related_name='order-detail+')

    def __str__(self):
        return f"Order for {self.user}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"OrderDetail: {self.order} - {self.product}"

    def save(self, *args, **kwargs):
        if self.final_price is not None and self.count is not None:
            self.final_price = self.price * self.count
        else:
            self.final_price = 0
        super().save(*args, **kwargs)
