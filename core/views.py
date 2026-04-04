from django.shortcuts import render, get_object_or_404
# Importamos las herramientas necesarias para enviar correos y mostrar mensajes en pantalla
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Importamos nuestros modelos
from .models import MensajeContacto, Comunidad, Unidad

def home(request):
    # 1. Contamos cuántas comunidades y unidades existen en la base de datos
    total_comunidades = Comunidad.objects.count()
    total_unidades = Unidad.objects.count()
    
    # 2. Pasamos estos datos a la plantilla a través del diccionario 'context'
    context = {
        'total_comunidades': total_comunidades,
        'total_unidades': total_unidades,
    }
    
    # Renderiza la plantilla de inicio con los datos dinámicos
    return render(request, 'pages/home.html', context)

def servicios(request):
    # Renderiza y devuelve la plantilla de servicios
    return render(request, 'pages/servicios.html')

def contacto(request):
    # Si el usuario hace clic en "Enviar Mensaje", el método será POST
    if request.method == 'POST':
        # 1. Obtener los datos del formulario HTML
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        try:
            # 2. Guardar el mensaje en la base de datos
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje
            )

            # 3. Armar el asunto y el cuerpo del correo
            asunto_correo = f"Nuevo contacto web: {nombre}"
            cuerpo_correo = f"""
            Has recibido un nuevo mensaje desde el sitio web de Visión 360, gestión y servicios SpA.
            
            Detalles del prospecto:
            -----------------------
            Nombre: {nombre}
            Email: {email}
            
            Mensaje o Requerimiento:
            ------------------------
            {mensaje}
            """

            # 4. Función de Django para enviar el correo
            send_mail(
                asunto_correo,
                cuerpo_correo,
                settings.EMAIL_HOST_USER, 
                [settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )
            
            # 5. Mensaje de éxito
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito! Nos pondremos en contacto a la brevedad.')
            
        except Exception as e:
            # Si algo falla, mostramos un error
            messages.error(request, 'Hubo un problema al procesar tu solicitud. Por favor, intenta nuevamente más tarde.')
            print(f"Error interno al guardar/enviar contacto: {e}")

    return render(request, 'pages/contacto.html')

# --- VISTA PARA LISTADO DE COMUNIDADES ---
def comunidades(request):
    # Traemos todas las comunidades
    lista_comunidades = Comunidad.objects.all()
    return render(request, 'pages/comunidades.html', {'comunidades': lista_comunidades})

# --- VISTA PARA EL DETALLE DE UNA COMUNIDAD ---
def comunidad_detalle(request, comunidad_id):
    # Buscamos el edificio por su ID
    comunidad_especifica = get_object_or_404(Comunidad, id=comunidad_id)
    return render(request, 'pages/comunidad_detalle.html', {'comunidad': comunidad_especifica})