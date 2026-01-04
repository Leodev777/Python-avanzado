# Objetivo:

"""Aprender a trabajar con archivos y manejar grandes cantidades de datos
Necesario para analizar y modificar informacion
"""
"""
Guardar datos para hacert nuestros programas mas comodos para el usuario
Poder reanuzar la ejecucion de un scripto o guardar mensaje de error
"""
"""Podemos manejar grandes cantidades de datos, todo se trata de manipular informacion
y ademas podemos guardar informacion de distinto tipo o del propio
script.
Ej: 
Tenemos que runnear un script duante muchas horas y varios dias, podemos
poner un OUTPUT que nos de el estado actual del script, procecos etc, que no esta bugueado ni nada
o puede que queramos tener un archivo de salida con los resultados del script
para despues poder analizarlos.

Tambien tenemos archivos de reanudacion, esto nos sirve para luego retomar el script
donde lo dejamos sin tener que volver a empezar desde cero
"""
"""
Leer un archivo, leer informacion dentro de la memoria del script

"""

# ler línea por línea (mejor para archivos grandes)
with open('digitos_pi.txt') as archivo:
    for linea in archivo:  # Itera sobre cada línea
        print(linea.strip())  # strip() elimina saltos de línea

#Leer solo los primeros N caracteres
with open('digitos_pi.txt') as archivo:
    primeros_10 = archivo.read(10)  # Lee solo 10 caracteres
    print(primeros_10)

# 3 leer as las líneas en una lista
with open('digitos_pi.txt') as archivo:
    lineas = archivo.readlines()  # Lista donde cada elemento es una línea
    print(f"Total líneas: {len(lineas)}")

# Open() devuelve un objeto que representa el archivo abierto


"""Leer un archivo"""

# Usar file PATHS RELATIVO
# O podemos usar PATHS ABSOLUTO
# Linux y OS /
# Windows \ 
# Verificar en que versiones cambiar el /\

# Relativo 

with open('path\directorio\digitos_pi.txt') as archivo_objeto:
    contenido = archivo_objeto.read()
    print(contenido)
# Absoluto
file_path = 'C:User\pepe\otros_archivos\archivos_texto\filename.txt'
with open(file_path) as archivo_objeto:
    contenido = archivo_objeto.read()
    print(contenido)

# Tambien puedo leer linea por linea
# Guardar informacion de un archivo

filename = 'digitos_pi.txt'
with open(filename) as archivo_objeto:
    lineas = archivo.objeto.readlines()
    for linea in lineas:
        print(linea.rstrip())

# Salida: ej 3.141592
#            98765488
#            33312341
#  ..................


# Manejar informacion de un archivo.
# Lo que quiero hacer es que todo esos numeros pasarlos a un string 

filename = 'digitos.pi.txt'
with open(filename) as archivo_objeto:
    lineas = archivo_objeto.readlines() 
pi_string = ''
for linea in lineas:
    pi_string +- linea.strip()
print(pi_string)
print(len(pi_string))

# Escritura de archivos
# Archivos vacios

filename = "Programa.txt"
with open(filename, "W") as archivo_objeto:
    archivo_objeto.write("Python")

"""
MODOS DE APERTURA DE ARCHIVOS EN PYTHON
========================================
Este script explica y demuestra todos los modos de apertura de archivos en Python.

Nota: Se crean archivos de ejemplo para las demostraciones. Al final se limpian automáticamente.
"""

# Crear archivo de ejemplo inicial
with open('ejemplo.txt', 'w', encoding='utf-8') as f:
    f.write("Línea 1: Contenido inicial\n")
    f.write("Línea 2: Más contenido\n")

print("=" * 60)
print("DEMOSTRACIÓN DE MODOS DE APERTURA DE ARCHIVOS EN PYTHON")
print("=" * 60)

print("\n Archivo creado para ejemplos: 'ejemplo.txt'")

# ===========================================================================
# 1. MODO 'r' (LECTURA) - PREDETERMINADO
# ===========================================================================
print("\n" + "=" * 60)
print("1. MODO 'r' - LECTURA (predeterminado)")
print("=" * 60)
print("• Abre archivo solo para lectura")
print("• Puntero al inicio del archivo")
print("• Error si el archivo no existe")

try:
    with open('ejemplo.txt', 'r') as archivo:  # 'r' es explícito
        contenido = archivo.read()
        print(f" Contenido leído:\n{contenido}")
except FileNotFoundError as e:
    print(f" Error: {e}")

