import os

def mostrar_productos():
    if not os.path.exists("productos.txt"):
        print("No existe productos.txt")
        return
    
    with open("productos.txt", "r") as archivo:
        for linea in archivo: #Recorro cada línea del archivo txt
            nombre, precio, cantidad = linea.strip().split(",") 
            print(f"Producto: {nombre}  |  Precio: ${precio}  |  Cantidad: {cantidad}")


def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print("Producto agregado exitosamente\n")
    
def mostrar_lista(productos):
    for producto in productos:
        print(f"Producto: {producto['nombre']}  |  Precio: ${producto['precio']}  |  Cantidad: {producto['cantidad']}")
        
        
def cargar_productos_lista():
    productos = []  #Crear lista vacia
    if not os.path.exists("productos.txt"):
        print("No existe productos.txt")
        return []

    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre" : nombre,
                "precio" : precio,
                "cantidad" : cantidad
            }
            
            productos.append(producto)
        
        print("Productos cargados exitosamente")
        mostrar_lista(productos)
        return productos
    
def buscar_producto(productos):
    if len(productos) == 0:
        print("No hay productos. Se debe cargar los productos primero")
        return
    
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False
    
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            print(f"Producto: {producto['nombre']}  |  Precio: ${producto['precio']}  |  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
        
    if not encontrado:
        print("Producto no encontrado.")

def reescribir_archivo(productos):
    if len(productos) == 0:
        print("No hay productos. Se debe cargar los productos primero")
        return
    
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
