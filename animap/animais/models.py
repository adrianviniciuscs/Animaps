from django.db import models

# Create your models here.
class Animal(models.Model):
    username = models.CharField(max_length = 50)
    endereço = models.CharField(max_length = 300)
    descriçao = models.CharField(max_length= 250)
    coordX = models.FloatField()
    coordY = models.FloatField()
    foto = models.URLField(blank=True, null=True)