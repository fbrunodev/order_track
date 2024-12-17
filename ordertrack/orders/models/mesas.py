from django.db import models
from .enums import StatusMesa

class Mesas(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero= models.IntegerField()
    status = models.IntegerField(
        choices=[(status.value, status.name) for status in StatusMesa],
        default=StatusMesa.DISPONIVEL.value
    )