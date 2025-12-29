# Envolver en while infinito - brack
# Pedir dos numeros al usuario
# Controlar el error: str en vez de int
# Sumar 2 numeros
while True:
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        result = num1 + num2 
        print("El resultado es ", result)
        break


    except ValueError:
        print("Solo numeros enteros")




