class Tareas:  # Nombre de clase con mayúscula inicial (convención PascalCase)
    
    def __init__(self):
        """
        Constructor: Inicializa la lista vacía de tareas.
        Se ejecuta automáticamente al crear una nueva instancia.
        """
        self.tareas = []  # Atributo de instancia para almacenar todas las tareas
    
    def agregar_tarea(self):
        """
        Solicita al usuario una tarea y la agrega a la lista.
        Cada tarea se almacena como un diccionario con dos claves:
        - "descripcion": texto de la tarea
        - "completada": estado booleano (False por defecto)
        """
        descripcion = input("Ingrese una tarea: ")
        # Crear diccionario con la estructura correcta
        nueva_tarea = {
            "descripcion": descripcion,
            "completada": False  # Por defecto, no está completada
        }
        self.tareas.append(nueva_tarea)  # Agregar a la lista
        print(f"Tarea '{descripcion}' agregada correctamente.")
    
    def marcar_completada(self, indice_tarea):
        """
        Cambia el estado de una tarea a completada.
        
        Parámetros:
        - indice_tarea: posición de la tarea en la lista (0-based)
        """
        if 0 <= indice_tarea < len(self.tareas):
            self.tareas[indice_tarea]["completada"] = True
            descripcion = self.tareas[indice_tarea]["descripcion"]
            print(f"Tarea '{descripcion}' marcada como completada.")
        else:
            print("Error: Índice de tarea no válido.")
        
    def mostrar_tareas(self):
        """
        Muestra todas las tareas numeradas con su estado.
        Usa enumerate para obtener índice y elemento simultáneamente.
        """
        if not self.tareas:  # Si la lista está vacía
            print("No hay tareas registradas.")
            return
            
        print("\n--- LISTA DE TAREAS ---")
        for indice, tarea in enumerate(self.tareas):
            # Operador ternario para determinar el estado
            estado = "✓ Completada" if tarea["completada"] else "✗ Pendiente"
            print(f"{indice}. {tarea['descripcion']} - {estado}")

# Ejemplo de uso CORRECTO
if __name__ == "__main__":
    # Crear instancia de la clase
    lista_tareas = Tareas()  # Correcto: Tareas() no tareas() o lista_tareas()
    
    # Agregar algunas tareas
    lista_tareas.agregar_tarea()
    lista_tareas.agregar_tarea()
    
    # Mostrar todas las tareas
    lista_tareas.mostrar_tareas()
    
    # Marcar la primera tarea (índice 0) como completada
    lista_tareas.marcar_completada(0)
    
    # Mostrar tareas actualizadas
    lista_tareas.mostrar_tareas()