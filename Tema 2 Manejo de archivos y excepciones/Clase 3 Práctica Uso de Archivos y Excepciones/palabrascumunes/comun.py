# Apariciones de una palabra en un texto
# Abrir txt
# Leer el conteniido, guardarlo en una variable
# comproar la aparicion de una palabra en el texto

def contar_aparicion(filename, palabra):
    """Contar las apariciones de una palabra en un archivo de texto"""
    try:
        with open(filename, "r", encoding="utf-8") as file: # Abro,ps eñ textp
            txt = file.read() 
            conteo = txt.count(palabra) # Guardamos en la variable
            return conteo
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return 0
  
# ejemplo de uso
filename = "texto.txt"
palabra_contar = "python"

ocurrencias = contar_aparicion(filename, palabra_contar)
print(f"La palabra '{palabra_contar}' aparece {ocurrencias} veces.")
















# def contar_aparicion(filename, palabra):
#    """Contar las apariciones de una palabra en un archivo de texto"""
#    with open(filename, "r") as file:
#        # guardar el contenido en una variable
#        txt = file.read() 
#        # contamos el numero de aparicion
#        conteo = txt.count(palabra)
#        return conteo

# ejemplo de uso
#filename = "texto.txt"
#palabra_contar = "python"

#ocurrencias = contar_aparicion(filename, palabra_contar)
#print(ocurrencias)