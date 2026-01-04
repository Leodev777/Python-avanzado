# Valida si una contraseña cumple criterios de seguridad

def validar_contrasena(contrasena):
    longitud_minima = 8

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    # Verificamos longitud mínima
    if len(contrasena) < longitud_minima:
        return False

    # Recorremos cada carácter de la contraseña
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else:
            tiene_caracter_especial = True

    # Solo es válida si cumple todas las condiciones
    return (
        tiene_mayuscula
        and tiene_minuscula
        and tiene_numero
        and tiene_caracter_especial
    )
