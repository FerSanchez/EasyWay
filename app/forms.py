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
