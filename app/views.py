from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dificultad,Categoria,Post
from .forms import DificultadForm,CategoriaForm,PostForm

# Create your views here.

def post(request):
    query_list = Post.objects.all()
    paginator = Paginator(query_list,16) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    context = {
            "Post":query,
        }
    return render(request,"Index.html", context)

def crear_categoria(request):
    form = CategoriaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        categoria = form.save(commit = False)
        categoria.save()
        return HttpResponseRedirect('/')
    context = {
        "form":form,
    }
    return render(request,"crearcategoria.html",context)

    def crear_dificultad(request):
    form = DificultadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        dificultad = form.save(commit = False)
        dificultad.save()
        return HttpResponseRedirect('/')
    context = {
        "form":form,
    }
    return render(request,"creardificultad.html",context)
