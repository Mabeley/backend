from .models import Plato, Stock
from rest_framework.generics import ListCreateAPIView, ListAPIView
from . serializers import PlatoSerializer, StockSerializer, PedidoSerializer, AgregarDetallePedidoSerializer,StockCreateSerializer
from rest_framework.permissions import (AllowAny, #sirve para que el controlador sea 
                                        #publico(no se necesite una token)
                                    IsAuthenticated, #solamente para los metodos GET no sera necesaria la token pero
                                    #para los demas metodos(POST,PUT,DELETE,PATCH) si sera requerido
                                    IsAuthenticatedOrReadOnly, 
                                    #verifica que en la token de acceso buscara al usuario y vera si es superuser(is_superuser)
                                    IsAdminUser,
                                    SAFE_METHODS
                                    )
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import DetallePedido, Pedido
from rest_framework import status
from django.utils import timezone
from django.db import transaction,IntegrityError
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


class StockApiView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset=Stock.objects.all()
    permission_classes=[IsAuthenticated, SoloAdminPuedeEscribir]

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return StockCreateSerializer
        return StockSerializer


class PedidoApiView(ListCreateAPIView):
    queryset= Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes=[IsAuthenticated, SoloMozoPuedeEscribir]
    def post(self, request : Request):
            print(request.user)
            request.data['usuarioId']=request.user.id
            data = self.serializer_class(data=request.data)
            data.is_valid(raise_exception=True)
            data.save()
            return Response(data =data.data, status=status.HTTP_201_CREATED)
        

class AgregarDetallePedidoApiView(ListAPIView):
    queryset= DetallePedido.objects.all()
    serializer_class = AgregarDetallePedidoSerializer
    permission_classes=[IsAuthenticated, SoloMozoPuedeEscribir]
    def post(self, request:Request):
        #1. valido la data con el serializer
        #2. verifico que tenga esa cantidad de productos en stock
        #3. agrego el detalle
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        stock:Stock| None= Stock.objects.filter(fecha=timezone.now(),
                                    platoId=data.validated_data.get('platoId'),
                                    cantidad__gte=data.validated_data.get('cantidad')).first()

        print(stock)
        if stock is None:
            return Response(data={"message":"No hay stock para ese producto para el dia de hoy"},
                            status=status.HTTP_400_BAD_REQUEST)
        ####
        #validar si el pedido existe
        pedido: Pedido |None = Pedido.objects.filter(
            id=data.validated_data.get('pedidoId')).first()
        if pedido is None:
            return Response(data={'message': 'No hay ese pedido'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                nuevoDetalle = DetallePedido(cantidad=data.validated_data.get(
                'cantidad'), stockId= stock, pedidoId=pedido)
                nuevoDetalle.save()
                stock.cantidad = stock.cantidad- nuevoDetalle.cantidad
                stock.save()
                #agrego la cabecera
                #pedido.total +=
                pedido.total =pedido.total + (nuevoDetalle.cantidad * stock.precio_diario)
                pedido.save()
        except IntegrityError:
            return Response(data={'message':'Error al crear el pedido, todo '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #####
        return Response(data={'mensage':'Detalle agregado exitosamente'})