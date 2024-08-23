from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Pago_semanal(request, pagoPorHora, horasTrabajadas):
    pagoPorHora = float(pagoPorHora)
    horasTrabajadas = float(horasTrabajadas)
    if horasTrabajadas <= 40:
        pagoSemanal = float(pagoPorHora) * float(horasTrabajadas)
    elif horasTrabajadas > 40:
        pagoSemanal = (float(pagoPorHora)*2) * float(horasTrabajadas)
    return HttpResponse(f"El pago semanal es: ${pagoSemanal}")