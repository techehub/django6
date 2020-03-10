from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=100)
    description= models.CharField(max_length=500)
    price= models.IntegerField()
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.name+ "::" + self.brand

