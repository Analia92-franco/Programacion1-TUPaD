#Ejercicio1
notas = [9.1, 7.5, 8.3, 6.9, 5.4, 4.8, 10.0, 8.7, 7.2, 6.0]

print(notas)

promedio = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)
print(f"El promedio es de: {promedio} ")
print(f"La nota más alta es: {nota_max} ")
print(f"La nota más baja es: {nota_min}")


#Ejercicio2
productos = []

for i in range(5):
    produc = input(f"Ingrese el producto {i + 1}: ")
    productos.append(produc)
print(f"Lista de productos: {sorted(productos)} ")

#Eliminar elemento de la lista
x = input("Ingrese el producto que desee eliminar de la lista: ")
if x in productos:
    productos.remove(x)
    print(f"Lista de productos actualizada: {sorted(productos)} ")
else:
    print("El elemento no se encuentra en la lista.")


#Ejercicio3
import random
num = []
num_par = []
num_imp = []

for i in range(15):
    n = random.randint(1,101)
    num.append(n)
    if n % 2 == 0:
        num_par.append(n)
    else:
        num_imp.append(n)

print(f"Hay {len(num_par)} pares y {len(num_imp)} impares.")

#Ejercicio4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = [] 
for dato in datos:
    if not dato in datos_unicos:
        datos_unicos.append(dato)
print(datos_unicos)


#Ejercicio5
estudiantes = ["Analia", "Florencia", "Nadia", "Elizabeth", "Fernando", "Jeremias", "Abigail", "Franco"]
print(f"Estudiantes presentes: {estudiantes} ")
accion = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()
if accion == "A":
    estudiantes.append(input("Ingrese nombre del nuevo estudiante: ").capitalize())
    print(f"Estudiantes actualizados: {estudiantes} ")
elif accion == "E":
    estudiante = input("Ingrese nombre del estudiante a eliminar: ").capitalize()
    if estudiante in estudiantes:
        estudiantes.remove(estudiante)
        print(f"Estudiantes actualizados: {estudiantes} ")
    else:
        print("El estudiante ingresado no es válido.")
else:
    print("La acción ingresada no es válida.")


#Ejercicio6
import random
lista = []
for i in range(7):
    lista.append(random.randint(1,101))
print(lista)
lista_nueva = [] 
for i in range(7):
    lista_nueva.append(lista[i-1])
print(lista_nueva)


#Ejercicio7
import random 
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = []

for i in range(len(semana)):
    min = random.randint(1,48)
    max = random.randint(min,48)
    temperaturas.append([min,max])
print(temperaturas)

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0
for i in range(len(temperaturas)):            #[0]0   1
    min = temperaturas[i][0] #temperaturas[i] = [31, 44]
    max = temperaturas[i][1]
    suma_min += min
    suma_max += max
    amplitud = max - min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = semana[i]
promedio_min = int(suma_min / len(temperaturas))
promedio_max = int(suma_max / len(temperaturas))
print(f"El promedio de la temperatura minima es: {promedio_min} y el promedio de la temperatura maxima es: {promedio_max}")
print(f"El día de mayor amplitud térmica es: {dia_mayor_amplitud}")



#Ejercicio8
import random
#Crear matriz con las notas de 5 estudiantes en 3 materias.
notas = []
for i in range(5): #5 estudiantes
    nota = []
    for j in range(3): #3 materias
        nota.append(random.randint(1,10))
    notas.append(nota)   
print(notas)
#Mostrar el promedio de cada estudiante.
for i in range(5):
    print(f"Promedio estudiante {i+1}: {sum(notas[i]) / 3}")    
#Mostrar el promedio de cada materia.
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    print(f"Promedio materia {j+1}: {suma / 5}")    


#Ejercicio9
tablero = []
sep = " | "

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

print(f"Tablero actual:\n{sep.join(tablero[0])}\n{sep.join(tablero[1])}\n{sep.join(tablero[2])}")

#Jugadores
turno = "X"

for jugada in range(9):
    print(f"Turno del jugador {turno}")
    posicion_valida = False
    while not posicion_valida:
        posicion = input("Ingrese posicion (fila, columna): ")
        coordenadas = posicion.split(",")
        if len(coordenadas) == 2:
            x = coordenadas[0].strip()
            y = coordenadas[1].strip()
            if not x.isnumeric:
                print("Fila inválida. Intente nuevamente")
            elif not 1 <= int(x) <= 3:
                print("Fila inválida. Intente nuevamente")
            elif not y.isnumeric:
                print("Columna inválida. Intente nuevamente")
            elif not 1 <= int(y) <= 3:
                print("Columna inválida. Intente nuevamente")
            elif tablero[int(x)-1][int(y)-1] != "-":
                print("Posición ya ocupada. Intente nuevamente")
            else:
                posicion_valida = True    
        else:
            print("Posición inválida. Intente nuevamente")
    tablero[int(x)-1][int(y)-1] = turno
    if turno == "X":   
        turno = "O"
    else:
        turno = "X"
    print(f"Tablero actual:\n{sep.join(tablero[0])}\n{sep.join(tablero[1])}\n{sep.join(tablero[2])}") 
print("Fin del juego.")


#Ejercicio10

ventas = [
    [10, 15, 20, 12, 18, 25, 14],  # Producto 1
    [5, 8, 12, 10, 15, 9, 7],      # Producto 2
    [20, 18, 15, 22, 19, 17, 21],  # Producto 3
    [12, 14, 16, 18, 20, 13, 15]   # Producto 4
]

max = 0
prodmax = 0

#Total mas vendido por cada producto
for i, producto in enumerate(ventas):
  total = 0
 # numeroProducto += 1
  for dia in producto:
   total += dia
   
  print (f"Ventas del producto #{i + 1}: {total}")
  if total > max:
    max = total
    pmax = i + 1
    
#Dia con mayores ventas totales
max = 0
diamax = 0

for dia in range(7): 
  total = 0
  for prod in range(4):
    total += ventas[prod][dia]
  #Total lo que se vendio durante ese dia
  if total > max:
    max = total
    dmax = dia + 1

print(f"El dia con mayor ventas fue el {dmax} ")

#Producto mas vendido en la semana
print(f"El producto mas vendido fue el #{pmax}")