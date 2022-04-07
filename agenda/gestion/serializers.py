from rest_framework import serializers
from .models import Tareas
class PruebaSerializer(serializers.Serializer):
    #https://www.django-rest-framework.org/api-guide/fields
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni= serializers.RegexField(max_length=8, min_length=8, regex="[0-9]")
    #dni = serializer.IntegerField(min_value=10000000, max_value=99999999)


class TareaSerializer(serializers.ModelSerializer):
    #https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    class Meta:
        model =Tareas
        fields ='__all__' #estare indicando que voy a utilizar todas las columnas de mi tabla
        #exclude = ['importancia'] #indicara que columnas NO quiero utilizar
        #NOTA: no se puede utilizar los dos a la vez, es decir, o bien se usa el fields o el exclude
