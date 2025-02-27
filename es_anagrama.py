def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

palabra1 = "Roma"
palabra2 = "Amor"
print(f"¿'{palabra1}' y '{palabra2}' son anagramas?:", es_anagrama(palabra1, palabra2))