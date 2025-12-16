# Potencia

def potencia(base, exponente):
    """Calcular la potencia de una base elvada a un exponente"""
    # INPUT: base (int), exponente (int)
    # OUTPUT: resultado (int)
    if exponente == 0:
        return 1
    # Recursividad
    return base * potencia(base, exponente -1)
# Caso de uso
potencia(10,2) # 100

print(potencia(10,2))