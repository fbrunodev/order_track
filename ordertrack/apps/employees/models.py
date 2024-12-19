from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    cargo = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)  

    salario = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)