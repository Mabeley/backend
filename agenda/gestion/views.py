# render> este render sirve para renderizar una plantilla html
#from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView
from .serializers import PruebaSerializer, TareasSerializer, EtiquetaSerializer, TareaSerializer, ArchivoSerializer, EliminarArchivoSerializer
from .models import Etiqueta, Tareas
from rest_framework import status
#son un conjunto de librerias que django nos provee para poder utilizar de una manera
#mas rapida ciertas configuraciones, timezone sirve para en base a la configuracion que 
#colocamos en el settins.py TIME_ZONE se basara en esta para darnos la hora y fecha con esa configuracion
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import remove
from django.conf import settings

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
    serializer_class= TareasSerializer

    def post(self, request: Request):
        #serializo la data para validar sus valores y su configuracion
        serializador = self.serializer_class(data=request.data)
        #llamo al metodo validar que retornara True si cumple o False si no
        if serializador.is_valid():
            #serializador.initial_data > data inicial sin la validacion
            #serializador.validated_data> data ya validada(solo se puede llamar
            #luego de llamar al metodo is_valid())
            #validare que la fehca_caducidad no sea menor que hoy
            fechaCaducidad= serializador.validated_data.get('fechaCaducidad')
            print(type(serializador.validated_data.get('fechaCaducidad')))
            #validar que la importancia sea entre 0 y 10
            importancia= serializador.validated_data.get('importancia')
            if importancia <0 or importancia >10:
                return Response (data ={
                    'message':'La importancia puede ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)
            if timezone.now()> fechaCaducidad:
                return Response(data={
                    'message':'La fecha no puede ser menor que la fecha actual'
                }, status=status.HTTP_400_BAD_REQUEST)
            serializador.save()
                #STATUS> https://www.django-rest-framework.org/api-guide/status-codes/#status-codes
            return Response(data=serializador.data, status = status.HTTP_201_CREATED) #created
        else:
            serializador.errors
            return Response(data={
                'message':'La data no es valida',
                'content': serializador.errors},
                status = status.HTTP_400_BAD_REQUEST)
class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class= EtiquetaSerializer

class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=TareaSerializer
    queryset =Tareas.objects.all()

class ArchivosApiView(CreateAPIView):
    serializer_class = ArchivoSerializer
    def post(self, request: Request):
        print(request.FILES)
        queryParams = request.query_params
        carpetaDestino = queryParams.get('carpeta')
        data= self.serializer_class(data = request.FILES)
        if data.is_valid():
            print(type(data.validated_data.get('archivo')))
            archivo: InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.size)
            #solamente subir imagenes de hasta 5MB
            #5(bytes) * 1024 > (kb) * 1024 > Mb
            #5*1024*1024 >
            if archivo.size>(5*1024*1024):
                return Response(data={
                    'message':'Archivo muy grande, no puede ser mas de 5Mb'
                }, status=status.HTTP_400_BAD_REQUEST)
            #default_storage>> https://docs.djangoproject.com/en/4.0/topics/files/#storage-objects
            resultado =default_storage.save(
                (carpetaDestino+'/' if carpetaDestino is not None else '')+archivo.name, ContentFile(archivo.read()))
            #el metodo read() lee archivos, pero la lectura hara que tambien se elimine
            #de la memoria temporal, asi q por ende no se puede llamar dos o mas veces a este metodo
            #ya que en la segunda no tendremos archivo que mostrar
            print(resultado)
            return Response(data={
                'message': 'archivo guardado exitosamente',
                'content': {
                    'ubicacion': resultado
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al subir la imagen',
                'content':data.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
#        
class EliminarArchivoApiView(DestroyAPIView):
    #el generico DestroyAPIView solicita una pk como parametro de la url 
    #para eliminar un determinado registro de un modelo personalizara 
    #para no recibir ello
    serializer_class = EliminarArchivoSerializer
    def delete(self, request: Request):
        data= self.serializer_class(data = request.data)
        try:
            data.is_valid(raise_exception=True)
            ubicacion =data.validated_data.get('archivo')
            remove(settings.MEDIA_ROOT/ ubicacion)
            return Response(data={
                'message':'Archivo eliminado exitosamente'
            })
            # else:
            #     return Response(data={
            #         'message': 'Error al eliminar el archivo',
            #         'content':data.errors
            #     })
        except Exception as e:
            return Response(data={
                'message':'Error al eliminar el archivo',
                'content':e.args
            },status = status.HTTP_400_BAD_REQUEST)