# ===========================================================================
# 2. MODO 'w' (ESCRITURA)
# ===========================================================================
print("\n" + "=" * 60)
print("2. MODO 'w' - ESCRITURA")
print("=" * 60)
print("• Crea archivo nuevo si no existe")
print("• Sobrescribe contenido si ya existe")
print("• Puntero al inicio del archivo")

with open('ejemplo.txt', 'w') as archivo:
    archivo.write("Contenido NUEVO - se borró lo anterior\n")
    archivo.write("Segunda línea del nuevo contenido\n")

with open('ejemplo.txt', 'r') as archivo:
    print(f" Nuevo contenido:\n{archivo.read()}")

# ===========================================================================
# 3. MODO 'a' (ANEXAR)
# ===========================================================================
print("\n" + "=" * 60)
print("3. MODO 'a' - ANEXAR")
print("=" * 60)
print("• Crea archivo si no existe")
print("• Añade contenido al FINAL (no sobrescribe)")
print("• Puntero al final del archivo")

with open('ejemplo.txt', 'a') as archivo:
    archivo.write("Línea 3: Añadida con modo 'a'\n")
    archivo.write("Línea 4: Más contenido anexado\n")

with open('ejemplo.txt', 'r') as archivo:
    print(f" Contenido tras anexar:\n{archivo.read()}")

# ===========================================================================
# 4. MODO 'x' (CREACIÓN EXCLUSIVA)
# ===========================================================================
print("\n" + "=" * 60)
print("4. MODO 'x' - CREACIÓN EXCLUSIVA")
print("=" * 60)
print("• Crea NUEVO archivo")
print("• FALLA si el archivo ya existe")
print("• Útil para evitar sobrescribir archivos existentes")

try:
    with open('exclusivo.txt', 'x') as archivo:
        archivo.write("Archivo creado con modo 'x'\n")
        print(" Archivo 'exclusivo.txt' creado exitosamente")
except FileExistsError:
    print(" Error: El archivo ya existe (esto es esperado)")

# Crear uno que no existe
with open('nuevo.txt', 'x') as archivo:
    archivo.write("Archivo creado exitosamente con 'x'\n")
    print(" Archivo 'nuevo.txt' creado con modo 'x'")

# ===========================================================================
# 5. MODO 'b' (BINARIO) - COMBINADO CON OTROS MODOS
# ===========================================================================
print("\n" + "=" * 60)
print("5. MODO 'b' - BINARIO")
print("=" * 60)
print("• Se combina con otros modos: 'rb', 'wb', 'ab', 'xb', 'r+b', 'w+b', 'a+b'")
print("• Lee/escribe bytes en lugar de strings")
print("• Necesario para archivos no-texto (imágenes, PDF, etc.)")

# Escritura binaria
datos_binarios = bytes([65, 66, 67, 68, 69])  # ABCDE en ASCII
with open('binario.bin', 'wb') as archivo:
    archivo.write(datos_binarios)
    print(" Escritos 5 bytes en 'binario.bin'")

# Lectura binaria
with open('binario.bin', 'rb') as archivo:
    contenido = archivo.read()
    print(f" Bytes leídos: {list(contenido)}")
    print(f" Como texto: {contenido.decode('ascii')}")

# ===========================================================================
# 6. MODO 't' (TEXTO) - PREDETERMINADO
# ===========================================================================
print("\n" + "=" * 60)
print("6. MODO 't' - TEXTO (predeterminado)")
print("=" * 60)
print("• Modo predeterminado si no se especifica 'b'")
print("• Se combina: 'rt', 'wt', 'at', 'xt' (normalmente omitimos la 't')")
print("• Trabaja con strings, maneja encoding automáticamente")

with open('texto.txt', 'wt', encoding='utf-8') as archivo:  # 'wt' = 'w'
    archivo.write("Texto con encoding UTF-8\n")
    archivo.write("Caracteres especiales: á é í ó ú ñ\n")

with open('texto.txt', 'rt', encoding='utf-8') as archivo:  # 'rt' = 'r'
    print(f" Contenido con encoding UTF-8:\n{archivo.read()}")

# ===========================================================================
# 7. MODOS CON '+' (ACTUALIZACIÓN/LECTURA+ESCRITURA)
# ===========================================================================
print("\n" + "=" * 60)
print("7. MODOS CON '+' - LECTURA Y ESCRITURA")
print("=" * 60)

# MODO 'r+' (Lectura y escritura)
print("\n• MODO 'r+':")
print("  - Archivo debe existir")
print("  - Puntero al inicio")
print("  - Sobrescribe desde la posición actual")

with open('ejemplo.txt', 'r+') as archivo:
    contenido = archivo.read()
    print(f"  Contenido actual:\n{contenido}")
    archivo.seek(0)  # Volver al inicio
    archivo.write("SOBREESCRITO con r+\n")  # Sobrescribe desde el inicio

