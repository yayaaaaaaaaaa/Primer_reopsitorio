# Ejercicio 2: Función calcular_promedio

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0: 
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# Test de la función
numeros = [10, 20, 30, 40, 50]
print("El promedio es:", calcular_promedio(numeros))
