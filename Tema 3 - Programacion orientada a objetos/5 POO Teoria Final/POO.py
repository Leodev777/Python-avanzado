""""
Miembros Privados: EJ: Tenemos un coche que vendemos en 6 mil USD pero cuyo coste
de produccion es de 1000 USD. Esto ultimo no queremos que el usuario lo sepa

Lo que debemos hacer es agregar una variable privada que con __coste
"""

class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__coste = 1000 # Variable private

mi_coche = Coche("Toyota", "Corolla", 2020)
print(f"Mi coche es un {mi_coche.marca} {mi_coche.modelo} del año {mi_coche.anio}.")
print(mi_coche.__coste)

# Esto en realidad no hace al atributo del todo privado
# Para acceder a el tenemos que poner

print(mi_coche._Coche__coste)

# Para que nos interesan?
""""
1. Encapsulacion: Al marcar un atrbuto como privado, estas indicando que se
atributo no debe ser accedido directamente desde fuera de la clase

Esto permite un mejor control sobre los datos son manipulados y protege
la integridad de los datos

2. Control de acceso
Los atributos privados restringen el acceso directo a los datos desde fuera de la clase
Solo los metodos dentro de la misma clase pueden acceder y modificar estos atributos
Esto evita modificaciones accidentales o inaprpiadas

3. Evitar colisiones: Al usar atributos privados, reduces el riesgo de colisiones
de nombres

4. Documentacion y abstraccion
Al marcar los atrivbutos como privados, estas señalando a otros programadores que estos atributos no estan
destiandos a ser accedridos directamente y que deben consultar la documentacion
de la clase para comprender como interactuar adecuadamente con ella
"""""

"""
Importar clases:

from POO impor Coche --> EJ

"""

"""
Guia de estilos...

Variable:
1. Letras minusculas
2 Separamos las palabras con guines bajos
3. Nombres descriptivos

Funciones:
1. Letras minusculas
2. Separamos con guines bajos
3. Usa verbos para describir acciones

Constante:
1. Letra Mayusculas
2. Sepramos las palabras con guines bajos
3. Nombre claros y concisos que trasmitan el prosito de la constante

Clases:
1. Una CamelCase (capitaliza la primerta letra de cada palabra
2. Nombres sustantivos o frases sustantivas que describan el objeto o concepto que la clase representa)
"""

