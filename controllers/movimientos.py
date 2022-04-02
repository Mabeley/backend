from flask_restful import Resource, request
from dtos.movimiento_dto import MovimientoRequestDTO, MovimientoResponseDTO
from models.movimientos import Movimiento
from flask_jwt import jwt_required, current_identity
from config import conexion
class MovimientoController(Resource):
    @jwt_required()
    def post(self):
        body= request.get_json()
        try:
            print(current_identity)
           
            data = MovimientoRequestDTO().load(body)
             #al la data agrego la llave  usuario_id en la cual colocare el id
            #del usuario proveniente de la JWT, ya no en el body
            data['usuario_id']= current_identity.id
            nuevoMovimiento =Movimiento(**data)
            conexion.session.add(nuevoMovimiento)
            conexion.session.commit()
            resultado = MovimientoResponseDTO().dump(nuevoMovimiento)
            return{
                'message':'Movimiento creado exitosamente',
                'content': resultado
            },201
        except Exception as e:
            conexion.session.rollback()
            return{
                'message': 'Error al crear el movimiento',
                'content': e.args
            }
    @jwt_required()
    def get(self):
        current_identity #el objeto del usuario
        #busca todos los movimientos que correspónden a ese usuario
        movimientos: list[Movimiento] = conexion.session.query(Movimiento).filter_by(usuario_id = current_identity.id).all()
        resultado = MovimientoResponseDTO(many=True).dump(movimientos)
        return{
            'message':'Los movimientos son',
            'content': resultado
        }