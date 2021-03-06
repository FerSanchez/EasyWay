from django import forms
from .models import Dificultad,Categoria,Post
class DificultadForm(forms.ModelForm):
    class Meta:
        model=Dificultad
        fields=[
        "dificultad",
        "descripcion",
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
        "categoria",
        "descripcion",
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
        "title",
        "dificultad",
        "categoria",
        "media",
        "usuario",
        "descripcion",
        "actualizado",
        "creado",        
        ]
