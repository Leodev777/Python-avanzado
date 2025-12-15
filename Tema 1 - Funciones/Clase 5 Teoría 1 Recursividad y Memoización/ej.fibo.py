# Serie de Fibonacci
# Es una secuencia donde cada numero es la suma de los dos anteriores
# 0 1 1 2 3 5 8 13 21 ... siempre es la suma de los 2 numeros anteriores
#  . . . 5*5, 8*8, 13*13, 21*21 . . .

# indice 1 2 3 4 5 6 7 8
# numero 0 1 1 2 3 5 8 13 21

def fibonacci(indice):
    if indice <= 1:
        return indice
    else:
        return fibonacci(indice-1) + fibonacci(indice-2) # llamada recursiva, llama al ultimo y al penultimo numero del indice

print(fibonacci(8)) # 21 porque es el numero en la posicion 8 = 21 (0,1,1,2,3,5,8,13,21)

for i in range(0,11):
    print(fibonacci(i))