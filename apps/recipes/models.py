from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_da_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_da_receita