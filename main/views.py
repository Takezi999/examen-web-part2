from django.shortcuts import render
from .models import Libro, Autor, Categoria, NavItem

def home(request):
    nav_items = NavItem.objects.all()
    return render(request, 'main/home.html', {'nav_items': nav_items})

def catalogo_libros(request):
    nav_items = NavItem.objects.all()
    libros = Libro.objects.all()
    return render(request, 'main/catalogo_libros.html', {'nav_items': nav_items, 'libros': libros})

def catalogo_autores(request):
    nav_items = NavItem.objects.all()
    autores = Autor.objects.all()
    return render(request, 'main/catalogo_autores.html', {'nav_items': nav_items, 'autores': autores})

def categorias(request):
    nav_items = NavItem.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'main/categorias.html', {'nav_items': nav_items, 'categorias': categorias})
