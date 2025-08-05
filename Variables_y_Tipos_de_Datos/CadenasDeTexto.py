print ('\n Cadenas de Texto')

print ("\nConcatenar: ")

nombre = "Pedro"
saludos = ('Hola,'+ nombre)

print (saludos) # imprime: Hola, Pedro

#

print ("\nRepetir")

print ("ja" * 3) # imprime: jajaja

#

print ("\nAcceder por indice")

texto = 'Descuajeringar'

print (texto[0]) # imprime el primer caracter

print (texto[-1]) # imprime el ultimo caracter

print (texto[6:15]) # imprime los caracteres desde y hasta las posicion qque se indique

#

print ('\nf')

name = 'Pepe'

print (f'Tu nombre es {name}')

#

print ("\nAlgunos metodos utiles para los str:")

mensaje= 'Jugo de Maracuya con Leche'

print (mensaje.lower()) # jugo de maracuya con leche

print (mensaje.upper()) # JUGO DE MARACUYA CON LECHE

print (mensaje.strip()) # "Jugo de Maracuya con Leche" (quita espacios externos)

print (mensaje.replace('Maracuya', 'Mora')) # Jugo de Mora con Leche

print (len(mensaje)) # 26 (cuenta los caracteres, tambien los espacios)