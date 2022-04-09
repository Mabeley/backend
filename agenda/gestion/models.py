from datetime import datetime
from distutils.command.upload import upload
from tkinter.tix import INTEGER
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

class Tareas(models.Model):

    class CategoriaOpciones(models.TextChoices):
        #cada opcion le podemos pasar dos parametros en la cual el primero sera su abreviatura
        #para que se guarde en la bd y el segundo el nombre completo que se mostrara cuando
        #querramos utilizar los valores en un formulario usando Templates (Jinja) o dentro del 
        #formulario de DRF
        TODO = 'TODO','TO_DO'
        IN_PROGRESS = 'IP', 'IN_PROGRESS'
        DONE = 'DONE', 'DONE'
        CANCELLED = 'CANCELED', 'CANCELLED'


    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45, null=False)
    #Forma I usando una subclase que herede de TextChoices
    categoria = models.CharField(max_length=45, choices =CategoriaOpciones.choices,
    default=CategoriaOpciones.TODO)
     #Forma II usando una lista de tuplas
    # categoria =models.CharField(max_length=45, choices=[
    #     ('TODO','TO_DO'),
    #     ('IP','IN_PROGRESS')
    #     ('DONE', 'DONE')
    #     ('CANCELED', 'CANCELLED')
    #     ], default='TODO')
    fechaCaducidad= models.DateTimeField(db_column='fecha_caducidad')
    importancia=models.IntegerField(null=False)
    descripcion = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    #En Django se puede utilizar las relaciones one-to -one, one-to-many o many-to-many
    #para crear las relaciones entre las tablas, aca ya no es necesario usar las relashionship
    #porque ya estan integradas dentro de la relacion
    etiquetas =models.ManyToManyField(to=Etiqueta, related_name = 'tareas')
    foto = models.ImageField(
    #el ImageField sirve para guardar la ubicacion en donde se almacenara mi imagen en el servidor
        #https://docs.djangoproject.com/en/4.0/ref/models/fields/#imagefield
        upload_to='multimedia',
        null = True
        )
    class Meta:
        db_table = 'tareas'
#si la tbala tareas_etiquetas no fuese una tabla pivote, detalle entonces tendria que 
#que crear la tabla como si fuese una tabla comun y corriente
#class TareasEtiquetas(models.Model):
#...
#etiquetasFK= models.ForeignKey(to=Etiqueta)
#tareaFK=models.ForeignKey(to=Tareas)
#las demas columnas