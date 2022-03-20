from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba, ValidarUsuarioPrueba
from dtos.ingrediente_dto import IngredienteRequestDTO, IngredienteResponseDTO
from marshmallow.exceptions import ValidationError
#todos los metodos HTTP que vamos a utilizar se define como metodos
#de la clase
class IngredientesController(Resource): 
    def get(self):
        #sesion.query> vamos a crear una sesion en la cual ejecutaremos una query
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        #many= True>si nosotros queremos convertir la informacion y es mas de una
        #con esto el DTO iterara cada uno de los items y lo serializara al valor correcto
        ingredientesSerializados = IngredienteResponseDTO(many=True).dump(resultado)
        return{
            'message':'Yo soy el get de los ingredientes',
            'content': ingredientesSerializados
                }
    def post(self):
        print(request.get_json())
        #registramos un nuevo ingrediente
        data = request.get_json()
        
        try:
            #validara que la data que el usuario me esta enviando cumpla con todos las
            #caracteristicas de mi modelo(que sea un string, que no sea muy largp(mas de 45))
            data_serializada = IngredienteRequestDTO().load(data)
            print(data_serializada)
            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre= data_serializada.get('nombre')
            #ahora guardo la informacion en la base de datos
            conexion.session.add(nuevoIngrediente)
            #add> estamos creando una nueva transaccion
            #commit> sirve para guardar los cambios de manera permanete en la bd
            conexion.session.commit()
            ingredienteSerializado = IngredienteResponseDTO().dump(nuevoIngrediente)
            return{
                'message': 'Ingrediente creado exitosamente',
                'ingrediente': ingredienteSerializado
            }, 201
        except ValidationError as e:
            return{
                'message':'La informacion es incorrecta',
                'content': e.args
            },400 # bad request(mala solicitud)
        except Exception as e:
            
            print(e.args[0])
            #si hubo un erros al momento de hacer alguna modificacion a la bd
            #entonces 'retrocedemos' todos esas modificaciones y lo dejaremos sin ningun cambio
            conexion.session.rollback()
            return{
                'message': 'Hubo un error al crear el ingrediente',
                'content': e.args[0]
            },500 #internal server error

class PruebaController(Resource):
    def post(self):
        try:
            data = request.get_json()
            validacion = ValidadorPrueba().load(data)
            print(validacion)
            return{
                'message':'ok',
                'data': validacion
            }
        except Exception as e:
            print(e.args)
            return{
                'message': 'error al recibir datos',
                'content': e.args
            }           
    def get(self):
        usuario={
            'nombre':'Mabel',
            'apellido':'cisneros',
            'nacionalidad':'Peru',
            'password': 'mamma'
        }
        resultado = ValidarUsuarioPrueba().dump(usuario)
        return{
            'message': 'EL usuario es',
            'content' : usuario,
            'resultado':resultado
        }


class IngredienteController(Resource):
    def get(self,id):
        #filter_by> tenemos que indicar dentro de ese metodo las clumnas que queremos
        #usar para hacer el filtro con su respectivo valor el parametro sera el nombre 
        #del atributo definido definido en el modelo y el segundo sera el valor
        #SELECT TOP1 = FROM INGREDIENTES where ID = $ID
        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        print(ingrediente)
        if ingrediente:
            #mando a llamar a mi DTO de respuesra del ingrediente1
            resultado = IngredienteResponseDTO().dump(ingrediente)
            return{
                'result': resultado
            }
        else:
            return{
                'message': 'El ingrediente a buscar no existe'
            },404

    def put(self, id):
        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        try:
            if ingrediente:
                body=request.get_json()
                #validadmos la data enviada por el usuario para que cumpla con lo definido en el DTO
                data_validada = IngredienteRequestDTO().load(body)
                #al ya validar nuestro ingrediente y que este exista procedemos a modificar sus columnas
                #(solo seria nombre) con el nuevo valor enviado por el usuario previamente ya validado
                ingrediente.nombre =data_validada.get('nombre')
                #solamente hacemos un commit ya que no estamos agregando nuevos valores a la base de datos
                conexion.session.commit()
                #usando el DTO de response pasar el ingrediente que me devuelva su informacion para 
                # agregarla en el content de la respuesta
                #dump> dame la info
                resultado = IngredienteResponseDTO().dump(ingrediente)
                return{
                    'message':'Ingrediente actualizado exitosamente',
                    'content': resultado
                }
            else:
                return{
                    'message':'Ingrediente a actualiza no existe'
                }, 404
        except Exception as e:
            return{
                'message':'Error al actualizar el ingrediente',
                'content': e.args
            },400