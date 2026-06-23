from django.contrib import admin
from .models import Parroquia, Barrio, Presidente

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('ubicacion', 'tipo')

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    search_fields = ('nombre', 'parroquia__nombre')
    list_filter = ('numero_parques',)

class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'cedula', 'edad', 'profesion', 'barrio')
    search_fields = ('nickname', 'cedula', 'barrio__nombre')

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Presidente, PresidenteAdmin)
