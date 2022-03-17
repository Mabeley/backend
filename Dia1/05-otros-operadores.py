#OPERADORES DE COMPARACION
numero1 , numero2 = 10, 20
#NOTA: en python no tenemos el triple igual
#=== en javascript compara el tipo de dato y el contenido
#IGUAL QUE
print(numero1 == numero2)
#MAYOR QUE | MAYOR IGUAL QUE
print(numero1>numero2)
print(numero1>=numero2)

#MENOR QUE | MENOR IGUAL QUE
print(numero1<numero2)
print(numero1<=numero2)

#DIFERENTE DE 
print(numero1 != numero2)



#operadores logicos
#sirve para comparar varias comparaciones
#en js se utiliza && en python se utiliza la palabra and
#en js se utiliza || en python se utiliza la palabra or
print((10>5) and (10< 20))

#en el AND todo tiene que ser verdadero para que el resultado sea verdader
print((10>5) or (10< 20))
#en el OR al menos una condicion tiene que ser verdadera para que el resultado final sea verdadero


#OPERADORE DE IDENTIDAD
#IS 
#IS NOT
# sirve para ver si estan apuntando a la misma direccion de memoria
verduras=['api','lechuga','zapallo']
verduras2 = verduras