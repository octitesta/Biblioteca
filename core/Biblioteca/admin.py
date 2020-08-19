from django.contrib import admin
from.models import *

class PrestamoInline(admin.TabularInline):
    model = Prestamo

class AlumnoAdmin(admin.ModelAdmin):
    inlines = [PrestamoInline,]
    list_display = ['matricula','nombre','apellido',]
    search_fields = ['nombre','apellido','correo','matricula']
    fieldsets = (
        ('Datos Personales',{
            'fields':('nombre','apellido','correo','telefono','matricula')
        }),
        ('Biblioteca',{
            'fields':('num_libros','deuda')
        })
        )

class ProfesorAdmin(admin.ModelAdmin):
    inlines = [PrestamoInline,]
    list_display = ['num_empleado','nombre','apellido']
    search_fields = ['nombre','apellido','correo','num_empleado']
    fieldsets = (
        ('Datos Personales',{
            'fields':('nombre','apellido','correo','telefono','num_empleado')
        }),
        ('Biblioteca',{
            'fields':('num_libros','deuda')
        })
        )

class LibroAdmin(admin.ModelAdmin):
    inlines = [PrestamoInline,]
    list_display = ['titulo','autor','status']
    search_fields = ['titulo','autor','status','editorial']

class RevistaAdmin(admin.ModelAdmin):
    inlines = [PrestamoInline,]
    list_display = ['titulo','autor','status']
    search_fields = ['titulo','autor','status']

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['persona','material','fecha_salida','fecha_regreso']

   
#admin.site.register(Material)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Revista,RevistaAdmin)
#admin.site.register(Persona)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Prestamo,PrestamoAdmin)
# Register your models here.
