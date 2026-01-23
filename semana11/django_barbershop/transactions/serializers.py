from .models import Appointment, Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'