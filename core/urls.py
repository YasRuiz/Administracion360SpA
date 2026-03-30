from django.urls import path
from . import views

urlpatterns = [
    # path(ruta_en_navegador, funcion_en_views, nombre_para_plantillas)
    path('', views.home, name='home'),                     # La página principal (Inicio)
    path('servicios/', views.servicios, name='servicios'), # Página de Servicios
    path('contacto/', views.contacto, name='contacto'),    # Página de Contacto
    path('comunidades/', views.comunidades, name='comunidades'), # Página de Comunidades
    # El <int:comunidad_id> atrapa el número en la URL y se lo pasa a la vista
    path('comunidades/<int:comunidad_id>/', views.comunidad_detalle, name='comunidad_detalle'),
]