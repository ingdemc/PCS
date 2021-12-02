

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Conexionbd(models.Model):
    id=models.AutoField(primary_key=True)
    nameconections=models.CharField(max_length=100,null=False,unique=True)
    note=models.CharField(max_length=200,null=False,unique=True)
    name=models.CharField(max_length=100,null=False,unique=True,verbose_name='Nombre')
    user=models.CharField(max_length=100,null=False,unique=True)
    host=models.CharField(max_length=50,null=False)
    port=models.IntegerField()
    url=models.CharField(max_length=150,null=False)
    password1 = models.CharField(max_length=50,null=False)

    def __integer__(self):
        return self.id

    class Meta:
        ordering = ['id']
        verbose_name = 'Tabla'
        verbose_name_plural = 'Tablas'


class datab(models.Model):
    id=models.AutoField(primary_key=True)
    nomtable=models.CharField(max_length=100,null=False,unique=True,verbose_name='Nombre')
    contrib=models.CharField(max_length=100,null=False,unique=True)
    