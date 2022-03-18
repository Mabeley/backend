#las tablas que queremos en python se representan en forma de clases y cada columna sera su atributo
#create table ingredientes(id int primary key.......)

from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
    #ahora esta clase tendra un comportamiento en forma de un model (tabla en la bd)
    #id> seria considerada como una columna de mi modelo (tabla) ingrediente
    id = Column(type_= types.Integer, primary_key = True,autoincrement = True)
    nombre = Column(type_= types.String(45), nullable = False, unique = True)

    __tablename__ = 'ingredientes'