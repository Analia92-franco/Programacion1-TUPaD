#TRABAJO PRÁCTICO 7: ESTRUCTURA DE DATOS COMPLEJOS

#Ejercicio1
#Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos nuevas frutas a la lista
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(f"Frutas agregadas a la lista {precios_frutas}")


#Ejercicio2
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"Lista de precio actualizado {precios_frutas}")


#Ejercicio3
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = list(precios_frutas.keys())

print(f"Lista de frutas {frutas}")


# Ejercicio4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# -Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# -Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

#Pedimos al usuario que cargue los 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = int(input(f"Ingrese el número de telefono {nombre}: "))
    contactos[nombre] = numero

#Consulta de contacto
buscar_nombre = input("Ingrese el nombre del contacto que desea consultar: ")

if buscar_nombre in contactos: #Verificamos si el contacto existe
    print(f"El nombre {buscar_nombre} es {contactos[buscar_nombre]}")
else:
    print(f"No se encontro el nombre {buscar_nombre} en los contactos.")


# Ejercicio5
# Solicita al usuario una frase e imprime:
# -Las palabras únicas (usando un set).
# -Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.lower().split() #Convierte la frase en minuscula y en una lista de palabras
palabras_unica = set(palabras) #Obtiene las palabras unicas usando un conjunto set()

#Diccionario 
cantidad_palabras = {}

for palabra in palabras:
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra] += 1
    else:
        cantidad_palabras[palabra] = 1

print(f"Palabras únicas: {palabras_unica}")
print(f"Cantidad de veces que aparece cada palabra: {cantidad_palabras}")


# Ejercicio6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

# Diccionario para guardar los alumnos y notas.
alumnos = {}

#Ingresar los datos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    notas = []
    
    for n in range(3):
        nota = float(input(f"Ingrese la nota {n + 1} de {nombre}: ")) 
        notas.append(nota)

    alumnos[nombre] = tuple(notas) #Conviertir en tupla y guardar

#Promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: notas {notas}, promedio: {promedio:.2f}")




# Ejercicio7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# -Mostrá los que aprobaron ambos parciales.
# -Mostrá los que aprobaron solo uno de los dos.
# -Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Nadia", "Eli", "Javo", "Flor"}
parcial2 = {"Ana", "Nadia", "Eli", "Seba"}

ambos_parciales = parcial1 & parcial2 #Intersección
solo_un_parcial = parcial1 ^ parcial2 #Diferencia Asimétrica 
total = parcial1 | parcial2 #Unión 

print(f"Alumnos que aprobaron ambos parciales: {ambos_parciales}")
print(f"Alumnos que aprobaron solo un parcial {solo_un_parcial}")
print(f"Alumnos que aprobaron al menos un parcial {total}")


# Ejercicio8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# -Consultar el stock de un producto ingresado.
# -Agregar unidades al stock si el producto ya existe.
# -Agregar un nuevo producto si no existe.

productos = {"Termo": 20, "Mate": 50, "Vasos": 12, "Botella": 22}

while True:
    print("--- MENU DE OPCIONES ---")
    print("1. Consultar stock del producto.")
    print("2. Agregar unidades al stock existente.")
    print("3. Agregar nuevo producto.")
    print("4. Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el producto a consultar: ")
        if producto in productos:
            print(f"Stock de {producto}: {productos[producto]}")
        else:
            print("Producto sin stock.")
    
    elif opcion == "2":
        producto = ("Ingrese el producto: ")
        if producto in productos:
            unidades = int(input("Ingrese la cantidad a agregar: "))
            productos[producto] += unidades
            print(f"Stock actualizado: {productos[producto]}")
        else:
            print("Producto no se encuentra en stock")
            
    elif opcion == "3":
        producto = input("Ingrese nuevo producto: ")
        if producto not in productos:
            unidades = int(input("Ingrese stock del producto: "))
            productos[producto] = unidades
            print("Producto agregado al stock")
        else:
            print("El producto ya existe")
    
    elif opcion == "4":
        print("Nos vemos!")
        break
    
    else:
        print("Opción inválida")
        


#Ejercicio9
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "11:00"): "Clase de Matemáticas",
    ("miercoles", "19:00"): "Clase de OE",
    ("miercoles", "20:00"): "Clase de AySO",
    ("jueves", "16:00"): "Microclase de Programación I"
   
}

while True:
    print("--- AGENDA ---")
    print("1. Consultar actividad")
    print("2. Agregar actividad")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        dia = input("Ingrese el dia: ").lower()
        hora = input("Ingrese hora (HH:MM): ")
        clave = (dia,hora)
        
        if clave in agenda:
            print(f"Actividad: {agenda[clave]}")
        else:
            print("No hay actividades programadas")
    
    elif opcion == "2":
        dia = input("Ingrese día: ").lower()
        hora = input("Ingrese hora (HH:MM): ")
        actividad = input("Ingrese actividad: ")
        
        agenda[(dia, hora)] = actividad
        print("Actividad agregada exitosamente")
        
    elif opcion == "3":
        print("Nos vemos!")
        break
    
    else:
        print("Opción inválida")
        
        
#Ejercicio10
#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#-Las capitales sean las claves.
#-Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Paraguay": "Asunción", 
    "Uruguay": "Montevideo,"
    }

#Invertir diccionario
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("--- DICCIONARIO ORIGINAL ---")
print(paises_capitales)

print("---DICCIONARIO INVERTIDO ---")
print(capitales_paises)
