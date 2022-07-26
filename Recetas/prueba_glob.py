from pathlib import Path
import  os
x='carnes'
receta = 'Entrecot al Malbec'+'.txt'
name=[]
otro=[]
palabra = ''
ruta=Path(Path.home(),'recetas',x)
ruta_receta=Path(Path.home(),'recetas',x,receta)
if ruta_receta.exists():
    print("RECETA EXISTEEEEEE.........")
if ruta.exists():
    print("RUTA EXISTE....")
actual = os.chdir(ruta)
for txt in Path(ruta).glob("*.txt"):
    #print(txt)
    name.append(os.path.basename(txt))
print(name)
ruta1 = Path(name[0])
print(ruta1.name)
archivo = open(ruta1.name)
print(archivo.read())

#for i in range(len(name)):
#   for j in range(len(name[i])):
#        if name[i][j] != '.':
#            palabra += name[i][j]
#        else:
#            otro.append(palabra)
#            palabra =''
#            break
#print(otro)
