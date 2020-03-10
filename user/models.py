from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName= models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

    def __str__ (self):
        return self.firstName +" " + self.lastName
