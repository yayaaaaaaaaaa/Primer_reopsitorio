# Función que enmascara todos los caracteres de la cadena excepto los últimos cuatro
def enmascarado_datos(dato):
    dato_str = str(dato)
    if len(dato_str) > 4:
        return '#' * (len(dato_str) - 4) + dato_str[-4:]
    else:
        return dato_str

# Ejemplo de uso con un número
dato = 1234567890  # Ejemplo con un número de teléfono
resultado = enmascarado_datos(dato)
print(f"El dato enmascarado es: {resultado}")

# Ejemplo con una cadena de texto
dato_texto = "abcdefg"  # Ejemplo con una cadena de texto
resultado_texto = enmascarado_datos(dato_texto)
print(f"El texto enmascarado es: {resultado_texto}")
