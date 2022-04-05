from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    #Tipos de Columnas >https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    #opciones de las columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre= models.CharField(max_length=20, unique=True, null=False)
    #Columnas de auditoria
    #son columnas que podran ayudar al seguimietno de la creacion de registros
    #createAt> es la fecha en la cual se creo el registro
    createAt= models.DateTimeField(auto_now_add=True, db_column='created_at')
    #updateAt> es la fecha en la cual se modifico algun campo del registro
    updateAt = models.DateTimeField(auto_now= True, db_column='updated_at') 
    #todas las configuraciones propias de la tabla se haran mediante la definicion 
    #de sus atributos en la clase Meta
    #https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        #cambiar el nombre de la tabla en la bd(a diferencia del nombre de la clase)
        db_table ='etiquetas'
        #modificar el ordenamiento natural (por el id)e imponiendo el propio que
        #seas ASC del nombre, solamente funcionara cuando hagamos el get usando el ORM
        ordering= ['-nombre']
