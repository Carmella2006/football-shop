from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('jersey', 'Jersey'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='shoes')
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def is_product_hot(self):
        return self.stock < 5

    def __str__(self):
        return self.name