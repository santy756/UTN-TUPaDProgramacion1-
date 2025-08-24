#PROGRAMACION
#Alumno: Santiago Nicolas Perez González
#Comisión: Comisión 11
#Trabajo practico MATERIA – Practico N° 1


#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Escriba su nombre: ")
apellido = input ("Escriba su apellido: ")
nombreCompleto =  nombre + " " + apellido
print ("Hola " + nombreCompleto)


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Escriba su nombre: ")
apellido = input ("Escriba su apellido: ")
edad = int(input ("Escriba su edad: "))
lugarResidencia = input ("Escriba su lugar de residencia: ")
fichaCompleta =  (f"Hola, soy {nombre} {apellido} tengo {edad} años y vivo en {lugarResidencia}" )
print (fichaCompleta)






#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

radio = float(input ("Escriba el radio del circulo del cual desea calcular el area y perimetro: "))
area = math.pi * radio**2
perimetro = 2*math.pi*radio
print (f"El area del criculo es: {area}. El perimetro del circulo es {perimetro}")

#*Buscando si existe alguna palabra reservada para “pi” y encontré que puedo exportar el modulo “Math” y asi usar la constante con “math.pi”*

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))
horas = segundos/60
print (f"{segundos} equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese el numero del cual desea conocer la tabla de multiplicar: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print (f"{numero} x {contador} = {resultado}")
    contador +=1






#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero = int(input("Ingrese un numero: "))

if numero!= 0:
    suma = numero + numero
    resta = numero - numero
    division = numero / numero
    multiplicacion = numero * numero

    print(f"Los resultados son: {suma} para la suma, {resta} para la resta, {division} para la division, {multiplicacion} para la multiplicacion2")
else :
    print("El numero debe ser diferente de 0")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚2)
numero = float(input("Ingrese su peso en KG para poder calcular Su IMC: "))
numero2 = float(input("Ahora ingrese su altura expresado en metros: "))

imc= numero/(numero2**2)

print(f"Su Indice de Masa Corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
 
celcius = float(input("Ingrese los grados en Celcius que quiere convertir en Farenheit: "))

fahrenheit= (celcius* 9/5) + 32

print(f"El resultado de los grados ingresados convertidos a Fahrenheit es: {fahrenheit}")
