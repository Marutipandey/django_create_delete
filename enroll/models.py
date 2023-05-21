from django.db import models

# Create your models here.
class simpleform(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField(max_length=80)
    phone_number=models.CharField(max_length=100)