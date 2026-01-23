from .models import Appointment, Customer
from rest_framework import serializers
from services.serializers import BarberSerializer, ServiceSerializer
from authentication.serializers import UserSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['barber'] = BarberSerializer(instance.barber).data
        representation['service'] = ServiceSerializer(instance.service).data
        representation['user'] = UserSerializer(instance.user).data
        return representation

    def create(self, validated_data):
        print(validated_data)
        customer = validated_data.pop('customer')
        customer_instance, _ = Customer.objects.get_or_create(
            email=customer.get('email'),
            document_number=customer.get('document_number'),
            defaults=customer
        )

        appointment_instance = Appointment.objects.create(
            customer=customer_instance,
            **validated_data
        )

        return appointment_instance