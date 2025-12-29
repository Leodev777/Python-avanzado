# Leer el archivo pi
# Guardar el contenido ----------> .read
# Buscar el string dentro de pi ---> .find()

def buscar_str(filename, string):
    """Busca fecha de nacimiento dentro del archivo de las 10k primeras cifras"""

    #Abrir archivo
    with open(filename, "r") as file:
        digitos = file.read() # Leer contenido
        posicion = digitos.find(string) # Encontrar posicion del srting

        return (posicion) # Devikver la posicion
    

# Ej uso:

filename = "pi_10k.txt"
fecha = "250585" # -1 si no encuentra y 0 si encuentra

# Preguntamos posicion de la fecha en el file
posicion = buscar_str(filename, fecha)
if posicion != -1:
    print(f"Tu fecha de Nacimiento es: {fecha} se encontron en las posicion {posicion}")
else:
    print(f"Tu fecha de Nacimiento es: {fecha} no se encontro en los primeros 10k")

