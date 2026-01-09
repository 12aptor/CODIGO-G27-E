from django.urls import path
from .views import index, get_date

urlpatterns = [
    path('', index, name='index'),
    path('date/', get_date, name='get_date'),
]