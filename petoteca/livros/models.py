from django.db import models

# Create your models here.
from django.forms import ChoiceField

class Livro(models.Model):
    #Nome = models.CharField(max_length = 100)
    #Email = models.EmailField(null = True)
    Titulo = models.CharField("Título", max_length = 100)
    Codigo = models.CharField("Código", max_length = 20, null = True)
    Autor = models.CharField(max_length = 100)
    Coautor = models.CharField(blank = True, max_length = 100)
    Edicao = models.IntegerField("Edição") 
    Volume = models.IntegerField(null = True)
    state_choices = (
        ('Bem conservado','Bem conservado'),
        ('Conservado','Conservado'),
        ('Pouco conservado','Pouco conservado')
    )
    Estado = models.CharField(max_length = 30, null = True, choices = state_choices)
    type_choices = (
        ('Livro','Livro'),
        ('Cópia','Cópia')
    )
    Tipo = models.CharField(max_length = 30, null = True, choices = type_choices)
    Data = models.DateField(null = True)