from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reportar/', views.reportar, name='reportar'),
    path('reportes/', views.reportes, name='reportes'), 
    path('politicas_privacidad/', views.politicas_privacidad, name='politicas_privacidad'),
    path('terminos_condiciones/', views.terminos_condiciones, name='terminos_condiciones'), 
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'), 
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('index/', views.index, name='index'),
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
    path('logout/', views.logout, name='logout'),
    path('mi_perfil/<int:id_user>/', views.mi_perfil, name='mi_perfil'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
