from rest_framework import generics
from datetime import time
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

class BarberAvailableView(generics.ListAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer

    def get_queryset(self):
        day_of_week = self.kwargs['day_of_week'] # MONDAY
        hour = self.kwargs['hour'] # 13:00
        hour_time = time.fromisoformat(hour)

        return self.queryset.filter(
            schedules__day_of_week=day_of_week,
            schedules__start_time__lte=hour_time,
            schedules__end_time__gte=hour_time,
        ).distinct()

class ScheduleView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ServiceSerializer

class ManageScheduleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer