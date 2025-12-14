# Genera contraseñas seguras de forma aleatoria

import random
import string

def generar_contrasena_segura(
    longitud=12,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_caracteres_especiales=True
):
    caracteres = ""

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    # Construimos la contraseña eligiendo caracteres al azar
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))

    return contrasena
