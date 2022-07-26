from pathlib import Path
import  os
import  funciones
cat = 'carnes'
file_recetas = open(r'C:\Users\usuario\Documents\recetas.txt','r')
ruta = Path(Path.home(),'recetas',cat)
archivosTxt = []
archivosTxt = Path(ruta).glob("*.txt")
archivosTxt = list(archivosTxt)
if len(archivosTxt) == 0:
    print('No hay archivos txt')
else:
    print(archivosTxt )

