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
# Recomendable especificar cada tipo de error.

#try:
#    print(5/0)
#except ZeroDivisionError: # Es recomendable especificar el tipo de error, si solo ponemos except no es buena practica
#    print("No puede dividir por cero")

# Lo bueno de esto es que no tendemos un CRASH del programa! ya que indicamos el manejo del error.

# EVITAR CRASHES

"""""" 

""""""

print("Dame 2 numeros para dividir")
print("Introduce 's' para salir.")

while True:
    numero1 = input("\nPrimer numero: ")
    if numero1 == 's':
        break
    numero2 = input("\nIngrese el segundo numero: ")
    if numero2 == 's':
        break
    try:
        resultado = int(numero1) / int(numero2)
    except ZeroDivisionError:
        print("No puedes dividir por 0")
    else:
        print(resultado)


# FileNotFound

filename = "test.txt"
try:
    with open(filename) as f_obj:
        contenido = f_obj.read()
except FileNotFoundError:
    msj = "El archivo " + filename + " no existe."
    print(msj)

# Analisis de texto

else: # contar cantidad de palabras de un file
    palabras = contenido.split()
    num_palabras = len(palabras)
    print("El archivo " + filename + " tiene " + str(num_palabras) + " palabras.")

# Que errores debemos reportar?

# Si el usuario sabe que textos deben ser analizados sabra porque algunos no han podido ser analizados}

# Si en cambio el usuario espero resultados pero no sabe que textos deben analizarse pueden que no necesite saer que hay algunos que estan disonibles

# En resumen: lo mas importante de manejo de errores es: ¿Le interesa al usuario? 
# Dar al usuario justo la informacion necesario porque lo confunde