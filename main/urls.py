from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo-libros/', views.catalogo_libros, name='catalogo_libros'),
    path('catalogo-autores/', views.catalogo_autores, name='catalogo_autores'),
    path('categorias/', views.categorias, name='categorias'),
]
