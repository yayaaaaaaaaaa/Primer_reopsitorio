
def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.strip(".,")  # Elimina comas y puntos
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    texto_filtrado = ' '.join([p for p in palabras if p.strip(".,") != palabra])
    return texto_filtrado


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se necesitan dos palabras para reemplazar")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se necesita una palabra para eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida")

# Caso de uso
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

# Contar palabras
print("Contar palabras:")
print(procesar_texto(texto, "contar"))

# Reemplazar la palabra 'texto' por 'relato'
print("\nReemplazar palabras:")
print(procesar_texto(texto, "reemplazar", "texto", "relato"))

# Eliminar la palabra 'ejemplo'
print("\nEliminar palabra:")
print(procesar_texto(texto, "eliminar", "ejemplo"))