with open('ejemplo.txt', 'r') as archivo:
    print(f"   Tras 'r+':\n{archivo.read()}")

# MODO 'w+' (Lectura y escritura, crea/sobrescribe)
print("\n• MODO 'w+':")
print("  - Crea o sobrescribe archivo")
print("  - Puntero al inicio")

with open('ejemplo.txt', 'w+') as archivo:
    archivo.write("Nuevo contenido con w+\n")
    archivo.seek(0)  # Ir al inicio para leer
    print(f"   Escrito y leído:\n{archivo.read()}")

# MODO 'a+' (Lectura y escritura, anexa)
print("\n• MODO 'a+':")
print("  - Crea o abre para anexar")
print("  - Puntero al FINAL para escritura")
print("  - Se puede mover puntero para lectura")

with open('ejemplo.txt', 'a+') as archivo:
    # Escritura (siempre al final)
    archivo.write("Añadido con a+\n")
    # Moverse para leer
    archivo.seek(0)
    print(f"   Contenido completo:\n{archivo.read()}")

# ===========================================================================
# RESUMEN TABULAR
# ===========================================================================
print("\n" + "=" * 60)
print("RESUMEN DE MODOS - TABLA COMPARATIVA")
print("=" * 60)

resumen = """
MODO  | EXISTE? | SOBRESCRIBE? | PUNTERO  | LECTURA | ESCRITURA
------|---------|--------------|----------|---------|----------
r / rt| Sí      | No           | Inicio   | Sí      | No
rb    | Sí      | No           | Inicio   | Binario | No
w / wt| Crea    | Sí           | Inicio   | No      | Sí
wb    | Crea    | Sí           | Inicio   | No      | Binario
a / at| Crea    | No (añade)   | Final    | No      | Sí
ab    | Crea    | No (añade)   | Final    | No      | Binario
x / xt| No      | -            | Inicio   | No      | Sí
xb    | No      | -            | Inicio   | No      | Binario
r+    | Sí      | Parcial*     | Inicio   | Sí      | Sí
w+    | Crea    | Sí           | Inicio   | Sí      | Sí
a+    | Crea    | No (añade)   | Final**  | Sí      | Sí
* r+: sobrescribe desde posición actual, no trunca archivo
** a+: escritura al final, lectura desde cualquier posición (con seek())
"""

print(resumen)

# ===========================================================================
# EJEMPLO PRÁCTICO COMPLETO
# ===========================================================================
print("\n" + "=" * 60)
print("EJEMPLO PRÁCTICO: REGISTRO DE LOGS")
print("=" * 60)

# Simulación de sistema de logs
nombre_log = 'app.log'

# Primera ejecución: crear log
with open(nombre_log, 'a') as log:
    log.write("[INFO] Aplicación iniciada\n")
    log.write("[INFO] Cargando configuración\n")

# Segunda ejecución: añadir más logs (sin borrar anteriores)
with open(nombre_log, 'a') as log:
    log.write("[WARN] Configuración no encontrada, usando valores por defecto\n")
    log.write("[INFO] Servicio iniciado correctamente\n")

# Leer log completo
print("📝 Contenido del archivo de log:")
with open(nombre_log, 'r') as log:
    for i, linea in enumerate(log, 1):
        print(f"  Línea {i}: {linea.strip()}")

# ===========================================================================
# BUENAS PRÁCTICAS Y RECOMENDACIONES
# ===========================================================================
print("\n" + "=" * 60)
print("BUENAS PRÁCTICAS")
print("=" * 60)

print("""
1. USAR 'with' SIEMPRE:
   • Cierra archivos automáticamente
   • Maneja excepciones correctamente

2. ESPECIFICAR ENCODING:
   • Usar encoding='utf-8' para archivos de texto
   • Evita problemas con caracteres especiales

3. ELEGIR MODO CORRECTO:
   • Solo lectura: 'r'
   • Reemplazar contenido: 'w'
   • Añadir al final: 'a'
   • Evitar sobrescribir: 'x'

4. PARA ARCHIVOS GRANDES:
   • Leer por líneas (for linea in archivo:)
   • No usar .read() en archivos muy grandes

5. MANEJO DE ERRORES:
   • Usar try-except para FileNotFoundError
   • Verificar permisos de escritura/lectura
""")

# Limpiar archivos de ejemplo creados
print("\n" + "=" * 60)
print("LIMPIEZA DE ARCHIVOS DE EJEMPLO")
print("=" * 60)
limpiar_archivos_ejemplo()
print("\nDemostración completada. Todos los archivos temporales eliminados.")