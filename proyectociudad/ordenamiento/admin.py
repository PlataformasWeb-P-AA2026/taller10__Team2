from django.contrib import admin

from ordenamiento.models import Parroquia, Barrio, Presidente

admin.site.site_header = "Sistema de Ordenamiento Territorial"
admin.site.site_title = "Sistema de Ordenamiento Territorial"
admin.site.index_title = "Administración - Parroquias, Barrios y Presidentes"

# Se crea una clase que hereda de ModelAdmin para el modelo Parroquia
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)

# admin.site.register se lo altera
admin.site.register(Parroquia, ParroquiaAdmin)


# Se crea una clase que hereda de ModelAdmin para el modelo Barrio
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    search_fields = ('nombre', 'parroquia__nombre')

admin.site.register(Barrio, BarrioAdmin)


# Se crea una clase que hereda de ModelAdmin para el modelo Presidente
class PresidenteAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'cedula', 'edad', 'profesion', 'barrio')
    search_fields = ('nickname', 'cedula')
    # Permite acceder a una interfaz para buscar el barrio
    raw_id_fields = ('barrio',)

admin.site.register(Presidente, PresidenteAdmin)
