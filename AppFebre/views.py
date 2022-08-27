from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from AppFebre.models import Abuelo

def abuelos(request):
    abuelo1 = Abuelo( nombre='Cacho', apellido='Febre',profesion='abogado')
    abuelo1.save()
    texto=f'el nombre de mi abuelo es {abuelo1.nombre} el apellido es {abuelo1.apellido} y es {abuelo1.profesion}'
    return HttpResponse(texto)