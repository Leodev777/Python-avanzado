# Memoizacion implementacion explicita

fibonacci_cache = {} # diccionario para almacenar los resultados de fibonacci ya calculados

def fibonacci_ca(indice):
    # Si tenemos el valor en cache lo devolvemos
    if indice in fibonacci_cache: # verifica si el indice ya fue calculado
        return fibonacci_cache[indice] # devuelve el valor almacenado en cache
    
    # Calcular el termino de orden n
    if indice <= 1: # caso base
        valor = indice # devuelve el indice si es 0 o 1
    else:
        valor = fibonacci_ca(indice-1) + fibonacci_ca(indice-2) # llamada recursiva para calcular el valor de fibo

    # Guardar el valor en cache y devolverlo
    fibonacci_cache[indice] = valor # almacena el valor calculado en el diccionario
    return valor

# Implementacion IMPLICITA

from functools import lru_cache # importamos el decorador lru_cache
@lru_cache(maxsize = 20) # maxsize es el numero maximo de resultados a almacenar en cache
def fibo_cache_implicito(indice): # funcion con memoizacion implicita
    if indice <= 1: 
        return indice
    else:
        return fibo_cache_implicito(indice-1) + fibo_cache_implicito(indice-2) # llamada recursiva

def fibo_inter(indice): # funcion iterativa
    secuencia = [0,1]
    for i in range(indice):# iteramos hasta el indice
        secuencia.append(secuencia[-1] + secuencia[-2]) # agregamos el siguiente numero a la secuencia

    return secuencia[-2] # devolvemos el numero en la posicion indice