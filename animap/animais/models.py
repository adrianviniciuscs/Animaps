from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animal(models.Model):
    username = models.CharField(max_length = 150)
    endereço = models.CharField(max_length = 300)
    descriçao = models.CharField(max_length= 250)
    coordX = models.FloatField()
    coordY = models.FloatField()
    foto = models.URLField(blank=True, null=True)