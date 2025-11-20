# Codificamos la informacion en sucesiones de 0s y 1s ---> ESTRUCTRUA DE DATOS ---> Estructuracion, manipulacion y almacenamiento de datos 

# La programacion se basa en crear una receta o secuencia de instrucciones ---> ESTRUCTURAS DE PROGRAMACION ----> Manipularemos la informacion (Los datos) para obtener un resultado de la manera mas optima posible.

# La forma

# Paradigmas de programacion: Enfoques o modelos que definen la forma en la que se debe diseñar, estructurar y escribir los programas.

# Programacion imprerativa: Tiene como foco en "COMO SE DEBEN EJECUTAR LAS INTRUCCIIONES" para lograr un resultado.
# estructuracion en una secuencia de comandos que modifican el estado del programa y realizan acciones especificas
# mis_numeros = [1, 2, 3, 4, 5]
# suma = 0
# for numero in mis_numeros:
#    if numero % 2 == 0:
#        suma +- num
# print(suma)

# PROGRAMACION FUNCIONAL: FOCO: Evaluacion de funciones matematicas. Enfoque en la inuatabilidad
# y evitar cambios de estados o sus efectos secundarios.

# mis_ numeros = [1, 2, 3, 4, 5]
# numeros_pares = filter(lambda x: x % 2 == 0, mis_numeros)
# suma = sum(numeros_pares)
# print(suma)

# PROGRAMACION ESTRUCTURADA: FOCO: Division en estructuras de control como bucles y decisiones
#(if statements). Se busca la claridad y la organizacion
# de codigo evitando el uso de saltos no estructudados como el goto.
# el goto es un salto incondicional a otra parte del codigo, lo que puede dificultar
# la lectura y el mantenimiento del mismo.

# mis_numeros = [1, 2, 3, 4, 5]
# suma = 0
# for numero in mis_numeros:
#    if numero % 2 == 0:
#        suma +- num
# print(suma)

# PROGRAMACION ORIENTADA A OBJETOS (POO): FOCO: Los programas se organizan
# alrededor de objetos que representan entidades
# del mundo real. ENcapsulameiento de datos y comportamientos en objetos. 
# conceptos particulares: herencia, polimorfismo y encapsulamiento.

# Ejemplo:
# class NumberList:
#   def __init__(self, numbers):
#       self.numbers = numbers

#   def suma_numeros_eneteros(self):
#       suma = 0
#       for numero in self.numbers:
#           if numero % 2 == 0:
#              suma +- numero
#       return suma
# mis_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mis_numeros_lista = NumberList(mis_numeros)
# print(mis_numeros_lista.suma_numeros_eneteros())


# PARADIGMAS DE PROGRAMACION:

# Muchos lenguajes de programacion admiten multiples paradigmas y permiten combinarlos segun sea necesario.

# La eleccion del paradigma dependel del problema a resolber, la preerencia del desarrollador
# y los requisitos del proyecto.

# -------------------------------------------------
# FUNCIONES: ¿Que es? ----> Bloque de codigo a los que asignamos un nombre
# Estan diseñados para realizar una tarea en especifico
# pueden ser usados repetidamente a lo largo del codigo

# Como creamos una funcion?
# def saludar_usuario(nombre): ----> (): siempre necesario entre parentesis el parametro en este caso nombre
#    """Mostrar un saludo simple por pantalla"""
#    print("Hola {nombre}") ---> instrucciones

# saluda_usuario()
# saluda_usuario("Ana") ---> argumento
# LLAMAMOS LA FUNCION 

# NOMBRE: PARAMETRO
# ANA: ARGUMENTO

# ARGUMENTOS POSICIONALES

# def describir mascota(tipo_animal, nombre_animal):
#    """Mostrar informacion sobre una mascota"""
#    print("tengo un " + tipo_animal + ".")
#    print("Mi " + tipo_animal + " se llama " + nombre_animal + ".")
# describir_mascota("perro", "Rex") ---> argumentos posicionales

# VALORES POR DEFECTO

# def describir_mascota(nombre_animal, tipo_animal="perro"):
#    """Mostrar informacion sobre una mascota"""
#    print("tengo un " + tipo_animal + ".")
#    print("Mi " + tipo_animal + " se llama " / + nombre_animal + ".")
# describir_mascota("Rex") ---> si no se especifica el tipo de animal, se asume que es un perro
# describir_mascota("Michi", "gato") ---> si se especifica el tipo de animal, se usa el valor proporcionado

