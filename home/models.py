from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,null='true')
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)


    def __str__(self):
         return f"{self.name} {self.email}"
