"""
CUATRO PILARES DEL POO

1. Abstraccion: Simplificacion y representacion de entidades del mundo real
en forma de objetos en el codigo.

2. Encapsulamiento: Agrupamiento de datos (atributos) y metodos (funciones)
relacionados en un mismo objeto.

3. Herencia: Capacidad de una clase (subclase) de heredar atributos y metodos
de otra clase (superclase).

4. Polimorfismo: Capacidad de distintos objetos de responder de forma distinta
a una misma llamada de metodo.
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

    def actualizar_km(self, km):
        """Actualiza el valor del cuenta KM al valor dado"""
        if km >= self.km:
            self.km = km
            print(f"OK: Kilometraje actualizado a {km} km")
        else:
            print(f"ERROR: No puede quitar KM. Actual: {self.km} km, Intentado: {km} km")

    def aumentar_km(self, km_adicionales):
        """Incrementa los km"""
        if km_adicionales >= 0:
            self.km += km_adicionales
            print(f"OK: Se anadieron {km_adicionales} km. Total: {self.km} km")
        else:
            print(f"ERROR: No se pueden anadir kilometros negativos")


mi_coche = [
    Coche('audi', 'a4', 2020, 'Rojo', 5892),
    Coche('audi', 'a3', 2022, 'Negro', 125523),
    Coche('audi', 'a4', 2021, 'Azul', 23541),
    Coche('audi', 'a1', 2025, 'Blanco', 12542),
    Coche('audi', 'a3', 2023, 'Gris', 232),
    Coche('audi', 'a2', 2026, 'Rojo', 685),
]

print("=== Antes de actualizar ===")
for coche in mi_coche:
    print(coche.crear_descr())
    print(coche.leer_km())
    print()

# Actualizar km de algunos coches
mi_coche[0].actualizar_km(6000)
mi_coche[2].actualizar_km(25000)
mi_coche[4].actualizar_km(1000)

print("\n=== Despues de actualizar ===")   
for coche in mi_coche:
    print(coche.crear_descr())
    print(coche.leer_km())
    print()

# Intentar reducir kilometros (deberia fallar)
print("=== Intentando reducir kilometros ===")
mi_coche[0].actualizar_km(5000)  # Intentar reducir de 6000 a 5000

# Aumentar kilometros
print("\n=== Aumentando kilometros ===")
mi_coche[0].aumentar_km(500)
print(mi_coche[0].leer_km())

# Intentar anadir kilometros negativos
print("\n=== Intentando anadir kilometros negativos ===")
mi_coche[1].aumentar_km(-1000)
print(mi_coche[1].leer_km())

print("\n" + "="*50)
print("SUPER CLASE: COCHE")
print("CLASE HIJO: COCHE ELECTRICO (CHILD CLASS, SUBCLASS O CLASE HIJO)")
print("="*50 + "\n")

"""
HERENCIA PARA CREAR UNA CLASE HIJA:
"""

class CocheElectrico(Coche): # Nombre de super clase
    """Representa aspectos especificos de un coche electrico."""
    
    def __init__(self, marca, modelo, anio, color, km, bateria):
        """Inicializa atributos de la clase padre (Coche)"""
        super().__init__(marca, modelo, anio, color, km) # Conectamos a la super clase
        self.bateria = bateria  # Capacidad de la bateria en kWh
        
    def descripcion_bateria(self):
        """Describe la capacidad de la bateria"""
        return f"Este coche tiene una bateria de {self.bateria} kWh."
        
    # Sobreescribir el metodo crear_descr para incluir info de electrico
    def crear_descr(self):
        nombre_extenso = (
            str(self.anio) + ' ' +
            self.marca + ' ' +
            self.modelo + ' ' +
            self.color + ' (Electrico)'
        )
        return nombre_extenso.title()


print("=== CREANDO Y PROBANDO COCHES ELECTRICOS (TESLA) ===")

# Crear coches electricos (Teslas)
mi_tesla1 = CocheElectrico('tesla', 'model s', 2023, 'Rojo', 12000, 100)
mi_tesla2 = CocheElectrico('tesla', 'model 3', 2024, 'Azul', 5000, 75)
mi_tesla3 = CocheElectrico('tesla', 'model x', 2023, 'Blanco', 25000, 95)

# Lista de coches electricos
mis_coches_electricos = [mi_tesla1, mi_tesla2, mi_tesla3]

print("\n=== Informacion de los Teslas ===")
for tesla in mis_coches_electricos:
    print(tesla.crear_descr())
    print(tesla.descripcion_bateria())
    print(tesla.leer_km())
    print()

# Probar que hereda todos los metodos de Coche
print("=== Probando herencia de metodos ===")
print("1. Aumentar kilometros a un Tesla:")
mi_tesla1.aumentar_km(300)
print(mi_tesla1.leer_km())

print("\n2. Intentar actualizar kilometros a un valor menor:")
mi_tesla2.actualizar_km(4000)  # Deberia fallar (actual: 5000)

print("\n3. Actualizar kilometros a un valor mayor:")
mi_tesla2.actualizar_km(6000)  # Deberia funcionar
print(mi_tesla2.leer_km())

print("\n=== Mezclando coches normales y electricos ===")
todos_los_coches = mi_coche + mis_coches_electricos

print(f"Total de coches: {len(todos_los_coches)}")
print(f"- Coche normales: {len(mi_coche)}")
print(f"- Coches electricos: {len(mis_coches_electricos)}")

print("\n=== Lista completa de todos los coches ===")
for i, coche in enumerate(todos_los_coches, 1):
    print(f"{i}. {coche.crear_descr()}")
    if hasattr(coche, 'descripcion_bateria'):
        print(f"   {coche.descripcion_bateria()}")
    print(f"   {coche.leer_km()}")
    print()


# Para que funcione la Subclase debe estar definida despues de la Superclase


""" Una vez el coche electrtico heredo los atributos y metdos de la superclase coche, podemos
añadir metodos que solo apliquen a los cocches electicos
"""

"""
POLIMORFISMO: Diferentes clases pueden tener metodos con el mismo nombre pero
comportamientos distintos.
"""

"""
Cuando estemos modelizando un elementyo del mundo real puede que nos encontremos con añadidos
cada vez mas detalles dentro de una clase. Quizas nos encontremos con una lista creciente de atributos y metodos
que hacen que nuestros archivos sean muy extensos.
EJ: Si continuamos añadiendo detalles a la clase CocheElectrico puede que notemos que estamos añadiendo
muchos atributos y metodos realcionados con la bateria del coche.
En estos momentos toca para y movver estos atributos y metodos a una nueva clase llamada Bateria.
"""

"""
Este ya es un nivel de logica superior donde ya solo pensamos en sintaxis sino realmente
pensando en ocmo modelizar el mundo real de nuestro alrededor.
"""

"""
Algunos enfoques son mas eficientes que otros, pero se necesita practica para encontrar las representaciones
mas eficientes. si tu codigo esta funcionado como deseas! ya lo estas haciendo bien

"""

"""
By Sofware-Craft _Serena
Linkedin: Leo Iglesias
"""