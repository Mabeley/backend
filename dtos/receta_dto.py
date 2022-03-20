from config import validador
from models.recetas import Receta
class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model= Receta