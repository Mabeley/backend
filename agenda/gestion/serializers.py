from dataclasses import fields
from rest_framework import serializers
from .models import Etiqueta, Tareas
class PruebaSerializer(serializers.Serializer):
    #https://www.django-rest-framework.org/api-guide/fields
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni= serializers.RegexField(max_length=8, min_length=8, regex="[0-9]")
    #dni = serializer.IntegerField(min_value=10000000, max_value=99999999)


class TareasSerializer(serializers.ModelSerializer):
    # Modifico la configuracion del modelo y le puedo setear la nueva configuracion 
    # que respetera el serializador, no se puede hacer cambios de tipos de datos muy 
    # drasticos (x ejemplo: si en el modelo es un IntegerField en el serializador no
    #  podre cambiarlo a CharField porque me lanzara un error al momento de guardar la data)
    #https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    foto = serializers.CharField(max_length=100)
    class Meta:
        model =Tareas
        fields ='__all__' #estare indicando que voy a utilizar todas las columnas de mi tabla
        #exclude = ['importancia'] #indicara que columnas NO quiero utilizar
        #NOTA: no se puede utilizar los dos a la vez, es decir, o bien se usa el fields o el exclude
         # > este sirve para que en caso quedramos devolver la informacion
        #de una relacion entre este modelo podemos indicar hastq ue grado de profundidad
        #queremos que nos devuelva la informacion, la profundidad no puede ser mayor a 10
        extra_kwargs ={
            'etiquetas':{
                'write_only': True
            }
        }

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1

class EtiquetaSerializer(serializers.ModelSerializer):
    #indicare que este atributo solamente funcionara para cuando vamos a serializar la
    #data antes de devolverla mas no para cuando querramos usarla para escritura
    #se tiene que llamar igual que el related_name para poder ingresar a esa relacion
    #o podremos definir el parametro source en el cual colocaremos el nombre del relates_name
    #NOTA: no podemos utilizar el parametro source si es que tbn colocaremos el mismo valor 
    #como nombre dle atributo
    tareas = TareasSerializer(many = True, read_only = True)#, source='tareas')
    class Meta:
        model = Etiqueta
        fields = '__all__'
        #--------------------pregunta----------------
        #¿COMO PUEDO MEDIANTE UN SERIALIZADOR INDICAR QUE COLUMNAS DE DETERMINADO MODELO SERAN SOLAMENTE
        #ESCRITURA O SOLAMENTE LECTURA SIN MODIFICAR SU COMPORTAMIENTO COMO ATRIBUTO
        #DE LA CLASE???
        #extra_kwargs y read_only_fields solamente funcionaran para cuando nosotros queramos
        #modificar el comportamiento de los atributos que no los hemos modificado manualmente 
        #dentro del serializer
        extra_kwargs ={'nombre':{'write_only':True},
                        'id':{'read_only': True}}
        #read_only_fields = ['nombre']
        
        read_only_fields = ['createAt']

class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tareas
        fields ='__all__'
        #exclude =['nombre] #funciona tanto para lectura como escritura
        extra_kwargs = {
            'nombre':{
                'read_only': True
            }
        }

class ArchivoSerializer(serializers.Serializer):
    #max_length => indica la longitud mazima DEL NOMBRE DEL ARCHIVO
    #USE_URL > si es verdadero retornara el link completo de la ubicacion del archivo
    #caso contrario retornara solamente la ubicacion dentro del proyecto del archivo
    archivo = serializers.ImageField(max_length=100, use_url =True)

class EliminarArchivoSerializer(serializers.Serializer):
    archivo = serializers.CharField(max_length=100)