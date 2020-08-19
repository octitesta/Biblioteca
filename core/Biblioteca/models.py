from django.db import models


# Create your models here.
ESTADO_DEL_LIBRO = [
    ('IN', 'En biblioteca'),
    ('BW', 'Prestado'),
    ('RQ', 'Pedido'),
    ('RV', 'Reservado'),
]

class Material(models.Model):
    codigo = models.CharField(max_length=20)
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=30)
    año = models.IntegerField()
    status = models.CharField(max_length=2, choices=ESTADO_DEL_LIBRO, default='En biblioteca')

    class Meta:
        verbose_name = ('Material de Lectura')
        verbose_name_plural = ('Materiales de Lectura')

class Libro(Material):
    editorial = models.CharField(max_length=40)

class Revista(Material):
    class Meta:
        verbose_name = ('Revista')
        verbose_name_plural = ('Revistas')

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    numero = models.IntegerField()
    num_libros = models.IntegerField()
    deuda = models.BooleanField()

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    num_empleado = models.IntegerField()