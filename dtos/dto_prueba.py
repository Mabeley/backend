from config import validador
from marshmallow import fields, validate

#este es el valiidaro de request =solicitud
class ValidadorPrueba(validador.Schema):
    nombre = fields.Str(validate =validate.Length(max=10))
    apellido = fields.Str()
    edad = fields.Int()
    soltero = fields.Bool()
    #class Meta:
        #es una clase que va ser para poder pasar parametros a la metadada del padre 
        #(de la clase de la cual estamos heredando), definimos atributos que van a servir a la clase
        #schema para poder hacer la validacion correcta
        #en el atributo fields iran lo que seria que valores necesitamos esperar del cliente
        #fields = ['nombre','apellido']


#validador de respoonse
class ValidarUsuarioPrueba(validador.Schema):
    nombre= fields.Str()
    apellido= fields.Str()

    

