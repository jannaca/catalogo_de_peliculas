from pathlib import Path
import shutil  # Modulo para mover archivo

#Variables
current_path = Path.cwd()
catalogo = current_path / "Peliculas"
carpeta_reciclaje = current_path/"Papelera de reciclaje"

# MENU
def menu():
    print("\n------------------------")
    print("Menú: ")
    print("1. Entrar a catálogo")
    print("2. Leer Resumen")
    print("3. Eliminar Resumen")
    print("4. Papelera de recilaje")
    print("5. Restaurar de la Papelera recilaje")
    print("6. Eliminar de Papelera recilaje")
    print("7. Salir:")
    print("------------------------\n")

# Listar archvios
def listar_peliculas(carpeta):
    peliculas = []
    for pelicula in carpeta.iterdir():
        if pelicula.suffix == ".txt":
            peliculas.append(pelicula.stem)
    return peliculas

# Enumerar peliculas
def enumerar_peliculas(carpeta, texto):
    print("-------------------------")
    print(f"{texto}\n")
    for i, pelicula in enumerate(carpeta, start=1):
        print(f"{i}. {pelicula}")
    print("-------------------------")

# Leer archivos
def leer_peliculas(pelicula):
    with open(catalogo / f"{pelicula}.txt", "r") as file:
        print(file.read())

# Mover archivos a papelera
def mover_papelera(pelicula):
    shutil.move(catalogo/f"{pelicula}.txt", carpeta_reciclaje)
    print(f"\nLa película '{pelicula}' fue movida a la papelera de reciclaje")

# Restaurar archivo de la papelera
def restaurar_papelera(pelicula):
    shutil.move(carpeta_reciclaje/f"{pelicula}.txt", catalogo)
    print(f"\nLa película '{pelicula}' fue restaurada exitosamente")

# Eliminar archivos
def eliminar_peliculas(pelicula):
    path_pelicula = carpeta_reciclaje/f"{pelicula}.txt"
    path_pelicula.unlink()
    print(f"\nLa Película '{pelicula}' fue eliminada")

# Validar si la pelicula existe
def validar_pelicula(numero, carpeta, funcion):
    numero_pelicula = numero-1
    if numero_pelicula < len(carpeta) and numero_pelicula >= 0:
        funcion(carpeta[numero_pelicula])
    else:
        print("\nPelícula no encontrada")

# Bucle para el menu
while True:
    menu()

    opcion = int(input("Seleccione una opción: "))
    print()

    #Listas donde se encuentran la peliculas de cada carpeta
    peliculas_catalogo = listar_peliculas(catalogo)
    peliculas_reciclaje = listar_peliculas(carpeta_reciclaje)

    # Salir de programa
    if opcion == 7:
        print("Programa finalizado.")
        break

    # Mostrar peliculas en catalogo
    if opcion == 1:
        enumerar_peliculas(peliculas_catalogo, "Peliculas disponibles")

    # Leer Resumen de pelicula
    if opcion == 2:
        numero = int(input("Ingrese el numero de la película que desea leer: "))
        validar_pelicula(numero, peliculas_catalogo, leer_peliculas)

    # Mover pelicula a papelera de reciclaje
    if opcion == 3:
        numero = int(
            input("Ingrese el numero de la película que desea eliminar: "))
        validar_pelicula(numero, peliculas_catalogo, mover_papelera)

    # Ver peliculas que se encuentran en papelera
    if opcion == 4:
        enumerar_peliculas(peliculas_reciclaje, "Papelera de reciclaje")

    # Restaurar pelicula a catalogo
    if opcion == 5:
        numero = int(
            input("Ingrese el numero de la película que desea restaurar de la Papelera: "))
        validar_pelicula(numero, peliculas_reciclaje, restaurar_papelera)

    # Eliminar pelicula de papelera de Reciclaje
    if opcion == 6:
        numero = int(
            input("Ingrese el numero de la película que desea eliminar permanentemente de la Papelera: "))
        validar_pelicula(numero, peliculas_reciclaje, eliminar_peliculas)
