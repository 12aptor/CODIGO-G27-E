from rest_framework import generics
from .models import *
from .serializers import *

class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ManageServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BarberView(generics.ListCreateAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer

class ManageBarberView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer