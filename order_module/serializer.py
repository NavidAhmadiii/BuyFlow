from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Order, OrderDetail

USER = get_user_model()


class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(source='order.user', read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'product', 'price', 'count', 'user']

    def create(self, validated_data):
        # ایجاد یک نمونه از OrderDetail با استفاده از داده‌های اعتبارسنجی شده
        return OrderDetail.objects.create(
            order=validated_data['order'],
            product=validated_data['product'],
            price=validated_data['price'],
            count=validated_data['count']
        )


class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'is_paid', 'is_payment', 'order_detail']


class OrderCreateSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'is_paid', 'order_detail']

    def create(self, validated_data):
        order_detail_data = validated_data.pop('order_detail')
        order = Order.objects.create(**validated_data)
        for detail_data in order_detail_data:
            OrderDetail.objects.create(order=order, **detail_data)
        return order
