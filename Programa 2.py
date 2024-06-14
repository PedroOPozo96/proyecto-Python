from Funciones import (
    fichero_compra, añadir_compra, mostrar_producto_por_clientes, eliminar_producto, 
    listar_productos_comprados, listar_compra_fecha, modificar_precio, mostrar_menu_2
)

compras = []
cliente_por_producto = {}

programa_principal = True

# Segundo Programa Principal 
while programa_principal:
    mostrar_menu_2()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        fichero_compra(compras, cliente_por_producto)
    elif opcion == '2':
        añadir_compra(compras, cliente_por_producto)
    elif opcion == '3':
        modificar_precio(compras)
    elif opcion == '4':
        mostrar_producto_por_clientes(cliente_por_producto)
    elif opcion == '5':
        eliminar_producto(compras, cliente_por_producto)
    elif opcion == '6':
        listar_productos_comprados(compras)
    elif opcion == '7':
        listar_compra_fecha(compras)
    elif opcion == '8':
        programa_principal = False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
