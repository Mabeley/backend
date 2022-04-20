from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class SoloAdminPuedeEscribir(BasePermission):
    #si queremos modificar el mensaje de error en el caso no se cumpla las condiciones haciendo
    #el uso del atributo
    message ="Este usuario no tiene permisos"
    #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    def has_permission(self, request:Request, view):
        #es la vista a la cual intenta acceder el usuairo, esto dependera de donde se 
        #coloque el middleware
        #Middleware> es un intermediario entre la peticion del front y la logica final 
        #(se encargara de validar si cumple o no cumple determinados reqs y si no cumple
        # no podra continuar)
        # el request nos dara toda la informacion de los atributos de la 
        #peticion en los custom permission SIEMPRE hay que retornar True o False para
        #indicar si cumple o no cumple con los permisos determinados
        #request.user> me brindara la informacion del usuario autenticado
        print(request.user)
        print(request.user.nombre)
        print(request.user.rol)
        print(request.auth)
        print(SAFE_METHODS)
        #SAFE_METHOD> son los metodos que el usuairo no podra modificar la informacion
        #del backend son GET, HEAD OPTIONS
        #auth>imprimira la token de autenticavion que se usa para esta solicitud (request)
        if request.method in SAFE_METHODS: 
            return True
        else:
            return request.user.rol == 'ADMINISTRADOR'
        # return request.user.rol =='ADMINISTRADOR'
        # if request.user.rol == 'ADMINISTRADOR':
        #     return True
        # else:
        #     return False

class  SoloMozoPuedeEscribir(BasePermission):
    def has_permission(self, request:Request, view):
        if request.method == SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'MOZO'