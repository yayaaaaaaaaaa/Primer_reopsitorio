class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"No tienes suficiente saldo para retirar {cantidad}.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad} unidades. Saldo restante: {self.saldo}")
    
    def transferir_dinero(self, cantidad, usuario_origen):
        if cantidad > usuario_origen.saldo:
            raise ValueError(f"El usuario {usuario_origen.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        else:
            usuario_origen.saldo -= cantidad
            self.saldo += cantidad
            print(f"Se han transferido {cantidad} unidades desde {usuario_origen.nombre}. Saldo de {self.nombre}: {self.saldo}, saldo de {usuario_origen.nombre}: {usuario_origen.saldo}")
    
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Has agregado {cantidad} unidades. Saldo actual: {self.saldo}")

# Caso de uso
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo a "Alicia"
alicia.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
bob.transferir_dinero(80, alicia)

# 4. Intentar retirar 50 unidades de saldo a "Alicia"
try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(e)
