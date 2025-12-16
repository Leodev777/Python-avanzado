# Sumar elementos de una lista

def sumar_lista(lista):
    """Sumar todos los elementos de una lista"""
    # INPUT: lista
    # OUTPUT: suma
    if len(lista) == 1: # si lista es = a 1 retorna el unico lemento de la lista
        return lista[0]
    # Recursividad
    return lista[0] + sumar_lista(lista[1:]) # sumar el primer elemento con la suma del resto de la lista
# Caso de uso
lista = [5,5 ,5 ,5]
print(sumar_lista(lista))