from django.db import models
from django.core.validators import MaxValueValidator

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reseña(models.Model):
    autor = models.CharField(max_length=50)
    puntuacion = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.autor} | {self.puntuacion}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} | ${self.precio}"