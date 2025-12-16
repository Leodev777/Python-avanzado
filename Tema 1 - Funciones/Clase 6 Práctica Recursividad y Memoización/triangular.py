"""Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
número triangular. Un número triangular se obtiene al sumar todos los 
números naturales desde 1 hasta n."""

def numero_triangular(numero):
    """Calcular el valor del numero triangualr de numero"""
    # INPUT: numero == int
    # OUPUT: int positivo

    # caso base
    if numero == 1: # si el numero es 1 retorna 1
        return 1
    else:
        # caso recursivo
        return numero + numero_triangular(numero -1) #
    # Ejemplo de uso
print(numero_triangular(990)) # salida 