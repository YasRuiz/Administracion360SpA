from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre Completo')
    email = models.EmailField(verbose_name='Correo Electrónico')
    mensaje = models.TextField(verbose_name='Mensaje')
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío')

    class Meta:
        verbose_name = 'Mensaje de Contacto'
        verbose_name_plural = 'Mensajes de Contacto'
        ordering = ['-fecha_envio'] # Ordena del más nuevo al más viejo

    def __str__(self):
        return f"{self.nombre} ({self.email})"


class Comunidad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Comunidad')
    direccion = models.CharField(max_length=200, verbose_name='Dirección')
    rut = models.CharField(max_length=12, blank=True, null=True, verbose_name='RUT')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comunidad'
        verbose_name_plural = 'Comunidades'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    # ForeignKey conecta cada unidad con una sola Comunidad
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE, related_name='unidades', verbose_name='Comunidad')
    numero = models.CharField(max_length=20, verbose_name='Número (Ej: Dpto 101)')
    nombre_propietario = models.CharField(max_length=100, verbose_name='Nombre del Propietario')
    email_propietario = models.EmailField(blank=True, null=True, verbose_name='Correo del Propietario')

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['comunidad', 'numero']

    def __str__(self):
        return f"{self.comunidad.nombre} - {self.numero}"