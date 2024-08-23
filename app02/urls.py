from django.urls import path

from . import views

urlpatterns = [
    path('<str:pagoPorHora>/<str:horasTrabajadas>', views.Pago_semanal, name='pagoSemanal'),
]