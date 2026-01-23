from django.urls import path
from .views import *

urlpatterns = [
    path('appointments/', AppointmentView.as_view()),
    path('payments/<int:appointment_id>/', PaymentView.as_view())
]