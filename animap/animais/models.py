from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Animal(models.Model):
    temp_id = models.UUIDField(default=uuid.uuid4)
    username = models.CharField(max_length = 150)
    endereço = models.CharField(max_length = 300)
    descriçao = models.CharField(max_length= 350)
    ponto_ref = models.CharField(max_length = 400, null=True)
    coordX = models.FloatField()
    coordY = models.FloatField()
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, default='pendente', choices=[
        ('pendente', 'Pendente'), 
        ('resgatado', 'Resgatado'),
        ('naolocalizado', 'Não localizado'), 
    ])

