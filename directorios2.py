#Uso de pathlib y objetos de Path
from pathlib import Path

carpeta = Path('C:/Users/usuario/Desktop/otro/prueba.txt')
#Ahora carpeta es un objeto de Path y presenta una serie de metodos distintos
#Usando esta instruccion no hace falta abrir el archivo (instruccion open)
#print(carpeta.read_text())

#Extrae el nombre del archivo con name
#print(carpeta.name)

#Con la funcion suffix se extrae la extension del archivo
#print(carpeta.suffix)

#Con stem se e extrae el nombre del archivo sin la extension
#print(carpeta.stem)

#Metodo que permite consultar si un archivo existe o no
if not  carpeta.exists():
    print('Archivo no existe')
else:
    print('El archivo existe')

