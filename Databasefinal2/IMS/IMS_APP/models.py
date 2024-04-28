from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=0 , default = 0)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
