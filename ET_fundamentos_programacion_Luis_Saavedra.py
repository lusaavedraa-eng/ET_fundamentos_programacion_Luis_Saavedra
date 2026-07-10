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


def asientos_origen(recorridos,venta,origen):
    total = 0
    for codigo in recorridos:
        if recorridos[codigo][0].lower() == origen.lower():
            total = total + venta[codigo][1]
    print("el total de asientos disponibles es: ",total)

def busqueda_precio(recorridos,venta,p_min,p_max):
    lista = []
    for codigo in venta:
        precio = venta[codigo][0]
        asientos = venta[codigo][1]
        if precio>= p_min and precio <= p_max and asientos > 0:
            origen = recorridos[codigo][0]
            destino = recorridos[codigo][1]
            lista.append(f"{origen}- {destino}-{codigo}")
            lista.sort()
            if len(lista) == 0:
                print("No hay recorridos en ese rango de precios.")
            else:
                print("recorridos encontrados: ")
                print(lista)

            



while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")
    op = leer_opcion()
    if op == 1:
        origen = input("ingrese ciudad de origen: ")
        asientos_origen(recorridos, venta, origen)
    elif op == 2:
        while True:
            try:
                minimo = int(input("ingrese precio minimo: "))
                maximo = int(input("ingrese precio maximo: "))
                if minimo>= 0 and maximo >= 0 and minimo <= maximo:
                    break
                else:
                    print("Debe ingresar valores enteros")

            except: ValueError
            print("Debe ingresar valores enteros")


    elif op == 6:
        print("programa finalizado.")
        break
