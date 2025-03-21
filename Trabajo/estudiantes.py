from operator import attrgetter

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad} años)"

class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad):
        self.estudiantes.append(Estudiante(nombre, edad))
        print(f"Estudiante {nombre} agregado exitosamente.")

    def buscar_estudiante(self, nombre):
        resultados = [e for e in self.estudiantes if e.nombre.lower() == nombre.lower()]
        if resultados:
            print("Estudiantes encontrados:")
            for e in resultados:
                print(e)
        else:
            print("No se encontró ningún estudiante con ese nombre.")

    def ordenar_y_mostrar(self, criterio, ascendente=True):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        
        # Ordenar sin modificar la lista original
        if criterio == "nombre":
            estudiantes_ordenados = sorted(self.estudiantes, key=attrgetter("nombre"), reverse=not ascendente)
        else:  # criterio == "edad"
            estudiantes_ordenados = sorted(self.estudiantes, key=attrgetter("edad"), reverse=not ascendente)

        orden = "ascendente" if ascendente else "descendente"
        print(f"Lista ordenada por {criterio} ({orden}):")
        for e in estudiantes_ordenados:
            print(e)

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for e in self.estudiantes:
                print(e)

def menu_ordenar(sistema):
    while True:
        print("\nOpciones de ordenamiento:")
        print("1. Ordenar por nombre (A-Z)")
        print("2. Ordenar por nombre (Z-A)")
        print("3. Ordenar por edad (menor a mayor)")
        print("4. Ordenar por edad (mayor a menor)")
        print("5. Volver al menú principal")

        opcion_ordenar = input("Seleccione una opción: ")

        match opcion_ordenar:
            case "1":
                sistema.ordenar_y_mostrar("nombre", ascendente=True)
            case "2":
                sistema.ordenar_y_mostrar("nombre", ascendente=False)
            case "3":
                sistema.ordenar_y_mostrar("edad", ascendente=True)
            case "4":
                sistema.ordenar_y_mostrar("edad", ascendente=False)
            case "5":
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

# Ejemplo de uso
sistema = SistemaEstudiantes()

while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Ordenar estudiantes")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            sistema.agregar_estudiante(nombre, edad)
        
        case "2":
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            sistema.buscar_estudiante(nombre)
        
        case "3":
            menu_ordenar(sistema)  # Llama al submenú de ordenación
        
        case "4":
            sistema.mostrar_estudiantes()
        
        case "5":
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción no válida. Intente de nuevo.")
