from django.shortcuts import render, redirect
from django.http import HttpResponse

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py
from ordenamiento.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros desde la base de datos
    """
    parroquias_db = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    
    # Calcular parques y profesiones de presidentes para cada parroquia
    lista_parroquias = []
    for p in parroquias_db:
        # numero de parques: sumar los parques de sus barrios
        parques = sum([b.numero_parques for b in p.barrios.all()])
        
        # profesiones de los presidentes
        profesiones = []
        for b in p.barrios.all():
            if hasattr(b, 'presidente'):
                profesiones.append(b.presidente.profesion)
        profesiones = list(set(profesiones)) # sin duplicados
        
        lista_parroquias.append({
            'obj': p,
            'total_parques': parques,
            'profesiones': profesiones
        })
    
    informacion_template = {
        'parroquias': lista_parroquias, 
        'numero_parroquias': len(parroquias_db),
        'barrios': barrios,
        'numero_barrios': len(barrios)
    }
    return render(request, 'index.html', informacion_template)

def obtener_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    informacion_template = {'parroquia': parroquia}
    return render(request, 'obtener_parroquia.html', informacion_template)

def obtener_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    informacion_template = {'barrio': barrio}
    return render(request, 'obtener_barrio.html', informacion_template)


def listar_parroquias(request):
    """
    """
    parroquias = Parroquia.objects.all()
    informacion_template = {
        'parroquias': parroquias
    }
    return render(request, 'listar_parroquias.html', informacion_template)


def listar_barrios(request):
    """
    """
    barrios = Barrio.objects.all()
    informacion_template = {
        'barrios': barrios
    }
    return render(request, 'listar_barrios.html', informacion_template)


def crear_parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    
    diccionario = {'formulario': formulario}
    return render(request, 'crear_parroquia.html', diccionario)


def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    
    diccionario = {'formulario': formulario}
    return render(request, 'editar_parroquia.html', diccionario)


def crear_barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    
    diccionario = {'formulario': formulario}
    return render(request, 'crear_barrio.html', diccionario)


def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    
    diccionario = {'formulario': formulario}
    return render(request, 'editar_barrio.html', diccionario)