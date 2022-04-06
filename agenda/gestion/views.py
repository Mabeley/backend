#render> este render sirve para renderizar una plantilla html
#from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view

@api_view(http_method_names=['GET','POST'])
def inicio(request):
    #reqeuest sera toda la informacion enviada por el cliente
    return {
        'message': 'Bienvenido a mi API de agenda'
    }
        