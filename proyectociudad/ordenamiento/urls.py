from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parroquias/', views.listar_parroquias, name='listar_parroquias'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    
    path('parroquia/crear/', views.crear_parroquia, name='crear_parroquia'),
    path('parroquia/<int:id>/', views.obtener_parroquia, name='obtener_parroquia'),
    path('parroquia/editar/<int:id>/', views.editar_parroquia, name='editar_parroquia'),
    
    path('barrio/crear/', views.crear_barrio, name='crear_barrio'),
    path('barrio/<int:id>/', views.obtener_barrio, name='obtener_barrio'),
    path('barrio/editar/<int:id>/', views.editar_barrio, name='editar_barrio'),
]
