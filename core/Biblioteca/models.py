from django.db import models


# Create your models here.
ESTADO_DEL_LIBRO = [
    ('IN', 'En biblioteca'),
    ('BW', 'Prestado'),
    ('RQ', 'Pedido'),
    ('RV', 'Reservado'),
]

class Material(models.Model):
    tipoMaterial = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=30)
    año = models.IntegerField()
    status = models.CharField(max_length=2, choices=ESTADO_DEL_LIBRO, default='En biblioteca')

    class Meta:
        verbose_name = ('Material de Lectura')
        verbose_name_plural = ('Materiales de Lectura')
