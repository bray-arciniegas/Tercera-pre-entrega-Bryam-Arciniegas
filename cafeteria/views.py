from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView

def home(request):
    return render(request, "home.html")

# VIEWS DE CLIENTE

class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "direccion", "email"]
    success_url = reverse_lazy("clientes")

# VIEWS DE RESEÑAS
    
class ReseñaList(ListView):
    model = Reseña

class ReseñaCreate(CreateView):
    model = Reseña
    fields = ["autor", "puntuacion", "comentario"]
    success_url = reverse_lazy("reseñas")

# VIEWS DE PRODUCTOS
    
class ProductoList(ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = ["nombre", "precio"]
    success_url = reverse_lazy("productos")

def buscarProductos(request):
    return render(request, "cafeteria/producto_buscar.html")

def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains = patron)
        contexto = {"producto_list": productos}
        return render(request, "cafeteria/producto_list.html", contexto)
    
    contexto = {"producto_list": Producto.objects.all()}
    return render(request, "cafeteria/producto_list.html", contexto)