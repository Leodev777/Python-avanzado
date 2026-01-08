""""
programacion

Python es un lenguaje de programacion orientad a objetos

Objetos y clases!

Clases: Es una representacion de algo del mundo real ej: Silla cosa con 4 patas, mas sus detalles colores
etc, pero en si silla es una Clases

otro ej un coche: el concepto de clase es el coche, y luego sus caracteristicas colores etc son los Objetos
que perteneces a la clase coche

Luego el OBJETO es una realizacion o instancia de esa clase por ejemplo el coche es color ROJO, esta Tuneado, Sin techo esto seria el OBJETO

    Estos objetos tienen 2 elementos fundamentales: 
        1. Los Atributos: DATOS: Motor, Color, Puertas (son datos que pertenecen a este coche, color, etc)
        2. Metodos: FUNCIONALICADES: Acelerar, Girar, Tocar bocina (Que puede hacer ese coche)

        EJ: class Fruta:
                def _init_(self): ----> Funcion de inicializacion
                    self.nombre = "Manzana" -----> Atributos
                    self.color = "Rojo" -----> Atributos

                    # Ahora designamos una variable a mi clase
            mi_fruta = Fruta() ---> Podemos asignar nuestra clase a una variable
                                ---> Esto es una instaciacion de la clase fruta
            print(mi_fruta.color) ---> Accedemos al color
            print(mi_fruta.nombre) ---> Accedemos al nombre
Tambien podemos reasignar valores
            mi_fruta.color = "Verde"
            mi_fruta.nombre = "Pera"
            print(mi_fruta.color)
            print(mi_fruta.nombre)

            
En terminos generales la clase seria a nivel conceptual general y poder asignar valores correspondientes a cada inicializacion

class Fruta:
    def _init_(self, nombre, color): # Va a tener cmo parametro de entrada el nombre y el color de la fruta y tenemos que dar el color, esto 
        self.nombre = nombre # Asignamos los parametros a los atributos
        slef.color = color # Asignamos los parametros a los atributos

mi_fruta = Fruta("Manzana", "Rojo") # Argumentos que entran entro de la funcion de inicializacion que el pasamos a la clase furta para que se pasen a la funcion de inicializacion
print(mi_fruta.color)
print(mi_fruta.nombre)
            
Esto nos permite crear muchos tipos de frutas

# INSTANCIAS #
manzana = Fruta("Manzana", "Rojo")
platano = Fruta ("Platano", "Amarillo")
kiwi = Fruta ("Kiwi", "Verde")

# CLASE #
class Fruta:
    def __init__(self, nombre, color):
    self.nombre = nombre
    self.color = color

permite crear muchas instancias de la clase fruta

Para cada uno de estos objetos voy a poder acceder a los atributos que claramente son difirentes para cada objeto

Hasta ahora vimos los Atributos de los objetos, ahora vamos a pasar al tema de los metodos
como añadir funcionalidades, son funciones relacionadas con objetos

class Fruta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    def details(self): # Añadimos de esta funcion que hace un print de los detalles de este objeto (Este es el metodo)
        print("mi " + self.nombre + " es " + self.color)
            
        
manzana = Fruta ("Manzana", "Rojo")
manzana.details()

mi manzana es roja
            
Al pasar self a todos los metodos podemos usar los mismos atributos en todos los metodos de nuestra clase

Aunque ambos metodos estan haciendo cosas completamente diferentes, pueden acceder a los mismos atributos

class Fruta:
    def __init__(self, nombre, color): ---> metodo a
        self.nombre = nombre
        self.color = color

    def details(self): ---> metodo b
        print("mi " + self.nombre + " es " + self.color)

Esto se puede hacer con el metodo SELF para poder accerder a los mismos atributos con diferentes funciones
            
¿Como usamos? como lo llamamos?

class Fruta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def details(self):
        print("mi " + self.nombre + " es " + self.color)

manzana = Fruta("Manzana", "Rojo")
manzana.details() ---> llamada al metodo

Metodo: __INIT__

1. Es ejecutado automaticamente con cada nueva instancia de una clase (Jno necesitamos llamarlo como al restro de métodos)
    a diferencia de details que la tenemos que llamar a __init__ no debemos llamarla, podemos acceder directamente a los atributos
2. Es donde inicializamos los atributos
3. Tiene el nombre reservado

class mi_clase:
    def __init__(self):
        self.attrib = []  

        
"self" es la referencia a la instancia actual de un objeto y se usa para acceder a sus atributos y métodos. (Osea se llama asi mismo)
            
Esto es lo que conforma la programacion orientada a objetos
1. Set de principios de programacion
2. Trabajamos con objetos en vez de con datos y procedimientos separados
3. Unimos data y funcionalidad en una sola estructura creando objetos que interacturan entre ellos

FUNCIONES ----> METODOS
VARIABLES CON PREFIJO SELF ---> ATRIBUTOS
INSTANCIA DE UNA CLASE ---> OBJETOS
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
"""         