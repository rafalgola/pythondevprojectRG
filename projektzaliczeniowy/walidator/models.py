from django.db import models


# Create your models here.
class Asserted_Pesels(models.Model):
    stamp = models.CharField(max_length=16)
    pesel = models.CharField(max_length=11)
    assertion_result = models.CharField(max_length=5)
