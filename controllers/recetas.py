from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO

#CREATE , GET ALL(PAGINATED),UPDATE, FIND por like de nombre, DELETE
class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            return{
                'message':'Receta creada exitosamente'
                
            }, 201
        except Exception as e:
            return{
                'message':'Error al crear la receta',
                'content': e.args
            }