
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
import requests
import os

def generarFactura():
    items = []
    item = {
        'unidad_de_medida': 'ZZ',
        'codigo': 'S-001',
        'descripcion': 'Corte de Cabello',
        'cantidad': 1,
        'valor_unitario': 100.00,
        'precio_unitario': 118.00,
        'subtotal': 100.00,
        'tipo_de_igv': 1,
        'igv': 18.00,
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
        'cliente_numero_de_documento': '76543219',
        'cliente_denominacion': 'Pepito Perez',
        'cliente_direccion': 'Avenida los Girasoles 123',
        'cliente_email': 'pepito@gmail.com',
        'feecha_de_emision': '01-01-2026',
        'moneda': 1,
        'porcentaje_de_igv': 18.0,
        'total_gravada': 100.00,
        'total_igv': 18.00,
        'total': 118.00,
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
            nubefact_json = generarFactura()

            payment = Payment(
                amount=100,
                method='YAPE',
                appointment_id=1
            )
            payment.save()

            return Response(nubefact_json, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)