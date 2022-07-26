#ELIMINAR RECETA.TXT
from pathlib import Path
import  os
from funciones import *
from shutil import  rmtree

def buscar_cat():
    limpiar_pantalla()
    #print("Leer Receta")
    categorias = buscar_categorias()
    limpiar_pantalla()
    print('Categorias Disponibles')
    for contador, cat in enumerate(categorias, start=1):
        print(contador, cat)
    num_categ = input("Ingrese el numero de la categoria: ")
    for contador, cat in enumerate(categorias, start=1):
        if contador == int(num_categ):
            nom_categ = cat
    return nom_categ

def mostrarTxt(categ):
    ruta = Path(Path.home(), 'recetas', categ)
    os.chdir(ruta)
    archivosTxt = Path(ruta).glob("*.txt")
    archivosTxt = list(archivosTxt)
    nom_receta = ''
    if len(archivosTxt) == 0:
        print('No hay recetas en la categoria')
    else:
        print(f"Categoria:  {categ} ")
        lista_recetas = []
        for txt in Path(ruta).glob("*.txt"):
            lista_recetas.append(txt.stem)
        wait()
        limpiar_pantalla()
        # Fin bucle para mostrar las recetas de las recetas sin .txt
        print(f'Lista de recetas de la categoria: {categ}')
        for contador, rec in enumerate(lista_recetas, start=1):
            print(contador, rec)
        num_rec = input("Ingrese el numero de la receta a eliminar: ")
        for contador, rec in enumerate(lista_recetas, start=1):
            if contador == int(num_rec):
                nom_receta = rec
    return nom_receta
categ = buscar_cat()
nombre_receta = mostrarTxt(categ)

print(f"Categoria:  {categ} ")
print((f'Nombre de la Receta: {nombre_receta}'))
if nombre_receta != '':
    resp = 's'
    resp = input('Esta seguro que quiere eliminar la receta (s/n)?')
    if resp == 's' or resp == 'S':
        ruta = Path(Path.home(), 'recetas', categ, nombre_receta + '.txt')
        #os.chdir(ruta)
        os.remove(nombre_receta+'.txt')
        #remove(nombre_receta+'.txt')
        print('Procesado')
    else:
        print('No hay recetas para eliminar')
wait()