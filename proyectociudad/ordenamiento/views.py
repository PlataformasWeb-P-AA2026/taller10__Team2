from django.shortcuts import render, get_object_or_4000, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm
from django.db.models import Sum

# Listar Parroquias y sus detalles complejos
def listar_parroquias(request):
    parroquias = Parroquia.objects.all()
    
    # Añadimos datos calculados dinámicamente en Python para cada parroquia
    for p in parroquias:
        p.total_parques = p.barrios.aggregate(Sum('parques'))['parques__sum'] or 0
        p.profesiones_presidentes = [b.presidente.profesion for b in p.barrios.all() if hasattr(b, 'presidente')]
        
    return render(request, 'ordenamiento/listar_parroquias.html', {'parroquias': parroquias})

# Listar Barrios
def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'ordenamiento/listar_barrios.html', {'barrios': barrios})

# CRUD Parroquia
def crear_parroquia(request):
    form = ParroquiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_parroquias')
    return render(request, 'ordenamiento/form_parroquia.html', {'form': form, 'accion': 'Crear'})

def editar_parroquia(request, pk):
    parroquia = get_object_or_404(Parroquia, pk=pk)
    form = ParroquiaForm(request.POST or None, instance=parroquia)
    if form.is_valid():
        form.save()
        return redirect('listar_parroquias')
    return render(request, 'ordenamiento/form_parroquia.html', {'form': form, 'accion': 'Editar'})

# CRUD Barrio
def crear_barrio(request):
    form = BarrioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_barrios')
    return render(request, 'ordenamiento/form_barrio.html', {'form': form, 'accion': 'Crear'})

def editar_barrio(request, pk):
    barrio = get_object_or_404(Barrio, pk=pk)
    form = BarrioForm(request.POST or None, instance=barrio)
    if form.is_valid():
        form.save()
        return redirect('listar_barrios')
    return render(request, 'ordenamiento/form_barrio.html', {'form': form, 'accion': 'Editar'})