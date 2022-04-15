from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=20)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()