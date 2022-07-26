from pathlib import Path
import msvcrt as m
import os
from shutil import  rmtree
def crear_archivo():
    file_recetas = open(r'C:\Users\usuario\Documents\recetas.txt','w')
    ruta = Path(Path.home(), 'recetas')
    for txt in Path(ruta).glob("**/*.txt"):
        aux_carpeta = os.path.dirname(txt)
        n_carpeta = os.path.basename(aux_carpeta)
        nomb_arch = os.path.basename(txt)
        reg = n_carpeta + ',' + nomb_arch+'\n'
        file_recetas.write(reg)
    file_recetas.close()

def saludo():
    print("\t    BIENVENIDO")
    print("\t    ----------")
    print("J  J  -   R O M A' S    /   RESTAURANT")

def ubicacion():
    ruta = Path(Path.home(),'recetas')
    #leer_subcarpetas()
    print(f"Ruta de acceso de las recetas en el disco \n{ruta}")

def nrorecetas():
    ruta = Path(Path.home(), 'recetas')
    cantidad = 0
    for txt in Path(ruta).glob("**/*.txt"):
        #print(txt)
        cantidad +=1
    print(f"Cantidad de recetas:  {cantidad}")

def wait():
    print('\nPulse cualquier tecla para continuar...')
    m.getch()

def limpiar_pantalla():
    os.system('cls')
def linea():
    print("------------------------------------")

def buscar_cat():
    limpiar_pantalla()
    #print("Leer Receta")
    categorias = buscar_categorias()
    limpiar_pantalla()
    print('Categorias Disponibles')
    for contador, cat in enumerate(categorias, start=1):
        print(contador, cat)
    num_categ = input("Ingrese el numero de la categoria (r) para regresar: ")
    if not num_categ.isdigit():
        return 'SALIR'
    for contador, cat in enumerate(categorias, start=1):
        if contador == int(num_categ):
            nom_categ = cat
    return nom_categ

def mostrarTxt(categ,tipo):
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
        num_rec = input(f"Ingrese el numero de la receta a {tipo} (r) para regresar: ")
        if not num_rec.isdigit():
            return 'r'
        for contador, rec in enumerate(lista_recetas, start=1):
            if contador == int(num_rec):
                nom_receta = rec
    return nom_receta

def mostrar_cat(categorias):
    limpiar_pantalla()
    print('Categorias Disponibles')
    for contador, cat in enumerate(categorias, start=1):
        print(contador, cat)
    return

def existe_receta(rut):
    nombre_receta = input("ingrese el nombre de la receta: ")
    rutareceta=Path(nombre_receta+'.txt')
    while rutareceta.exists():
        print("receta ya existe")
        nombre_receta = input("ingrese el nombre de la receta: ")
        rutareceta = Path(nombre_receta + '.txt')
    return nombre_receta

def crear_recetas():
    categ = buscar_cat()
    if categ == 'SALIR'  :
        return
    limpiar_pantalla()
    ruta = Path(Path.home(), 'recetas', categ)
    os.chdir(ruta)
    print(f"Categoria:  {categ} ")
    # Pide el nombre de la receta
    nombre_receta = existe_receta(ruta)
    resp = 'n'
    contenido = []
    # while resp == 'n' or resp == 'N':
    receta = input("Escriba el contenido de la receta: ")
    contenido.append(receta)
    resp = input("Desea continuar escribiendo la receta (s/n)?: ")
    while resp == 's' or resp == 'S':
        receta = input("Escriba el contenido de la receta: ")
        contenido.append(receta)
        resp = input("Desea continuar escribiendo la receta (s/n)?: ")
    conf_grab = input("Desea grabar la receta (s/n)?: ")
    if conf_grab == 's' or conf_grab == 'S':
        file_recetas = open(nombre_receta + '.txt', 'w')
        linea = ''
        for i in contenido:
            linea = i
            file_recetas.write(linea + '\n')
        for i in contenido:
            print(i)

def menu():
    print("MENU DE OPCIONES")
    print("-------------------")
    print('''1.- leer receta
2.- crear receta
3.- crear categoría
4.- eliminar receta
5.- eliminar categoría
6.- finalizar programa
''')

def pedir_opcion():
    opc = 0
    opc = str(opc)
    while (ord(opc) <49) or (ord(opc) > 54):
        opc = input("Escoja una opcion del 1 al 6: ")
    opc1 = int(opc)
    return opc1

def despedida():
    limpiar_pantalla()
    print("\tGRACIAS POR SU VISITA")
    print("J  J  -   R O M A N    /   RESTAURANT")
    print("\tHASTA LUEGO")

