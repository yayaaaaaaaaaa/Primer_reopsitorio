# Función que encuentra el primer duplicado en una lista
def encontrar_duplicado(lista):
    vistos = set()
    for numero in lista:
        if numero in vistos:
            return numero  
        vistos.add(numero)
    return None
lista = [1, 2, 3, 4, 5, 3, 6, 7] 
resultado = encontrar_duplicado(lista)
print(f"El primer duplicado es: {resultado}")
