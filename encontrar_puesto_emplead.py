def encontrar_puesto_empleado(nombre_completo, empleados):
    nombre, apellido = nombre_completo.split()
    
    for empleado in empleados:
        if empleado['nombre'] == nombre and empleado['apellido'] == apellido:
            return f"El puesto de {nombre_completo} es: {empleado['puesto']}"
    return f"{nombre_completo} no trabaja aquí."
empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

nombre_completo = input("Ingresa el nombre completo del empleado (nombre y apellido): ")

print(encontrar_puesto_empleado(nombre_completo, empleados))
