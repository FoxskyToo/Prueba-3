import json

def cargar_libros():
    try:
        with open('biblioteca.json', 'r', encoding='utf-8') as file:
            libros = json.load(file)
    except FileNotFoundError:
        libros = []
    return libros


def guardar_libros(libros):
    with open('biblioteca.json', 'w', encoding='utf-8') as file:
        json.dump(libros, file, indent=5)


def mostrar_menu():
    print('***********************************')
    print('*           MUNDO LIBRO           *')
    print('***********************************')        
    print("1. Mantenedor de Libros")
    print("2. Reportes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    libros = cargar_libros()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            while True:
                print('***********************************')
                print('*      MANTENEDOR DE LIBROS       *')
                print('***********************************')
                print("1. Agregar libro")
                print("2. Editar libro")
                print("3. Eliminar libro")
                print("4. Buscar libro")
                print("5. Volver al menú principal")
                accion = input("Seleccione una acción: ")

                if accion == '1':
                    agregar_libro(libros)
                elif accion == '2':
                    editar_libro(libros)
                elif accion == '3':
                    eliminar_libro(libros)
                elif accion == '4':
                    buscar_libro(libros)
                elif accion == '5':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == '2':
            print("Opción de Reportes aún no implementada.")

        elif opcion == '3':
            guardar_libros(libros)
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_libro(libros):
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Ingrese el título del libro: ")
    autor_id = input("Ingrese el ID del autor: ")
    categoria_id = input("Ingrese el ID de la categoría: ")
    ano_publicacion = input("Ingrese el año de publicación: ")

    nuevo_libro = {
        'LibroID': len(libros) + 1,
        'Titulo': titulo,
        'AutorID': autor_id,
        'CategoriaID': categoria_id,
        'AnoPublicacion': ano_publicacion
    }

    libros.append(nuevo_libro)
    print("Libro agregado correctamente.")

def editar_libro(libros):
    print("\n--- EDITAR LIBRO ---")
    id_libro = input("Ingrese el ID del libro que desea editar: ")

    for libro in libros:
        if str(libro['LibroID']) == id_libro:
            libro['Titulo'] = input(f"Nuevo título ({libro['Titulo']}): ") or libro['Titulo']
            libro['AutorID'] = input(f"Nuevo ID de autor ({libro['AutorID']}): ") or libro['AutorID']
            libro['CategoriaID'] = input(f"Nuevo ID de categoría ({libro['CategoriaID']}): ") or libro['CategoriaID']
            libro['AnoPublicacion'] = input(f"Nuevo año de publicación ({libro['AnoPublicacion']}): ") or libro['AnoPublicacion']
            print("Libro editado correctamente.")
            return

    print(f"No se encontró ningún libro con ID {id_libro}.")

def eliminar_libro(libros):
    print("\n--- ELIMINAR LIBRO ---")
    id_libro = input("Ingrese el ID del libro que desea eliminar: ")

    for libro in libros:
        if str(libro['LibroID']) == id_libro:
            libros.remove(libro)
            print("Libro eliminado correctamente.")
            return

    print(f"No se encontró ningún libro con ID {id_libro}.")

def buscar_libro(libros):
    print("\n--- BUSCAR LIBRO ---")
    id_libro = input("Ingrese el ID del libro que desea buscar: ")

    for libro in libros:
        if str(libro['LibroID']) == id_libro:
            print("Información del libro encontrado:")
            print(f"Título: {libro['Titulo']}")
            print(f"Autor ID: {libro['AutorID']}")
            print(f"Categoría ID: {libro['CategoriaID']}")
            print(f"Año de Publicación: {libro['AnoPublicacion']}")
            return

    print(f"No se encontró ningún libro con ID {id_libro}.")

if __name__ == "__main__":
    main()