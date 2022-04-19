from .models import Plato
from rest_framework.generics import ListCreateAPIView
from . serializers import PlatoSerializer
from rest_framework.permissions import (AllowAny, #sirve para que el controlador sea 
                                        #publico(no se necesite una token)
                                    IsAuthenticated, #solamente para los metodos GET no sera necesaria la token pero
                                    #para los demas metodos(POST,PUT,DELETE,PATCH) si sera requerido
                                    IsAuthenticatedOrReadOnly, 
                                    #verifica que en la token de acceso buscara al usuario y vera si es superuser(is_superuser)
                                    IsAdminUser
                                    )
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
class PlatoApiView(ListCreateAPIView):
    serializer_class =PlatoSerializer
    queryset= Plato.objects.all()
    #sirve para indicar que tipos de permisos necesita el cliente
    #para poder realizar la peticion
    permission_classes =[IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        data=self.serializer_class(instance=self.get_queryset(),many=True)
        #hacer una iteracion para modificar la foto de cada plato y devolver el link de la foto
        print(data.data[0].get('foto'))
        link=CloudinaryImage(data.data[0].get('foto')).image(secure=True)
        print(link)
        return Response(data={data.data})