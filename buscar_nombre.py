# Función para buscar un nombre en la lista
def buscar_nombre():
    nombres = ["Jaime", "Silvia", "Ana"]
    nombre_buscado = input("Ingresa el nombre a buscar: ")
    if nombre_buscado in nombres:
        print(f"El nombre {nombre_buscado} ha sido encontrado.")
    else:
        raise ValueError(f"El nombre {nombre_buscado} no se encuentra en la lista.")

try:
    buscar_nombre()
except ValueError as e:
    print(e)
