from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

validador = Marshmallow()
conexion = SQLAlchemy()

#todo el uso de todas las clases, se crea una sola instancia