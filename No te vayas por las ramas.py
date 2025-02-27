class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self):
        self.tronco += 1
    def nueva_rama(self):
        self.ramas.append(1)
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición no válida.")
    def info_arbol(self):
        return f"Longitud del tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}"

# Caso de uso
# 1.
arbol = Arbol()
# 2. 
arbol.crecer_tronco()
# 3.
arbol.nueva_rama()
# 4. 
arbol.crecer_ramas()
# 5. 
arbol.nueva_rama()
arbol.nueva_rama()
# 6. 
arbol.quitar_rama(2)
# 7. 
info = arbol.info_arbol()
print(info)
