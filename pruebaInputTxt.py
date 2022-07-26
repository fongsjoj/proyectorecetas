from pathlib import Path
import  os
def existe_receta(rut):
    nombre_receta = input("ingrese el nombre de la receta: ")
    rutareceta=Path(nombre_receta+'.txt')
    while rutareceta.exists():
        print("receta ya existe")
        nombre_receta = input("ingrese el nombre de la receta: ")
        rutareceta = Path(nombre_receta + '.txt')
    return nombre_receta
def grabar_arch_Rec(carpeta,nombre):
    file_recetas = open(r'C:\Users\usuario\Documents\recetas.txt','a')
    reg = carpeta + ',' + nombre+'\n'
    file_recetas.write(reg)
    file_recetas.close()

categ = 'sandwich'
ruta=Path(Path.home(),'recetas',categ)
os.chdir(ruta)
print(f"Categoria:  {categ} ")
#Pide el nombre de la receta
nombre_receta = existe_receta(ruta)
resp = 'n'
contenido = []
#while resp == 'n' or resp == 'N':
receta=input("Escriba el contenido de la receta: ")
contenido.append(receta)
resp = input("Desea continuar escribiendo la receta (s/n)?: ")
while resp == 's' or resp == 'S':
    receta = input("Escriba el contenido de la receta: ")
    contenido.append(receta)
    resp = input("Desea continuar escribiendo la receta (s/n)?: ")
conf_grab=input("Desea grabar la receta (s/n)?: ")
if conf_grab == 's' or conf_grab == 'S':
    file_recetas = open(nombre_receta+'.txt','w')
    linea= ''
    for i in contenido:
        linea = i
        file_recetas.write(linea+'\n')
    grabar_arch_Rec(categ,nombre_receta+'.txt')
    for i in contenido:
        print(i)
    #break