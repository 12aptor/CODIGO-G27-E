from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>/', ManageServiceView.as_view()),
    path('barbers/', BarberView.as_view()),
    path('barbers/<int:pk>/', ManageBarberView.as_view()),
]