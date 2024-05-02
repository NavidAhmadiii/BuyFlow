from django.contrib import admin
from .models import Order, OrderDetail


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_paid', 'is_payment']
    list_filter = ['is_paid']
    search_fields = ['user__username']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'final_price']
