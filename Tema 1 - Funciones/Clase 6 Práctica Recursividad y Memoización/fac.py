# Factorial es: el producto de todos los numeros enteros posirivos desde el 1 hasta n
# # 1 x 2 x 4
# Factorial de N 1x2x3x4x...xn

def factorial(intro_num):
    """"Calcular el factorial de una numero entero poisitivo n
    INPUT:
    - n: int
    OUTPUT:
    - resultado: int
    """
    # Caso base
    if intro_num == 0 or intro_num == 1: # El factorial de 0 y 1 es 1
        return 1
    # Plantear la sentencia recursiva
    else:
        return intro_num * factorial(intro_num - 1)
    # Caso de uso

    factorial(3) 
    """
    3 * factorial(2)
    3 * 2 * facotorial(1)
    3 * 2 * 1 = 6
    """