from django.db import models
from datetime import date

class Categoria(models.Model):
    nome = models.CharField( max_length = 40 )
    descricao = models.TextField()

    def __str__ (self):
        return self.nome

class Livros(models.Model):
    titulo = models.CharField( max_length = 100 )
    codigo = models.CharField( max_length = 15 )
    autor = models.CharField( max_length = 50 )
    data_cadastro = models.DateField( default = date.today )
    disponivel = models.BooleanField( default = True )
    volume = models.DecimalField( max_digits = 10, decimal_places = 0, blank = True, null = True )
    edicao = models.DecimalField( max_digits = 10, decimal_places = 0, blank = True, null = True )
    categoria = models.ForeignKey( Categoria, on_delete = models.DO_NOTHING )

    class Meta: 
        verbose_name = 'Livro'

    def __str__ (self):
        return self.titulo