"""
CUATRO PILARES DEL POO

1. Abstracción: Simplificación y representación de entidades del mundo real
en forma de objetos en el código.

2. Encapsulamiento: Agrupamiento de datos (atributos) y métodos (funciones)
relacionados en un mismo objeto.

3. Herencia: Capacidad de una clase (subclase) de heredar atributos y métodos
de otra clase (superclase).

4. Polimorfismo: Capacidad de distintos objetos de responder de forma distinta
a una misma llamada de método.
"""

class Coche:
    def __init__(self, marca, modelo, anio, color, km):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.km = km

    def crear_descr(self):
        nombre_extenso = (
            str(self.anio) + ' ' +
            self.marca + ' ' +
            self.modelo + ' ' +
            self.color
        )
        return nombre_extenso.title()

    def leer_km(self):
        return f"Este coche tiene {self.km} kilometros recorridos."


mi_coche = [
    Coche('audi', 'a4', 2020, 'Rojo', 5892),
    Coche('audi', 'a3', 2022, 'Negro', 125523),
    Coche('audi', 'a4', 2021, 'Azul', 23541),
    Coche('audi', 'a1', 2025, 'Blanco', 12542),
    Coche('audi', 'a3', 2023, 'Gris', 232),
    Coche('audi', 'a2', 2026, 'Rojo', 685),
]

for coche in mi_coche:
    print(coche.crear_descr())
    print(coche.leer_km())
