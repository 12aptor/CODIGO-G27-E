from django.urls import path
from .views import index, get_date, get_json, get_html

urlpatterns = [
    path('', index, name='index'),
    path('date/', get_date, name='get_date'),
    path('json/', get_json, name='get_json'),
    path('html/', get_html, name='get_html'),
]