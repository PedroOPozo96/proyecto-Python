# proyecto-Python


El programa debe mostrar el siguiente menú:
1. Añade compra (se solicita DNI del cliente, fecha de compra, nombre del
producto, cantidad, precio y descuento).
2. Muestra cuántos clientes han comprado un producto (si el producto no
existe da un error).
3. Elimina un producto de una compra (se solicita DNI del cliente, fecha de
compra y nombre del producto).
4. Lista los nombres de los productos comprados.
5. Listado de compra de un cliente en una fecha ordenadas por producto (debe
aparecer nombre del producto, precio, importe con descuento. Al final del
listado hay que incluir el importe total de las compras realizadas por ese
cliente en esa fecha).
6. Salir.
Crea un nuevo programa Python que modifique el punto 1 del ejercicio anterior
de forma que la primera opción del menú lea la información del fichero ficticio
(compras.txt) que tiene la siguiente estructura: DNI del cliente, fecha de
compra, nombre del producto, cantidad, precio y descuento. Al finalizar el
programa, el fichero compras.txt debería tener la información actualizada
(opcional). Además, en el mismo se deben emplear excepciones.
En los dos programas cada compra se puede almacenar en un diccionario y se
debe usar al menos una función para el menú que devuelva un entero con la
opción escogida y otra para cada una de las opciones.
