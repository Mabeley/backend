from config import conexion
from sqlalchemy import Column, types

class Categoria(conexion.Model):
    id= Column(type_=types.Integer,primary_key=True, autoincrement=True)
    nombre= Column(type_=types.String(length=45),nullable=False)