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
def buscar_codigo(venta,codigo):
    codigo = codigo.upper()
    for cod in venta:
        if cod.upper() == codigo:
            return True
    return False
def actualizar_precio(venta,codigo,nuevo_precio):
    codigo = codigo.upper()
    if buscar_codigo(venta,codigo):
        for cod in venta:
            if cod.upper == codigo:
                venta[cod][0] = nuevo_precio
                return True
    return False


def validar_codigo(codigo):
    return codigo.strip() != ""
def validar_origen(origen):
    return origen.strip() != ""
def validar_destino(destino):
    return destino.strip() != ""
def validar_distancia(distancia):
    return distancia > 0
def validar_tipo_bus(tipo_bus):
    return tipo_bus.lower() in ['normal','semi-cama','cama']
def validar_servicio(servicio):
    return servicio.lower() in ['dia', 'noche']
def validar_tiene_wifi(wifi):
    return wifi.lower() in ['s', 'n']
def validar_precio(precio):
    return precio > 0
def validar_asientos(asientos):
    return asientos >= 0

def agregar_recorrido(recorridos,venta,codigo,origen,destino,distancia,tipo_bus,servicio,tiene_wifi,precio,asientos):
    if buscar_codigo(venta,codigo):
        return False
    recorridos[codigo] = [
        origen,
        destino,
        distancia,
        tipo_bus,
        servicio,
        tiene_wifi,
        precio,
        asientos,
    ]
    venta[codigo] = [precio,asientos]
    return True
def grip():

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
        elif op == 3:
            while True:
                codigo = input("ingrese codigo del recorrido: ").upper
                while True:
                    try:
                        nuevo_precio = int(input("ingrese nuevo precio: "))
                        if nuevo_precio>0:
                            break
                        else:
                            print("el precio debe ser mayor a 0")
                    except: ValueError
                    print("debe ingresar un numero entero")
                    if actualizar_precio(venta,codigo,nuevo_precio):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                        pregunta = input("¿Desea actualizar otro precio (s/n)?").lower
                        if pregunta == "n":
                            break



        elif op == 4:
            print("")
        
        elif op == 5:
            print("")
        

        elif op == 6:
            print("programa finalizado.")
            break
