# Trabajar con archivos JSON

"""  
En muchos programas queremos guardar el INPUT de los usuarios.
EJ preferencias en un juego o datos de visualizacion

Guardamos la informacion en estructuras de datos como lsitas o diccionarios

Cuando se cierra el programa queremos que la ifnromacion de los settings no se pierda.
Para eso podemos guardar la infomracion en archivos tipo JSON

JSON = JavaScript Objet Notation
Desarrollado originalmente para JavaScript

"""

import json

numeros = [2,3,5,11,92,13]
filename = 'numeros.json' # Creamos file con extension .json
with open(filename, 'w') as f_obj: # Abrimos archivo en modo escritura
    json.dump(numeros, f_obj) # y para escribir el objeto dentro de este file usamos json.dump

# DUMP: convierte un objeto de python en un JSON STRING
# numeros: DATOS
# f_obj: ARCHIVO



# Leer

filename = 'numeros.json'
with open(filename) as f_obj: # Abrimos el archivo en reading mode
    numeros = json.load(f_obj) # load convierte json string en un objeto de python
    print(numeros)