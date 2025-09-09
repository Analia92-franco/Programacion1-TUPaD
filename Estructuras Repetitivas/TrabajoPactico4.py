#Ejercicio1
for num in range(0, 101):
    print(num)



#Ejercicio2
num = int(input("Ingrese un número entero: "))
n = abs(num)

if n == 0:
    digito = 1
else:
    digito = 0
    while n > 0:
        n //= 10
        digito += 1

print(f"El número {num} tiene {digito} digitos: ")



#Ejercicio3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0

if num1 == num2:
    print("Los valores son iguales")
else:
    for i in range(num1 + 1, num2): 
        suma += i

print(f"La suma de los números entre {num1} y {num2}, excluyendolos, es: {suma}")



#Ejercicio4
suma = 0
ite = True

while ite:
    num = int(input("Ingrese un número entero, (0 para salir): "))
    suma += num
    ite = num != 0 

print(f"La suma es: {suma}")
    


#Ejercicio5
import random
numAl = random.randint(0,9)
num = int(input("Adivina el número entre el 0 y 9: "))
intentos = 1

while num != numAl:
    num = int(input("¡No adivinaste! Intenta nuevamente: "))
    intentos += 1

print(f"¡Adivinaste! El número era {numAl}. La cantidad de intentos fue de: {intentos}")
    


#Ejercicio6
for i in range(100, -2, -2):
    print(i)



#Ejercicio7
num = int(input("Ingrese un número entero positivo: "))
suma = 0

if num < 0:
    print("El número debe ser positivo")
else:
    for i in range(1, num + 1):
        suma += i
    print(f"La suma de los números comprendidos entre 0 y {num} es: {suma}")



#Ejercicio8
par = 0
imp = 0
neg = 0
pos = 0

for i in range(1,101):
    num = int(input("Ingrese un número entero: "))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            imp += 1
        if num < 0:
            neg += 1
        else:
            pos +=1
print(f"Ha ingresado {par} números pares, {imp} números impares, {neg} números negativos y {pos} números positivos")



#Ejercicio9
suma = 0

for i in range(1, 101):
    num = int(input("Ingrese un número entero: "))
    suma += num
print(f"La media es {suma/100}")

#Ejercicio10
num = int(input("Ingrese un número entero: "))
n = 0

if num != 0:
    i = abs(num)
    while i > 0:
        n = n * 10 + i % 10
        i //= 10
    if num < 0:
        n *= -1

print(f"El número invertido de {num} es {n}")