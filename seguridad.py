from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autenticador(username, password):
    #funcion encargada de validar si nuestras credenciales son correctas
    pass
    #primero valido si los parametros son correctos
    if username and password:
        #buscare el usuario en la base de datos
        usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=username).first()
        if usuarioEncontrado:
            #ahora valido si la password es la correcta
            validacion = checkpw(bytes(password,'utf-8'),
                                 bytes(usuarioEncontrado.password, 'utf-8'))
            if validacion is True:
                return usuarioEncontrado
            else:
                return None
        else:
            return None
    else:
        return None

def identificador(payload):
    #sirve para validar al usuario previamente autenticado
    usuarioEncontrado : Usuario | None = conexion.session.query(
        Usuario).filter_by(id=payload['identity']).first()
    if usuarioEncontrado:
        return{
            'id':usuarioEncontrado.id,
            'nombre':usuarioEncontrado.nombre,
            'correo':usuarioEncontrado.correo
        }
    else:
        return None