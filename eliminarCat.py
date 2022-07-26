from pathlib import Path
import  os
import  funciones
from os import rmdir
from shutil import  rmtree

ruta=Path(Path.home(),'recetas')
os.chdir(ruta)
nombre_categoria = funciones.buscar_categorias()
#funciones.mostrar_cat(nombre_categoria)

funciones.limpiar_pantalla()
print('Categoria Disponibles')
for contador, cat in enumerate(nombre_categoria, start=1):
    print(contador, cat)
num_categ = input("Ingrese el numero de la categoria: ")
for contador, cat in enumerate(nombre_categoria, start=1):
    if contador == int(num_categ):
        nom_categ = cat
        print('nombre categoria', nom_categ, cat)
        break
    else:
        nom_categ = ''
print()

if nom_categ == '':
    print('No hay categorias para eliminar', nom_categ)
else:
    resp = 'n'
    resp = input(f'Esta seguro de borrar la categoria {nom_categ} (s/n): ? ')
    if resp ==  's' or resp == 'S':
        rmtree(Path(ruta, nom_categ))
        print('Ejecutado')
    else:
        print('No se realizo la eliminacion')
        funciones.wait()
