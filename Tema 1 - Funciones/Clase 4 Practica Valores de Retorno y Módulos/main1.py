# Solicita una contraseña, la valida y, si no es segura, sugiere una nueva

import validador
import generador

def solicitar_contrasena_segura():
    # Pedimos la contraseña al usuario
    contrasena = input("Por favor, ingrese una contraseña: ")

    # Validamos la contraseña usando el modulo validador
    es_valida = validador.validar_contrasena(contrasena)

    if es_valida:
        print("Contraseña OK")
    else:
        print("Contraseña no segura")
        # Generamos una contraseña segura como sugerencia
        sugerencia = generador.generar_contrasena_segura(longitud=12)
        print(f"Sugerencia de contraseña segura: {sugerencia}")

# Punto de entrada real del programa
solicitar_contrasena_segura()
