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
        print(f"producto: {venta['producto']}, precio: {venta['precio']}") # ---> mostramos el producto y el precio de cada venta