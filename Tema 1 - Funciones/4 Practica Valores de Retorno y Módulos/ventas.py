# Nuestra estructura sera una lista de deiccionarios
# [{producto: "nombre producto", precio:}
# {producto: "nombre producto", precio: precio
#.

ventas = []

def agregar_venta (producto, precio): # ---> datos de entrada
    """Agregamos la ventas a la base de datos"""
    venta = {"producto": producto, # ---> guardamos los datos de entrada en un diccionario PRODUCTO
             "precio": precio} # ---> guardamos los datos de entrada en un diccionario PRECIO
    ventas.append(venta) # ---> agregamos una nueva lista y vamos guardanto las ventas con .append (sirve para agregar elementos a una lista)

def mostrar_ventas(): # ---> funcion para mostrar las ventas
    for venta in ventas:
        print(f"Producto: {venta['producto']} Precio: {venta['precio']}") # ---> mostramos el producto y el precio de cada venta


# Ejemplo de uso
agregar_venta("Pecera", 34.67)
agregar_venta("Piedra de rio tokenizado", 1200.00)
agregar_venta("Electrodos punta de madera", 10.00)

mostrar_ventas()