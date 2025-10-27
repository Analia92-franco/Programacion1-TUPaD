import utils

opcion = "0"
productos = []

menu = [
    "\n--- Gestor de productos ---",
    "\n1. Mostrar productos.",
    "2. Agregar productos.",
    "3. Cargar productos en lista de diccionario.",
    "4. Buscar producto.",
    "5. Reescribir archivo.",
    "6. Salir\n"
]

while opcion != "6":
    for item in menu:
        print(item)
    
    opcion = input("Ingrese una opción (1-6)").strip()
    
    if not opcion.isdigit():
        print("Opción inválida. Vuelva a intentarlo")
        continue
    
    match opcion:
        case "1":
            utils.mostrar_productos()
        case "2":
            utils.agregar_productos()
        case "3":
            productos = utils.cargar_productos_lista()
        case "4":
            utils.buscar_producto(productos)
        case "5":
            utils.reescribir_archivo(productos)
        case "6":
            print("Nos vemos!!")
        case _:
            print("Opción fuera de rango, intente nuevamente")
              
