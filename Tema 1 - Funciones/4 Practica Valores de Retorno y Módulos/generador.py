import random # Esta libreria nos permite generar selecciones aleatorias
import string # Estra libreria nos permite acceder a conjuntos de caracteres predefinidos con .ascii_uppercase, .ascii_lowercase, .digits, .punctuation
# Importante: recordar instalar librerias si es necesario

# Funcion para generar una contraseña segura
def generar_contrasena_segura(longitud, incluir_mayusculas = True, incluir_minusculas = True, incluir_numeros = True, incluir_caracteres_especiales = True):
    """Genera una contraseña segura basada en los criterios especificados"""

    
    caracteres = "" # Generamos un string vacio para ir agragando los tipos de caracteres

    if incluir_mayusculas: # Agregamos mayus
        caracteres += string.ascii_uppercase
    if incluir_minusculas: # Agregamos minus
        caracteres += string.ascii_lowercase
    if incluir_numeros: # Agregamos numeros
        caracteres += string.digits
    if incluir_caracteres_especiales: # Agregamos caracteres especiales
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) # Generamos la contraseña seleccionando aletatoriamente

    return contrasena # Devolvemos pass generada