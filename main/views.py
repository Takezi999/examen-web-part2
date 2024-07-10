from django.shortcuts import render
from .models import Libro, Autor, Categoria, NavItem
import json

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
def agregar_al_carrito(request):
    if request.method == 'POST' and request.is_ajax():
        libro_id = request.POST.get('libro_id')
        # Aquí puedes implementar la lógica para agregar el libro al carrito
        # Por ahora, simplemente responderemos con un mensaje de éxito
        response_data = {'message': 'Libro agregado al carrito exitosamente'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error': 'Invalid request'}), status=400, content_type="application/json")