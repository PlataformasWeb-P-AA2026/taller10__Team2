from django.contrib import admin
from .models import Parroquia, Barrio, Presidente

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'parroquia')

@admin.register(Presidente)
class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'cedula', 'profesion', 'barrio')
