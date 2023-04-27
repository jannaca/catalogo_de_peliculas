from pathlib import Path

current_path = Path.cwd()
catalogo = current_path / "Peliculas"

# MENU


def menu():
    print("\n------------------------")
    print("Menú: ")
    print("1. Entrar a catálogo")
    print("2. Leer Resumen")
    print("3. Eliminar Resumen")
    print("4. Salir:")
    print("------------------------\n")

# Listar archvios


def listar_peliculas():
    peliculas = []
    for pelicula in catalogo.iterdir():
        if pelicula.suffix == ".txt":
            peliculas.append(pelicula.stem)
    return peliculas

# Leer archivos


def leer_peliculas(pelicula):
    with open(catalogo / f"{pelicula}.txt", "r") as file:
        print(file.read())

# Eliminar archivos


def eliminar_peliculas(pelicula):
    path_pelicula = catalogo/f"{pelicula}.txt"
    path_pelicula.unlink()


def validar_pelicula(numero,funcion): 
    numero_pelicula = numero-1
    if numero_pelicula < len(peliculas) and numero_pelicula >= 0:
        funcion(peliculas[numero_pelicula])
    else:
        print("\nPelícula no encontrada")



# Bucle para el menu
while True:
    menu()

    opcion = int(input("Seleccione una opción: "))
    print()

    peliculas = listar_peliculas()

    if opcion == 4:
        print("Programa finalizado.")
        break

    if opcion == 1:

        print("-------------------------")

        print("Películas disponibles:\n")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")

        print("-------------------------")

    if opcion == 2:
        numero = int(input("Ingrese el numero de la película: "))
        validar_pelicula(numero,leer_peliculas)

    if opcion == 3:
        numero = int(
            input("Ingrese el numero de la película que desea eliminar: "))
        validar_pelicula(numero,eliminar_peliculas)
        print("\nPelícula eliminada")