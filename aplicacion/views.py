from django.shortcuts import render, redirect
from .forms import PersonaForm, AutoForm, CiudadForm
from .models import Persona, Auto, Ciudad

def index(request):
    return render(request, 'index.html')

def insertar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request, 'insertar_persona.html', {'form': form, })

def insertar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutoForm()
    return render(request, 'insertar_auto.html', {'form': form, })

def insertar_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CiudadForm()
    return render(request, 'insertar_ciudad.html', {'form': form, })


def buscar_persona(request):
    query = request.GET.get('q')

    resultados = None
    if query:
        resultados = Persona.objects.filter(nombre__icontains=query)
    return render(request, 'buscar_persona.html', {'resultados': resultados,})

def buscar_auto(request):
    query = request.GET.get('q')

    resultados = None
    if query:
        resultados = Auto.objects.filter(modelo__icontains=query)
    return render(request, 'buscar_auto.html', {'resultados': resultados,})
    
def buscar_ciudad(request):
    query = request.GET.get('q')

    resultados = None
    if query:
        resultados = Ciudad.objects.filter(nombre__icontains=query)
    return render(request, 'buscar_ciudad.html', {'resultados': resultados,})

