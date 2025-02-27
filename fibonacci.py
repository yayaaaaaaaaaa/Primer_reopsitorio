# Función recursiva para calcular el término n de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
     return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Ingresa el número n para calcular el término n de Fibonacci: "))
print(f"El término {n} de la secuencia de Fibonacci es: {fibonacci(n)}")
