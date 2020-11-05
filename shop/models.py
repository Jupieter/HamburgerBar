from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productName = models.CharField(max_length=40)
    productIngredients = models.CharField(max_length=200)
    productPrice = models.DecimalField(max_digits=7, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    prodctActive = models.BooleanField(default="True")


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.productName