from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    descri = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 8)
    comment = models.TextField(default='COOL RIGHT')
    margonha = models.URLField(max_length=200, null = True)