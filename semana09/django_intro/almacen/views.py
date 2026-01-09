from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from .models import Producto

def index(request):
    return HttpResponse("👻 Bienvenido a mi aplicación de Django")

def get_date(request):
    date = datetime.now()
    html = f'<h1>Fecha y hora actuales: {date}</h1>'
    return HttpResponse(html)

def get_json(request):
    user = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@gmail.com',
        'age': 30
    }
    return JsonResponse(user)

def get_html(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})