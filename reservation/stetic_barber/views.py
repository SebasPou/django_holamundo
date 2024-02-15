from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reservation(request):
    return HttpResponse('Hola Mundo')
    

def home(request):
    template = 'index.html'
    servicios = [
        {'nombre':'Corte de cabello hombre', 'detalles':'pelo corto', 'precio':'5$'},
        {'nombre':'Corte de cabello mujer', 'detalles':'solo puntas', 'precio':'8$'},
        {'nombre':'pintado de cabello', 'detalles':'rayos color rojo', 'precio':'10$'},
        {'nombre':'manicura', 'detalles':'manicura', 'precio':'5$'},
    ]
    return render(request, template, {'servicios': servicios})


def servicios(request, nombre):
    template= 'servicios.html'
    contenido = {
        'mesaje':'Informacion de servicios',
        'titulo': nombre,
        
    }
    return render(request, template, contenido)