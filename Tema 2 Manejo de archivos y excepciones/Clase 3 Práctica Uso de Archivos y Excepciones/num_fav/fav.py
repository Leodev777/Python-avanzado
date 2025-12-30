import json  # Permite serializar y deserializar datos en formato JSON

# Pedir numero favorito
# Guardar
# Comprobar si se guardó el numero favorito
# Imprimir número favorito

def comprobar_fav():
    """Comprueba si existe un archivo con el número favorito y, si existe, lo devuelve"""
    try:
        # Abre el archivo en modo lectura
        with open("numero_fav.json", "r") as file:
            # Carga el número desde el archivo JSON
            num_fav = json.load(file)
            # Devuelve el número favorito
            return num_fav
    except FileNotFoundError:
        # Si el archivo no existe, devuelve None
        return None           

def guar_num_fav(num_fav):
    """Guarda el número favorito ingresado por el usuario"""
    # Abre (o crea) el archivo en modo escritura
    with open("numero_fav.json", "w") as file:
        # Guarda el número favorito en formato JSON
        json.dump(num_fav, file)

def preg_num_fa():
    # Solicita al usuario su número favorito y lo convierte a entero
    num_fav = int(input("Cual es tu numero favorito: "))
    # Guarda el número ingresado
    guar_num_fav(num_fav)
    # Devuelve el número favorito
    return num_fav

def print_fav(num_fav):
    # Imprime el número favorito
    print(f"Tu numero favorito es ... {num_fav}")

# Uso del programa

# Intenta obtener el número favorito desde el archivo
numero_fav = comprobar_fav()

# Si el archivo existe (None significa que no existe)
if numero_fav is not None:
    # Imprime el número recuperado
    print_fav(numero_fav)
else:
    # Pide el número al usuario
    numero_fav = preg_num_fa()
    # Imprime el número recién guardado
    print_fav(numero_fav)

"""
Explicación del flujo del programa:

Inicio.
Se intenta leer el número favorito desde un archivo JSON.
Si el archivo no existe, la función devuelve None.
El programa evalúa el resultado.
Si el valor es distinto de None, significa que ya hay un número guardado y se imprime.
Si el valor es None, se solicita el número al usuario.
El número ingresado se guarda en el archivo.
Se imprime el número favorito.
Fin.

"""