def leer_receta():
    limpiar_pantalla()
    print("Leer Receta")
    categorias = buscar_categorias()
    limpiar_pantalla()
    print('Categoria Disponibles')
    for contador, cat in enumerate(categorias, start=1):
        print(contador, cat)
    num_categ = input("Ingrese el numero de la categoria: (r)  para regresar ")
    if not num_categ.isdigit():
        return
    for contador, cat in enumerate(categorias, start=1):
        if contador == int(num_categ):
            nom_categ = cat

# Se llama a la funcion que  muestra los nombres de  las recetas numeradas

    nombre_receta =mostrarTxt(nom_categ,'consultar')
    if nombre_receta =='r':
        return
    if nombre_receta != '':
        resp = 's'
        limpiar_pantalla()
        archivotxt = open(nombre_receta + '.txt')
        print(nombre_receta.title())
        linea()
        print(archivotxt.read())
    wait()
    return
def crear_receta():
    limpiar_pantalla()
    crear_recetas()
    #wait()
    return
def crear_categoría():
    limpiar_pantalla()
    ruta = Path(Path.home(), 'recetas')
    os.chdir(ruta)
    lista = []
    lista = buscar_categorias()
    mostrar_cat(lista)
    resp = 's'

    while resp == 's' or resp == 'S':
        nombre_categoria = input("ingrese el nombre de la categoria a crear (r) para regresar: ")
        if nombre_categoria == '' or nombre_categoria == 'r':
            return
        if Path(Path.home(), 'recetas', nombre_categoria).exists():
            print('Nombre de categoria Ya existe')
        else:
            os.makedirs(Path(Path.home(), 'recetas', nombre_categoria))
            file_recetas = open(r'C:\Users\usuario\Documents\recetas.txt', 'a')
            file_recetas.write(nombre_categoria)
            print('Ejecutado')
            break
        resp = input("Desea continuar (s/n)?: ")
    wait()
    return
def eliminar_receta():
    limpiar_pantalla()

    categ = buscar_cat()
    if categ == 'SALIR'  :
        return
    nombre_receta = mostrarTxt(categ,'eliminar')

    print(f"Categoria:  {categ} ")
    print((f'Nombre de la Receta: {nombre_receta}'))
    if nombre_receta != '':
        resp = 's'
        resp = input('Esta seguro que quiere eliminar la receta (s/n)?')
        if resp == 's' or resp == 'S':
            ruta = Path(Path.home(), 'recetas', categ, nombre_receta + '.txt')
            # os.chdir(ruta)
            os.remove(nombre_receta + '.txt')
            # remove(nombre_receta+'.txt')
            print('Procesado')
        else:
            print('No hay recetas para eliminar')
    wait()
    return
def eliminar_categoría():
    limpiar_pantalla()
    ruta = Path(Path.home(), 'recetas')
    os.chdir(ruta)
    nombre_categoria = buscar_categorias()
    # funciones.mostrar_cat(nombre_categoria)

    limpiar_pantalla()
    print('Categoria Disponibles')
    for contador, cat in enumerate(nombre_categoria, start=1):
        print(contador, cat)
    num_categ = input("Ingrese el numero de la categoria (r) para regresar: ")
    if not num_categ.isdigit():
        return
    for contador, cat in enumerate(nombre_categoria, start=1):
        if contador == int(num_categ):
            nom_categ = cat
            break
        else:
            nom_categ = ''
    print()

    if nom_categ == '':
        print('No hay categorias para eliminar')
    else:
        resp = 'n'
        resp = input(f'Esta seguro de borrar la categoria {nom_categ} (s/n): ? ')
        if resp == 's' or resp == 'S':
            rmtree(Path(ruta, nom_categ))
            print('Ejecutado')
        else:
            print('No se realizo la eliminacion')
    wait()
    return
def leer_subcarpetas():
    ruta = Path(Path.home(),'recetas')
    for txt in Path(ruta).glob("**/*.txt"):
        aux_carpeta = os.path.dirname(txt)
        n_carpeta = os.path.basename(aux_carpeta)
        #print(n_carpeta)
        nomb_arch = os.path.basename(txt)
        #print(nomb_arch)
        reg = n_carpeta+','+nomb_arch
        #print(reg)
    return

def buscar_categorias():
    ruta = Path(Path.home(), 'recetas')
    ##########################
    # Uso de scandir para buscar los directorios en la ruta
    ##########################
    with os.scandir(ruta) as ficheros:
        subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
    categ= list(subdirectorios)
    categ.sort()
    return categ


