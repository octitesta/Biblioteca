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

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = ('Material de Lectura')
        verbose_name_plural = ('Materiales de Lectura')

class Libro(Material):
    editorial = models.CharField(max_length=40)
    fotoPortada = models.ImageField(max_length=100, upload_to='portadas/', blank=True)

class Revista(Material):
    pass

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.IntegerField()
    num_libros = models.IntegerField()
    deuda = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    num_empleado = models.IntegerField()
    class Meta:
        verbose_name = ('Profesor')
        verbose_name_plural = ('Profesores')

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 30)
    fecha_salida = models.DateField(auto_now=False)
    fecha_regreso = models.DateField(auto_now=False)
    persona = models.ForeignKey('Persona',on_delete=models.CASCADE,null=False)
    material = models.ForeignKey('Material',on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.codigo

