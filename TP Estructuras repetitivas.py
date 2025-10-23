import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for i in range(101):
#        print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

# numero = int(input("Ingrese un numero entero: "))

# contador = 0

# for i in str(numero):
#     contador += 1
    
# print(f"El numero tiene {contador} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# inicio = int(input("Ingrese el numero inicial: "))
# fin = int(input("Ingrese el numero final: "))

# if inicio > fin:
#     inicio, fin = fin, inicio #Validacion para que en caso de que inicio sea mayor a fin, los valores se intercambien

# suma = 0

# for i in range(inicio +1, fin): #para cada numero dentro de inicio y fin, sumarlos en "suma", el +1 es necesario para evitar que el primero numero de "inicio" no sea contabilizado
#     suma += i

# print (f"La suma de los valores entre {inicio} y {fin} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# suma= 0
# numero = int(input("Ingrese un numero: "))

# while numero!=0:
#     suma += numero
#     numero = int(input("Ingrese otro numero (Si desea finalizar, ingrese 0): "))

# print (suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# numeroAleatorio = random.randint(0,9)
# intentos = 0
# intento = -1
# print("¡Adivina el número secreto entre 0 y 9!")

# while intento != numeroAleatorio:
#     intento = int(input("Ingresa tu numero: "))
#     intentos += 1
    

# print (f"Acertaste! el numero secreto era {numeroAleatorio} y la cantidad de intentos fueron {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, -1, -1):
#     if i % 2 == 0:
#         print (i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# print("Suma de los numeros entre 0 y el ingresado por el usuario")
# numeroUsuario = int(input("Ingrese un numero positivo: "))

# suma = 0

# for i in range(0, numeroUsuario+1): #el +1 es para incluir el numero ingresado por el usuario, en caso de no querer incluirlo habria que sacar el +1
#     suma += i

# print (f"La suma de los numeros entre 0 y {numeroUsuario} es {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# for i in range(10): #Lo deje en 10 para poder probarlo pero cambiando el 10 por 100 y funciona igual
#     numero = int(input(f"Ingresá el número {i + 1}: "))

#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

# print("\nResultados:")
# print("Números pares:", pares)
# print("Números impares:", impares)
# print("Números positivos:", positivos)
# print("Números negativos:", negativos)


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# suma= 0
# cantidad = 10

# for i in range (cantidad):
#     numero= int(input(f"Ingrese el numero {i+1}: "))
#     suma += numero

# media = suma/cantidad

# print(f"La media del total de los numeros ingresados es {media}")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# numero = input("Ingrese el numero a invertir: ")
# numeroStr = str(numero)

# numeroInvertido =""

# for i in numero:
#     numeroInvertido = i + numeroInvertido

# print(f"El numero invertido es: {numeroInvertido}")
