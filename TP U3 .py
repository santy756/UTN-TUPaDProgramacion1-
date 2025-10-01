from statistics import mode, median, mean
import random



#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#edad_usuario = int(input("Ingrese su edad: "))
#edad_minima = 18

#if (edad_usuario>=edad_minima):
#    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

#notaUsuario = int(input("Ingrese su nota: "))
#notaMinima = 6

#if (notaUsuario >= notaMinima):
#    print ("Aprobado")
#else:
#    print("Desaprobado")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.


#numeroUsuario = int(input("Ingrese un numero par: "))


#if(numeroUsuario % 2==0) :
#      print ("Ha ingresado un número par")
#else:
#     print ("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#edad = int(input("Ingrese su edad: "))

#if edad < 12:
#    print("Niño/a: menor de 12 años.")
#elif edad >= 12 and edad < 18:
#    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
#elif edad >= 18 and edad < 30:
#    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
#else:
#    print("Adulto/a: mayor o igual que 30 años.")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

# stringUsuario = input("Ingrese su contraseña: ")
# longitud = (len(stringUsuario))
   
# if (longitud>=8 and longitud<=14):
#    print("Ha ingresado una contraseña correcta")
# else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.


# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios)
# mediana= median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)


# print (f"La media es: {media}, la mediana: {mediana},Moda: {moda}"
#        )
# if ((media>mediana) and (mediana>moda)):
#     print("Sesgo positivo o a la derecha ")
# elif ((media<mediana) and (mediana<moda)):
#     print("Sesgo negativo o a la izquierda ")
# elif((media==mediana) and (mediana==moda)):
#     print ("Sin sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.


# palabraUsuario = input("Por favor, ingrese una palabra: ")
# ultimaLetra = palabraUsuario [-1].lower()
# vocales = "aeiou"

# if (ultimaLetra in vocales):
#     print(f"{palabraUsuario}"+ "!")
# else:
#     print(f"{palabraUsuario}")


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# informacionUsuario = input("Ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: \n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. :\n")
# mayus = "1"
# miniscula ="2"
# primeraMayus = "3"

# if (mayus in informacionUsuario):
#     print(informacionUsuario.upper())
# elif(miniscula in informacionUsuario):
#     print(informacionUsuario.lower())
# elif (primeraMayus in informacionUsuario):
#     print(informacionUsuario.title())
# else:
#     print("Por favor ingrese una opcion valida.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitudUsuario = input("Ingrese el numero que represente la magnitud: ")
# magnitudUsuario = float(magnitudUsuario)

# if (magnitudUsuario<=3) :
#     print("Muy leve (imperceptible)")
# elif(magnitudUsuario>=3 and magnitudUsuario <4):
#     print("Leve (ligeramente perceptible)")
# elif(magnitudUsuario>=4 and magnitudUsuario<5):
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif(magnitudUsuario>=5 and magnitudUsuario<6):
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif(magnitudUsuario>=6 and magnitudUsuario<7):
#     print("Muy Fuerte")
# elif(magnitudUsuario>=7):
#     print("Extremo (puede causar graves daños a gran escala)")
# else:
#     print("Por favor ingrese")


#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# Programa para determinar la estación del año según el hemisferio

# hemisferio = input("En qué hemisferio te encuentras? (N/S): ").upper()
# mes = int(input("Ingresa el número del mes (1-12): "))
# dia = int(input("Ingresa el día del mes: "))

# estacion = ""

# # Condiciones para el hemisferio norte
# if hemisferio == "N":
#     if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#         estacion = "Primavera"
#     elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#         estacion = "Verano"
#     else:
#         estacion = "Otoño"

# # Condiciones para el hemisferio sur
# elif hemisferio == "S":
#     if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#         estacion = "Otoño"
#     elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#         estacion = "Invierno"
#     else:
#         estacion = "Primavera"
# else:
#     print("Hemisferio no válido.")

# if estacion:
#     print(f"En el hemisferio {hemisferio} en la fecha {dia}/{mes}, la estación es {estacion}.")


