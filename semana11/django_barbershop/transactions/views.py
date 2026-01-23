from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment, Appointment
from .serializers import AppointmentSerializer
import requests
import os
from datetime import datetime

class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

def generarFactura(appointment):
    precio_unitario = appointment.service.price
    total = appointment.service.price
    valor_unitario = precio_unitario / 1.18
    subtotal = total / 1.18
    igv = total - subtotal

    items = []
    item = {
        'unidad_de_medida': 'ZZ',
        'codigo': 'S-001',
        'descripcion': appointment.service.name,
        'cantidad': 1,
        'valor_unitario': valor_unitario,
        'precio_unitario': precio_unitario,
        'subtotal': subtotal,
        'tipo_de_igv': 1,
        'igv': igv,
        'total': total,
        'anticipo_regularizacion': False,
    }
    items.append(item)

    data = {
        'operacion': 'generar_comprobante',
        'tipo_de_comprobante': 2,
        'serie': 'BBB1',
        'numero': 1,
        'sunat_transaction': 1,
        'cliente_tipo_de_documento': 1,
        'cliente_numero_de_documento': appointment.customer.document_number,
        'cliente_denominacion': appointment.customer.name,
        'cliente_direccion': appointment.customer.address,
        'cliente_email': appointment.customer.email,
        'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
        'moneda': 1,
        'porcentaje_de_igv': 18.0,
        'total_gravada': subtotal,
        'total_igv': igv,
        'total': total,
        'enviar_automaticamente_a_la_sunat': True,
        'enviar_automaticamente_al_cliente': True,
        'items': items
    }

    response = requests.post(
        url=os.getenv('NUBEFACT_API_URL'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv('NUBEFACT_TOKEN')}'
        },
        json=data
    )
    json = response.json()
    status = response.status_code

    if status != 200:
        raise Exception(json['errors'])
    
    return json

class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            appointment_id = kwargs.get('appointment_id')
            appointment = Appointment.objects.get(id=appointment_id)

            if not appointment:
                raise Exception('Appointment not found')

            nubefact_json = generarFactura(appointment)

            payment = Payment(
                amount=appointment.service.price,
                method='YAPE',
                appointment=appointment
            )
            payment.save()

            return Response(nubefact_json, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)