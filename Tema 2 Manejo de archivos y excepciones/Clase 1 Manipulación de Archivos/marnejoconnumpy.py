#Lectura
import numpy as mp

# Leer datos de un archivo CSV
data = np.loadtxt('datos.csv', delimiter=',')

# Leer datos de texto

data = np.loadtxt('datos.txt')

# Leer datos de un archivo con encabezados

data = np.genfromtxt('datos.csv', delimiter=',', skip_header=1)


# Escritura

# Crear datos

data = np.array([[1,2,3], [4,5,6], [7,8,9]])

# Guardar en CSV

np.savetxt('datos.csv', data, delimiter=',')

# Guardar en TXT

np.savetxt('datos.txt', data)

# Guardar datos en un archivo con encabezados
header = 'columna1,columna2,columna3'
np.savetxt('datos.csv', data, delimiter=',', header=header, comments='')
