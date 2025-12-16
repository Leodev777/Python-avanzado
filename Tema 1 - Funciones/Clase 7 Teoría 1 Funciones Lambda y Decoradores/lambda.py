# Funciones lambda
# Que son? Son funciones ANONIMAS
# Para que se usan? Para abreviar sintaxis y ahorrarnos tiempo

# t0do lo que podemos hacer con una funcion lambda puede hacerse con una funcion nomarl,
# pero no todo lo que podemos hacer con funciones normales puede hacerse con funcioes lambda


# Sintaxis:

def area_triangulo (base, altura):
    return (base * altura) / 2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(10,5)

print(triangulo1, triangulo2)

# Ahora con lambda

area_triangulo = lambda base, altura: (base * altura / 2)

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(10,5)

# No puede tener bucles o condiciones. solo puede devolver un calculo
# tambien les llaman on demand, on the go.

# Ejemplo potencia

al_cubo = lambda numero: numero ** 3
print(al_cubo(3))

# Filtos con funciones lambda

def numero_par(numero):
    if numero % 2 == 0:
        return True
numeros=[63,98,21,94,76,532,10,29,98,283,12,67]
print(list(filter(numero_par, numeros)))
print(list(filter(lambda numero: numero % 2 == 0, numeros))) # : representa el return
# list: convierte el filtro en una lista
# filter: filtra los elementos de una lista segun una condicion

# Funciones lambda como CLAVE
# Ej: SORT
autores = ["Victor Hugo", "Emile Zola", "Honore de Balzac", "Alexandre"]
autores.sort()
print(autores)
# Lambda
autores.sort(key=lambda name:name.split(" ")[-1]) # Ordena por apellido
print(autores)

