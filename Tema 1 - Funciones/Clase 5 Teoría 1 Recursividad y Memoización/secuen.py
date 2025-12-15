def fibonacci(indice):
    secuencia = [0,1]
    for i in range(indice):
        secuencia.append(secuencia[-1] + secuencia[-2])

        return secuencia[-2]
    
for i in range(0,11):
    print(fibonacci(i))


    # Memoizacion: Tecnica de optimizacion utilizada para acelerar las funciones almacenando
    # los resultados de llamadas o funciones costosas y devolviendo el resultado cacheado
    # cuando se llama con los mismos argumentos nuevamente
    # Def: Tenica de optimizacion en la programacion en la cual se almacenan en memoria
    # los resultados de una funcion para evitar reclacularlos en llamadas
    # futuras con los mismos parametros.

    # La memoizacion puede mejorar significativamente el rendimiento de 
    # las funciones que realizan calculos costoros o repetitivos, como en el caso
    # de la serie de fibonacci.
    # By Zeroooooooo! Rooooot!

    