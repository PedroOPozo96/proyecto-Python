import os

# 1. Cargar fichero de compras.
def fichero_compra(compras, cliente_por_producto):
    archivo_path = "compras.txt"
    print(f"Intentando abrir el archivo en la ruta: {os.path.abspath(archivo_path)}")
    
    try:
        with open(archivo_path, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                elementos = linea.strip().split(",")
                if len(elementos) == 6:
                    dni_cliente, fecha_compra, nombre_producto, cantidad, precio, descuento = elementos
                    try:
                        cantidad = int(cantidad)
                        precio = float(precio)
                        descuento = float(descuento)
                    except ValueError:
                        print(f"Error en el formato de los datos: {linea}")
                        continue

                    cantidad_total = cantidad * precio
                    compra = {
                        'DNI': dni_cliente,
                        'Fecha': fecha_compra,
                        'Producto': nombre_producto,
                        'Cantidad': cantidad,
                        'Precio': precio,
                        'Descuento': descuento,
                        'Cantidad Total': cantidad_total
                    }

                    compras.append(compra)
                    if nombre_producto in cliente_por_producto:
                        cliente_por_producto[nombre_producto].add(dni_cliente)
                    else:
                        cliente_por_producto[nombre_producto] = {dni_cliente}
                
            print("\nDatos de compras cargados.\n")

    except FileNotFoundError:
        print("El fichero de compra no existe")
    except Exception as e:
        print(f"\nError al cargar la información del fichero: {e}\n")



# 2. Añadir compra.

def añadir_compra(compras, cliente_por_producto):
    try:
        dni_cliente = input("Ingrese el DNI del cliente: ")
        fecha_compra = input("Ingresa la fecha de la compra: ")
        nombre_producto = input("Ingresa el nombre del producto: ")
        cantidad = int(input("Ingresa la cantidad comprada: "))
        precio = float(input("Ingrese el precio: "))
        descuento = float(input("Ingrese el porcentaje del descuento aplicado: "))

        cantidad_total = cantidad * precio
        importe_descuento = cantidad_total * (descuento / 100)
        importe_con_descuento = cantidad_total - importe_descuento

        compra = {
            'DNI': dni_cliente,
            'Fecha': fecha_compra,
            'Producto': nombre_producto,
            'Cantidad': cantidad,
            'Precio': precio,
            'Descuento': descuento,
            'Cantidad Total': cantidad_total,
            'Importe con Descuento': importe_con_descuento
        }    

        compras.append(compra)
        
        if nombre_producto in cliente_por_producto:
            cliente_por_producto[nombre_producto].add(dni_cliente)
        else:
            cliente_por_producto[nombre_producto] = {dni_cliente}

        print("\nCompra agregada exitosamente.\n")

        with open("compras.txt", 'a') as archivo:
            archivo.write(f"{dni_cliente},{fecha_compra},{nombre_producto},{cantidad},{precio},{descuento}\n")

        print("\nEl fichero compras.txt ha sido actualizado.\n")
    
    except ValueError:
        print("Error en el formato de los datos ingresados, inténtelo de nuevo.")
    except Exception as e:
        print(f"Se produjo un error: {e}")



# 4. Mostrar Producto por clientes.
def mostrar_producto_por_clientes(cliente_por_producto):
    print("\nNúmero de clientes únicos que han comprado cada producto:")
    for producto, clientes in cliente_por_producto.items():
        print(f"{producto}: {len(clientes)} cliente(s)")

# 5. Eliminar producto de una compra.

def eliminar_producto(compras, cliente_por_producto):
    dni_cliente = input("Ingresa el DNI del cliente: ")
    fecha_compra = input("Ingresa la fecha de la compra: ")
    nombre_producto = input("Ingresa el nombre del producto: ")

    compras_actualizadas = []
    producto_eliminado = False
    for compra in compras:
        if compra['DNI'] == dni_cliente and compra['Fecha'] == fecha_compra and compra['Producto'] == nombre_producto:
            producto_eliminado = True
        else:
            compras_actualizadas.append(compra)

    if producto_eliminado:
        if nombre_producto in cliente_por_producto:
            cliente_por_producto[nombre_producto].discard(dni_cliente)
            if not cliente_por_producto[nombre_producto]:
                del cliente_por_producto[nombre_producto]

        compras[:] = compras_actualizadas
        with open("compras.txt", 'w') as archivo:
            for compra in compras:
                archivo.write(f"{compra['DNI']},{compra['Fecha']},{compra['Producto']},{compra['Cantidad']},{compra['Precio']},{compra['Descuento']}\n")
        print("\nProducto eliminado correctamente de la compra.\n")
    else:
        print("\nCompra no encontrada o el producto no existe en la compra.\n")


# 6. Listar nombres de productos.
def listar_productos_comprados(compras):
    productos_comprados = set()
    for compra in compras:
        if compra['Producto']:
            productos_comprados.add(compra['Producto'])

    if productos_comprados:
        print("\nNombres de los productos comprados:")
        for index, producto in enumerate(productos_comprados, start=1):
            print(f"{index}. {producto}")
    else:
        print("\nNo se ha comprado productos todavía.\n")

# 7. Listar compras de un cliente en una fecha.

def listar_compra_fecha(compras):
    dni_cliente = input("Ingrese el DNI del cliente: ")
    fecha_compra = input("Ingresa la fecha: ")

    total_importe_fecha = 0
    compras_cliente_fecha = []

    for compra in compras:
        if compra['DNI'] == dni_cliente and compra['Fecha'] == fecha_compra:
            compras_cliente_fecha.append(compra)
            nombre_producto = compra['Producto']
            precio = compra['Precio']
            descuento = compra['Descuento']
            cantidad_total = compra['Cantidad'] * compra['Precio']
            importe_con_descuento = cantidad_total * (1 - (descuento / 100))
            descuento_aplicado = cantidad_total - importe_con_descuento
            total_importe_fecha += importe_con_descuento

            print(f"Producto: {nombre_producto}, Precio: {precio}, Importe sin Descuento: {cantidad_total}, Importe con Descuento: {importe_con_descuento}, Descuento aplicado: {descuento_aplicado}")

    if compras_cliente_fecha:
        print(f"\nListado de compras de {dni_cliente} en la fecha {fecha_compra}:")
        for compra in compras_cliente_fecha:
            nombre_producto = compra['Producto']
            cantidad = compra['Cantidad']
            precio = compra['Precio']
            descuento = compra['Descuento']
            cantidad_total = cantidad * precio
            importe_con_descuento = cantidad_total * (1 - (descuento / 100))
            print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Precio: {precio}, Descuento: {descuento}, Importe Total: {cantidad_total}, Importe con Descuento: {importe_con_descuento}")
        print(f"\nImporte total de las compras realizadas por {dni_cliente} en la fecha {fecha_compra}: {total_importe_fecha}\n")
    else:
        print(f"\nNo se encontraron compras para el cliente {dni_cliente} en la fecha {fecha_compra}.\n")
    dni_cliente = input("Ingrese el DNI del cliente: ")
    fecha_compra = input("Ingresa la fecha: ")

    total_importe_fecha = 0
    compras_cliente_fecha = []

    for compra in compras:
        if compra['DNI'] == dni_cliente and compra['Fecha'] == fecha_compra:
            compras_cliente_fecha.append(compra)
            nombre_producto = compra['Producto']
            precio = compra['Precio']
            descuento = compra['Descuento']
            cantidad_total = compra['Cantidad Total']
            importe_descuento = cantidad_total - compra['Importe con Descuento']
            total_importe_fecha += compra['Importe con Descuento']
            
            print(f"Producto: {nombre_producto}, Precio: {precio}, Importe sin Descuento: {cantidad_total}, Importe con Descuento: {compra['Importe con Descuento']}, Descuento aplicado: {importe_descuento}")

    if compras_cliente_fecha:
        print(f"\nListado de compras de {dni_cliente} en la fecha {fecha_compra}:")
        for compra in compras_cliente_fecha:
            print(f"Producto: {compra['Producto']}, Cantidad: {compra['Cantidad']}, Precio: {compra['Precio']}, Descuento: {compra['Descuento']}, Importe Total: {compra['Cantidad Total']}, Importe con Descuento: {compra['Importe con Descuento']}")
        print(f"\nImporte total de las compras realizadas por {dni_cliente} en la fecha {fecha_compra}: {total_importe_fecha}\n")
    else:
        print(f"\nNo se encontraron compras para el cliente {dni_cliente} en la fecha {fecha_compra}.\n")

# Mostrar menú específico para el programa 2.
def mostrar_menu_2():
    print("Menú:")
    print("1. Cargar fichero de compras.")
    print("2. Añadir compra.")
    print("3. Añadir nuevo precio.")
    print("4. Mostrar producto por clientes.")
    print("5. Eliminar producto de una compra.")
    print("6. Listar nombres de productos.")
    print("7. Listar compras de un cliente en una fecha.")
    print("8. Salir.")

# 3. Funcion de Modificar el Precio.
def modificar_precio(compras):
    nombre_producto = input("Ingresa el nombre del producto: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))

    precio_modificado = False
    for compra in compras:
        if compra['Producto'] == nombre_producto:
            compra['Precio'] = nuevo_precio
            precio_modificado = True
    
    if precio_modificado:
        with open("compras.txt", 'w') as archivo:
            for compra in compras:
                archivo.write(f"{compra['DNI']},{compra['Fecha']},{compra['Producto']},{compra['Cantidad']},{compra['Precio']},{compra['Descuento']}\n")
        print(f"\nEl precio del producto '{nombre_producto}' ha sido modificado en todas las compras.\n")
    else:
        print(f"\nNo se encontró el producto '{nombre_producto}' en las compras.\n")



def compras_cliente(compras):
    dni_cliente = input("Ingresa el DNI del cliente: ")

    compras_cliente = [compra for compra in compras if compra['DNI'] == dni_cliente]

    numero_compras = len(compras_cliente)

    print(f"\nEl cliente con DNI {dni_cliente} ha realizado {numero_compras} compra(s).\n")
