from config import validador
from models.ingredientes import Ingrediente
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate
class IngredienteRequestDTO(validador.SQLAlchemyAutoSchema):
    #nosotros heredar el SQLAlchemyAutoSchema estamos indicando que usaremos un modelo como mapeo de los atributos
    #necesarios para hacer la validacion de nuestra informacion

    #auto_field> se modifica la columna nombre de la tabla llamada y le estamos agregando la validacion
    #para que ahora su longitud minima sea de al menos 1 caracter
    nombre= auto_field(validate = validate.And(validate.Length(min=1),validate.Regexp("[A-Z][a-z]+")))
    class Meta:
        model = Ingrediente


class IngredienteResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingrediente