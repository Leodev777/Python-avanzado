# Solicitar una contraseña

# Validar la contraseña

## Contraseñas no avalida --> sugerir nueva contraseña

def solicitar_contrasena_segura():
    contrasena = input("Por favor, ingrese una contraseña: ")
    valida = validar_contrasena(contrasena)

    if valida:
        print("Contraseña OK")
    else:
        print("Contraseña no segura, ingrese nueva contraseña :")
        sugerencia = generar_contrasena_segura()
        print(f"Sugerencia de contraseña segura: {sugerencia}")
    
    # Ejemplo
    solicitar_contrasena_segura()