from django.db import models


class Acompanhamentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=20)