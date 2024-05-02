from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
        ('in_progress', 'In Progress'),
        ('added_soon', 'added soon'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
