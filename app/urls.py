from django.urls import path

from . import views

urlpatterns = [
    path('suma/<int:n1>/<int:n2>', views.suma, name='suma'),
    path('resta/<int:n1>/<int:n2>', views.resta , name='resta'),
    path('multiplicacion/<int:n1>/<int:n2>', views.multiplicacion, name='multiplicacion')
]