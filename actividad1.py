# #Ejercicio1
print("Hola Mundo!")

# #Ejercicio2
print(f"Hola, {input("Ingrese su nombre: ")}")

# #Ejercicio3
print(f"Soy {input("Ingrese su nombre: ")} {input("Ingrese su apellido: ")}, tengo {input("Ingrese su edad: ")} años y vivo en {input("Ingrese su país: ")}")

# #Ejercicio4
import math
r = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {math.pi * r ** 2}")
print(f"El perímetro del círculo es: {2 * math.pi * r}")

# #Ejercicio5
print(f"{(seg := int(input("Ingrese la cantidad de segundos: ")))} segundos equivalen a {int(seg / 3600)} horas.")

#Ejercicio6
num = int(input("Ingrese un número: "))
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")

# #Ejercicio7
num1 = int(input("Ingrese el primer número que no sea 0: "))
num2 = int(input("Ingrese el segundo número que no sea 0: "))
print(f"La suma es :{num1 + num2}")
print(f"La división es: {int(num1 / num2)}")
print(f"La multiplicación es: {num1 * num2}")
print(f"La resta es: {num1 - num2}")

# #Ejercicio8
altura = float(input("Ingrese su altura en metro: "))
peso = float(input("Ingrese su peso en kg: "))
print(f"Su masa corporal es de: {peso / altura ** 2}")

# #Ejercicio9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"La equivalencia en grados Fahrenheit es de: {celsius * 9 / 5 + 32}")

# #Ejercicio10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(f"El promedio es de: {(num1 + num2 + num3) / 3}")