from django.db import models

class Parroquia(models.Model):
    # Opciones para ubicación
    OPCIONES_UBICACION = (
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    )
    
    # Opciones para tipo
    OPCIONES_TIPO = (
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    )

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10, choices=OPCIONES_UBICACION)
    tipo = models.CharField(max_length=10, choices=OPCIONES_TIPO)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Barrio(models.Model):
    # Opciones para el número de parques
    OPCIONES_PARQUES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )

    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField(verbose_name='número de viviendas')
    numero_parques = models.IntegerField(choices=OPCIONES_PARQUES, verbose_name='número de parques')
    numero_edificios_residenciales = models.IntegerField(verbose_name='número de edificios residenciales')
    
    # Relación de Muchos a Uno con Parroquia
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return f"{self.nombre} - Parroquia: {self.parroquia.nombre}"


class Presidente(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    
    # Relación Uno a Uno con Barrio
    barrio = models.OneToOneField(Barrio, on_delete=models.CASCADE, related_name='presidente')

    def __str__(self):
        return f"{self.nickname} - Presidente de {self.barrio.nombre}"
