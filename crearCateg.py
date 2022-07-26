from pathlib import Path
import  os
import  funciones



def mostrar_cat(categorias):
    funciones.limpiar_pantalla()
    print('Categorias Disponibles')
    for contador, cat in enumerate(categorias, start=1):
        print(contador, cat)
    return

ruta=Path(Path.home(),'recetas')
os.chdir(ruta)
lista = []
lista = funciones.buscar_categorias()
mostrar_cat(lista)
resp = 's'

while resp == 's' or resp == 'S':
    nombre_categoria = input("ingrese el nombre de la categoria a crear: ")
    if  Path(Path.home(),'recetas',nombre_categoria).exists():
        print('Nombre de categoria Ya existe')
    else:
        os.makedirs(Path(Path.home(),'recetas',nombre_categoria))
        file_recetas = open(r'C:\Users\usuario\Documents\recetas.txt', 'a')
        file_recetas.write(nombre_categoria)
        print('Ejecutado')
        break
    resp = input("Desea continuar (s/n)?: ")