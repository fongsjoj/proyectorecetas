#Como crear rutas que sean interpretadas por cualquier OS. Uso del modulo PATH
#Se importa el modulo PATH a un OBJETO Path desde PATHLIB
from pathlib import Path
#Observar la P mayuscula, se debe colocar la P mayuscula sino da error
#carpeta = Path('C:/Users/usuario/Desktop/otro/')
#Se usa '/' para concatenar la expresion
#archivo = carpeta / 'prueba.txt'

#Lo mismo anterior pero en una sola linea
carpeta = Path('C:/Users/usuario/Desktop\otro/') / 'prueba.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())