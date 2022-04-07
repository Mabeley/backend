# render> este render sirve para renderizar una plantilla html
#from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer, TareaSerializer
from .models import Tareas

@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    # reqeuest sera toda la informacion enviada por el cliente
    # https://www.django-rest-framework.org/api-guide/requests
    print(request.method)
    print(request)
    if request.method == 'GET':
        # comportamiento cuando sea GET
        return Response(data={
            'message': 'Bienvenido a mi API de agenda'
        })
    elif request.method == 'POST':
        # Comportamiento cuando sea POST

        return Response(data={
            'message': 'Hiciste un post'
        }, status=201)


class PruebaApiView(ListAPIView):
    # sirve para ayudarnos cuando se llame este request nos haga el trabajo de
    # serializar y de deserializar la informacion
    # (es igual q un DTO)
    serializer_class = PruebaSerializer
    #queryset es el encargado de hacer la busqueda para este controlador(para todos sus metodos )
    queryset = [{'nombre': 'Mabel',
                'apellido': 'Cisneros',
                 'correo': 'mabel_elcie@hotmail.com',
                 'dni': '25974365',
                 'estado_civil': 'soltera'},
                 {'nombre': 'Alex',
                'apellido': 'suarez',
                 'correo': 'ale.sdjfe@hotmail.com',
                 'dni': '87596412',
                 'estado_civil': 'viudo'}
                 ]

    def get(self, request:Request):
        #dentro de las vistas genericas se puede sobrescribir la logica
        #inicial del controlador
        #si modifico la logica original de cualquier generico en base a su
        #metodo a utilizar ya no sera necesario definir los atributos
        #serializer_class y queryset ya que estos se usan para cuando no
        #se modifica la logica original

        informacion= self.queryset
        #uso el serializador para filtar la infofmacion necesaria y no mostrar 
        #alguna informacion de mas pero en este caso como le voy a pasar uno
        #o mas registrso de usuario, para q el serializador los pueda serializar
        #se coloca el parametro many)True que lo que hara sera iterar
        informacion_serializada = self.serializer_class(data =informacion, many=True)
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message':'Hola',
            'content': informacion_serializada.data
            })
class TareasApiView(ListCreateAPIView):
    queryset =Tareas.objects.all() #> esto es igual a SELECT * FROM tareas;
    serializer_class= TareaSerializer
