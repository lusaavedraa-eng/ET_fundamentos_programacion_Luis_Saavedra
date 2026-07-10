recorridos = {
    'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'dia', True],
    'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
    'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'dia', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'dia', True],
    'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
    'R006': ['Santiago', 'Rancagua', 90, 'normal', 'dia', True],
}

venta = {
    'R001': [7990, 20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12],
}

def leer_opcion():
    while True:
        try:
            opcion = int(input("ingrese opcion: "))
            if opcion>=1 and opcion<=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("Debe seleccionar una opción válida")
while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")
    opcion = leer_opcion()
    if opcion == 1:
        def asientos_origen(recorridos,venta,origen):
            