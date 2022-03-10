#Esto es un comentario y sirve para dar contexto de que se hace, se hizo o se hara 
#TODO: logica para este controlador

#variables de texto
nombre = 'eduardo'
apellido="de'rivero"

#si queremos tener un texto que pueda contener saltos de linea
descripcion = """hola amigos:
como estan"""

descripcion2 = '''Hola amigos:
como estan?'''
print (descripcion)
print (descripcion2)
#variable numericas
year = 2022
edad = 30
#type()> mostrara que tipo de variable es
print(type(year))
print(type(descripcion))

#python no se puede crear una variable sin un contenido a excepcion del None
#en pyhton None = null / undefined
especialidad = None
#en python no existen las constantes
dni = [1232323]
dni='peruano'
dni= False
#pinrt(id())> dara la ubicacion de esa variable en relacion a la memoria del dispositivo
print(id(dni))

print(type(especialidad))


mes , dia = "febrero", 28
print(mes)
#del> elimina la variable de la memoria
del mes
#si queremos usar luego de la eliminacion esa variable no sera posible ya que se elimino de la memoria
print(mes)