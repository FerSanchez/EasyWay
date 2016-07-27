from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Dificultad(models.Model):
    dificultad= models.CharField(max_length=120)
    descripcion=models.TextField()
    # creada = models.DateTimeField(auto_now=False, auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.dificultad

class Categoria(models.Model):
    categoria= models.CharField(max_length=120)
    descripcion=models.TextField()
    # creada = models.DateTimeField(auto_now=False, auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.categoria


class Post(models.Model):
    title=models.CharField(max_length=120)
    dificultad = models.ForeignKey(Dificultad,null=True,blank=True)
    categoria=models.ForeignKey(Categoria,null=True,blank=True)
    media=models.FileField(null=True,blank=True)
    usuario=models.ForeignKey(User)#esto no me funciona correctamente
    descripcion=models.CharField(max_length=15000)
    actualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
    creado = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.title
