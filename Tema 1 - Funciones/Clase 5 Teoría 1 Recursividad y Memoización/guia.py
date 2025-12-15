# Guia de estilo:

#Funciones y moduloes deben tener nombres descriptivos en minusculas y con "_" separando las palabras.
# Las funciones deben incluir un comentario conciso que ecplique su funcion en fomatro DOCSTRING """"""
# Sabiendo el nombre de la funcion, los argumentos necesarios y los valores de retorno cualquier
# programador debe poder integrar la funcion en sus programas


# def nombre_funcion (parametro_0, parametro_1='valor por defecto')

# llamada_funcion(parametro_0, parametro_1="valor")

# NO DEBE HABER ESPACIOS ALREDEDORR DEL "=" EN LOS ARGUMENTOS DE UNA FUNCION


# GUIA DE ESTRILO
# PEP 8 - https://peps.python.org/pep-0008/
# PEP 257 - https://peps.python.org/pep-0257/
# Google Python Style Guide - https://google.github.io/styleguide/pyguide.html
#    """
#    Descripcion concisa de la funcion y su proposito.
#
#    Args:
#        parametro_0 (tipo): Descripcion del parametro 0.
#        parametro_1 (tipo, opcional): Descripcion del parametro 1. Valor por defecto es 'valor por defecto'.
#
#    Returns:
#        tipo: Descripcion del valor retornado.
#    """
#    # Cuerpo de la funcion
#    pass


# Recomienda limitar las lineas de codigo a 79 caracteres.
# def nombre_funcion(
#        parametro_0, parametro_1, parametro_2,
#        parametro_3, parametro_4, parametro_5):
#    # cuerpo de la funcion
#    pass

# La separacion entre la definicion de ldos funciones de dos lineas en blanco
# los import deben escribirse al comienzo del script despues de los comentarios que describen el programa al completo

#___________________
#name
#porpose:
#author                   ----------> Informacion general
#created
#update
#_____________________

# import
# import                    ------------> Importacion de modulos
# from arcy import evn

#________________

# set thr curren ....
# to the feature ...       ------> Comentarios la secciones del script
# rums unionr ...
#________________

# no se importa nada en las funciones, solo en ocasiones excepcionales: como por ejemmplo 
# para evitar dependencias o problemas de importaciones circulares

# Recursividad: Concepto basico en computer scince: Se basa en dividir el problema en sub-problemas
# faciles de resolver uno a uno y resolver el problema original
# Se trata de llamar una funcion dentro de si misma

# def recursividad(i):
#    if i ==1:
#        return i
#    else:
#        return recursividad(i-1)
    
# Caso base es cuando llega a 1 a eso se le llama caso base
# recursividad(100)

# EJ:

def numeros_pares(num):

    print(num)
    if num == 2: # Si el numero es igual a 2 devuelvo el numero
        return num # ---> Caso base
    else: 
        return numeros_pares(num - 2) # Llamada recursiva
    
numeros_pares(8)

