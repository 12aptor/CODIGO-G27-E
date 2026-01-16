from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    document_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'customers'

class Appointment(models.Model):
    appointment_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='appointments'
    )
    barber = models.ForeignKey(
        'services.Barber',
        on_delete=models.CASCADE,
        db_column='barber_id',
        related_name='appointments'
    )
    service = models.ForeignKey(
        'services.Service',
        on_delete=models.CASCADE,
        db_column='service_id',
        related_name='appointments'
    )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='appointments'
    )

    class Meta:
        db_table = 'appointments'

class Payment(models.Model):
    amount = models.FloatField()

    METHOD_CHOICES = (
        ('CREDIT_CARD', 'CREDIT_CARD'),
        ('CASH', 'CASH'),
        ('YAPE', 'YAPE')
    )

    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    appointment = models.ForeignKey(
        'Appointment',
        on_delete=models.CASCADE,
        db_column='appointment_id',
        related_name='payments'
    )

    class Meta:
        db_table = 'payments'