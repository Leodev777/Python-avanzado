# Funciones Decoradores
# Son funciones que añaden funcionalidades a funciones ya
# existentes en nuestro programa

# Estructura
# 3 funciones (a,b,c) donde A recibe como parametro la funcion B y devuelve
# la funcion C

# Un decorador devuelve una funcion que envuelve a otra funcion

# EJ

def funcion_A(funcion_B):
    def funcion_C(): # Codigo de funcion interna
        return(funcion_C)
    

# Ej: podriamos tener muchismas funciones y yo quiero ponerles que diga
# comenzamos con el calculo y lo quiero agregar a todas las funciones
# es tedioso hacer a mano para eso utilizamos las funciones decoradoras
# imagemnos que queremos 2 print uno antes y otros despues del calclu

def suma():
    print(1+2)

def resta():
    print(2-1)


def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("Comenzamos el calculo")
        funcion_parametro()
        print("Hemos terminado el calculo")
    return funcion_interna

    

@funcion_decoradora # @sirve para aplicar el decorador
def suma():
    print(1+2)
@funcion_decoradora
def resta():
    print(2-1)
