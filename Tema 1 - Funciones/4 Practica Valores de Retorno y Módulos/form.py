# Funcion para validar
def validator_form (name, email, phone):
    """Esta funciona valida si los datos ingresados son correctos"""

    # Parameters
    ## Name: str
    ## Email: str
    ## Tel: str
    if len(name) < 3:
        return False
    
    if "@" not in email or "." not in email:
        return False
    if len(phone) <=9 or not phone:
        return False
    
    return True

# Pedir informacion al usuario
name = input("What´s your Name: ")
email = input("What´s your Email: ")
phone = input("What´s your number Phone: ")

# Validamos el fomrulario
form_val = validator_form(name, email, phone)
# Comprobar
if form_val:
    print("Form OK")
else:
    print("Form Not OK")

# Valirdar formulario
## Si la validacion da true --> formulario valido
## false --> Formulario invalido