

from django.db import models

# Create your models here.
class RegisterForm(models.Model):

    objects = None
    name = models.CharField(max_length=100,null=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    address = models.CharField(max_length=100, null=False)
    contact = models.CharField(max_length=50,null=False)

