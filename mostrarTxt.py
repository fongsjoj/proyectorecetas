from pathlib import Path
import  os
from funciones import *
def mostrar_categorias():
    ruta = Path(Path.home(), 'recetas')
    ##########################
    #  USO DE SCANDIR PARA BUSCAR LOS DIRECTORIOS EN LA RUTA
    ##########################
    with os.scandir(ruta) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
    print(subdirectorios)
    print('ESTOY AQUI')
    archivosTxt = []
    #################################
    # RUTINA PARA DETECTAR QUE UNA CARPETA VIENE VACIA SIN TXT
    #################################
    for subdir in subdirectorios:
        ruta = Path(Path.home(), 'recetas',subdir)
        archivosTxt  = Path(ruta).glob("**/*.txt")
        archivosTxt = list(archivosTxt)
        if len(archivosTxt) == 0:
           print('No hay archivos txt')
           print(subdir)
           return subdir

    return

#categ = 'carnes'
#mostrar_categorias()
categ = mostrar_categorias()
ruta=Path(Path.home(),'recetas',categ)
os.chdir(ruta)
print(f"Categoria:  {categ} ")
print('Recetas de la categoria')
print('-----------------------')
#Bucle para  mostrar las recetas de la categoria
lista_recetas= []
for txt in Path(ruta).glob("*.txt"):
    #print(os.path.basename(txt))
    lista_recetas.append(txt.stem)
    #a=txt.stem
    #print(a)

wait()
limpiar_pantalla()
#Fin bucle para mostrar las recetas de las recetas sin .txt
print(f'Lista de recetas de la categoria: {categ}')
for contador, rec in enumerate(lista_recetas, start=1):
    print(contador, rec)
num_rec = input("Ingrese el numero de la receta a consultar")
for contador, rec in enumerate(lista_recetas, start=1):
    if contador == int(num_rec):
        nom_receta = rec

#resp = 's'
#while resp == 's' or resp == 'S':
#    nom_receta = input("ingrese el numero de la receta a mostrar: ")
#    if not Path(Path.home(),'recetas',categ,nombre_receta+'.txt').exists():
#        print('Nombre de receta no existe')
#    else:
        #print(Path(Path.home(),'recetas',categ,nombre_receta+'.txt'))
        #carpeta = Path('C:/Users/usuario/Desktop\otro/') / 'prueba.txt'
#Aqui se imprime el contenido de la receta
        limpiar_pantalla()
        archivotxt = open(nom_receta+'.txt')
        print(nom_receta.title())
        linea()
        print(archivotxt.read())
        wait()
        #break
    #resp = input("Desea continuar (s/n)?: ")




