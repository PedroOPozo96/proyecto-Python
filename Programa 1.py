from Funciones import (
    añadir_compra, mostrar_producto_por_clientes, eliminar_producto, 
    listar_productos_comprados, listar_compra_fecha, modificar_precio, compras_cliente
)

def mostrar_menu():
    print("Menú:")
    print("1. Añadir compra.")
    print("2. Añadir nuevo precio.")
    print("3. Mostrar producto por clientes.")
    print("4. Eliminar producto de una compra.")
    print("5. Listar nombres de productos.")
    print("6. Listar compras de un cliente en una fecha.")
    print("7. Salir.")

compras = []
cliente_por_producto = {}

programa_principal = True

# Programa Principal
while programa_principal:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        añadir_compra(compras, cliente_por_producto)
    elif opcion == '2':
        modificar_precio(compras)
    elif opcion == '3':
        mostrar_producto_por_clientes(cliente_por_producto)
    elif opcion == '4':
        eliminar_producto(compras, cliente_por_producto)
    elif opcion == '5':
        listar_productos_comprados(compras)
    elif opcion == '6':
        listar_compra_fecha(compras)
    elif opcion == '7':
        compras_cliente(compras)
    elif opcion == '8':
        programa_principal = False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
