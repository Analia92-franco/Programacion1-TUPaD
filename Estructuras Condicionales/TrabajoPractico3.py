# #Ejercicio1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")



#Ejercicio2
nota = float(input("Ingrese la nota: "))

if nota >= 6:
    print("APROBADO")
elif nota < 6:
    print("DESAPROBADO")



#Ejercicio3
num = int(input("Por favor, ingrese un número par: "))

if num % 2 == 0:
    print(f"El número {num} es par")
elif num % 2 == 1:
print(f"El número {num} es impar")



#Ejercicio4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("La categoría es Niño/a")
elif edad >= 12 and edad < 18:
    print("La categoría es Adolescente")
elif edad >= 18 and edad < 30:
    print("La categoría es Adulto/a joven")
else:
    print("La categoría es Adulto/a")



#Ejercicio5
import len

password = int(input("Por favor, ingrese una contraseña entre 8 y 14 caracteres: "))

if (password >= 6 and <= 16):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#Ejercicio6
from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda: 
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")



#Ejercicio7
frase = input("Ingrese una frase o palabra: ")

if frase.lower().endswith(("a", "e", "i", "o", "u")):
    frase += "!" # es lo mismo que hacer frase = frase + "!" (forma reducida)

print(frase)



#Ejercicio8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opción deseada, 1. Si quiere su nombre en mayúscula, 2. Si quiere su nombre en minúscula, 3. Si quiere su nombre con la primera letra mayúscula: "))

if 1 == opcion:
    print(nombre.upper())
elif 2 == opcion:
    print(nombre.lower())
elif 3 == opcion:
    print(nombre.title())
else:
    print("Por favor, ingrese una opción: ")



#Ejercicio9
magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")



#Ejercicio10
hemisferio = input("¿En cuál hemisferio se encuentra N/S?: ").upper()
mes = int(input("¿Qué número de mes del año es?: ")) 
dia = int(input("¿Qué día es?: "))

if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Se encuentra en invierno")
    else:
        print("Se encuentra en verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Se encuentra en primavera")
    else:
        print("Se encuentra en otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Se encuentra en verano")
    else:
        print("Se encuentra en invierno")
elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Se encuentra en otoño")
    else:
        print("Se encuentra en primavera")
else:
    print("El hemisferio, mes y/o día ingresado es incorrecto")