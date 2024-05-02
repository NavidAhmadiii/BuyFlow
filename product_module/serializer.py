from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer class for the Category model.
        This serializer is used for serializing Category instances to JSON format.
    """
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    """
        Serializer class for the Product model.
        This serializer is used for serializing Product instances to JSON format.
    """
    category = CategorySerializer

    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'description', 'category', 'status')


class ProductCreateSerializer(serializers.ModelSerializer):
    """
        Serializer class for creating a new product.
        This serializer handles the validation and creation of new product instances.
        It defines the fields that are required to create a new product and maps them to the Product model fields.

        Note:
        Ensure that the 'image' field is handled as multipart/form-data when making POST requests to the API endpoint.
    """

    class Meta:
        model = Product
        fields = ('title', 'image', 'description', 'category', 'status')
