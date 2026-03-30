from django.contrib import admin
from .models import MensajeContacto, Comunidad, Unidad

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    # Qué columnas queremos ver en la lista principal
    list_display = ('nombre', 'email', 'fecha_envio')
    
    # Agrega una barra de búsqueda para encontrar clientes rápidamente
    search_fields = ('nombre', 'email', 'mensaje')
    
    # Agrega un filtro lateral por fechas
    list_filter = ('fecha_envio',)
    
    # Protege la fecha para que no se pueda modificar accidentalmente
    readonly_fields = ('fecha_envio',)

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'rut')
    search_fields = ('nombre', 'rut')

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('numero', 'comunidad', 'nombre_propietario', 'email_propietario')
    list_filter = ('comunidad',) # Filtro lateral súper útil para ver solo dptos de un edificio
    search_fields = ('numero', 'nombre_propietario')