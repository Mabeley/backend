from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngredientesController, PruebaController
from config import conexion, validador

app = Flask(__name__)
#creamos la instancia de flask_restfull.Api y le indicamos toda
#la configuracion que haremos se agrege a nuestra instancia de Flask
api= Api(app=app)

#aap.config > acac se alamcenara todas las variables de configuracion de mi proyecto flask, en ella se podran encontrar algunas variables como DEBUG y ENV
#APP.config ES UN DICCIONARIO EN EL CUAL SE ALMACENARAN LAS VARIABLES POR LLAVE: VALOR
print(app.config)


#APP.config> SE ASIGNA LA CADENA DE CONEXION A NUESTRA BASE DATOS
#tipo://usuario:password@dominio:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:H4ku@127.0.0.1:3306/recetario'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#sqlalchemy_track_modification> si se establece True entonces SQLALCHEMY rastreara las modificaciones de los objetos (modelos)
#y emitiran señales cuando cambie algun modelo, su valor por defecto es none

#para jalar la configuracion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)
validador.init_app(app)
#validador> para jalar la configuracion de mi flask y poder agregar la validacion a nuestro proyecto
#create_all> con este comando indicaremos la creacion de todas las tablas en la bd
#emitira un error si es que no hay ninguna tabla a crear
#emitira un error si no le hemos instalado el conector correctamente
#tenemos que declarar en el parametro app nuestra aplicacion de flask
conexion.create_all(app=app)

@app.route('/status', methods = ['GET'])
def status():
    return{
        'status':True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
@app.route('/')
def inicio():
    return 'Bienvenido a mi Api de recetas'

#Ahora definimos las rutas que van a ser utilizadas con un determinado controlador
api.add_resource(IngredientesController,'/ingredientes','/ingrediente')
api.add_resource(PruebaController,'/pruebas')


#comprobara que la clase Flask se este ejecutando en el archivo principal
#del proyecto, esto se usa para no crear multiples instancias y generar 
#un posible error de Flask

if __name__ == '__main__':
    app.run(debug=True)

print('Hola')

#2:18