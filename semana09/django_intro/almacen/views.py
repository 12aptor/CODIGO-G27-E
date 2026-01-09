from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("👻 Bienvenido a mi aplicación de Django")

def get_date(request):
    date = datetime.now()
    html = f'<h1>Fecha y hora actuales: {date}</h1>'
    return HttpResponse(html)