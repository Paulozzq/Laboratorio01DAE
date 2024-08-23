from django.shortcuts import render
from django.http import HttpResponse

def suma(request, n1, n2):
    suma = int(n1) + int(n2)
    return HttpResponse(f"La suma de {n1} y {n2} es: {suma}")
def resta(request, n1, n2):
    resta = int(n1) - int(n2)
    return HttpResponse(f"La resta de {n1} y {n2} es: {resta}")
def multiplicacion(request, n1, n2):
    multiplicacion = int(n1) * int(n2)
    return HttpResponse(f"La multiplicacion de {n1} y {n2} es: {multiplicacion}")
