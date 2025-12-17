# El objetivo es manejrar errores para que nuestros programas no tengan un crash cuando
# se encuentren con situaciones inesperadas.

# Ademas sirve para que alguien no tecnico pueda ver de que trata el error que esta pasando
# Esto añade solidez y estabilidad a nuestro codigo
# A esto lo llamamos EXCEPCIONES

# Error Zero
# print(5/0)
# Salida: ZeroDivisionError: division by zero : Objeto de excepcion
# se crea cuando python no puede realizar aquello que se le pide

# Para esto el uso de bloques try-except

try:
    print(5/0)
except ZeroDivisionError: # Es recomendable especificar el tipo de error, si solo ponemos except no es buena practica
    print("No puede dividir por cero")

