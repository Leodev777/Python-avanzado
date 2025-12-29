# Comprobar si el archivo esta disponible, si lo esta imprime el contenido
filename = ["cat.txt", "dog.txt"]

for filenames in filename:
    try:
        with open(filename, "r") as file:
            print(f"Contenido del {filename}")
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
            print(f"No se encuentra el archivo")
            pass
    