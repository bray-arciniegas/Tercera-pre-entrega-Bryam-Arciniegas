from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),

    #Cliente
    path("clientes/", ClienteList.as_view(), name="clientes"),
    path("clientes_create/", ClienteCreate.as_view(), name="clientes_create"),

    #Reseña
    path("reseñas/", ReseñaList.as_view(), name="reseñas"),
    path("reseñas_create/", ReseñaCreate.as_view(), name="reseñas_create"),

    #Producto
    path("productos/", ProductoList.as_view(), name="productos"),
    path("productos_create/", ProductoCreate.as_view(), name="productos_create"),
    
    #Busqueda
    path("buscar_productos/", buscarProductos, name="productos_buscar"),
    path("encontrar_productos/", encontrarProductos, name="producto_encontrar"),
]