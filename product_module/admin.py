from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
