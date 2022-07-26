import  os

#Con la instruccion os.getcwd() se obtiene la ruta del directorio actual donde se esta
#apuntando en python
#ruta =  os.getcwd()

#La forma aprendida para seleccionar un archivo desde un directorio usando el comando
# r'directorio'  o en crudo
#ruta = r'C:\Users\usuario\Desktop\otro'

#Para abrir un archivo directamente con el comando 'r'
#archivo = open(r'C:\Users\usuario\Desktop\otro\prueba.txt')

#Cuando se trabaja con windows se debe colocar doble barra invertida para que tome
#la ruta o cambio de directorio de trabajo
#ruta = os.chdir('c:\\users\\usuario\\desktop\\otro')
#archivo = open(prueba.txt')
#print(archivo.read())

#Para cambiar de directorio usando os.chdir
#ruta = os.chdir('c:\\users\\usuario\\desktop\\otro')

#para crear una carpeta desde python usado libreria OS se usa el comando
#ruta = os.makedirs('c:\\users\\usuario\\desktop\\otro\\nuevacarpeta')

#Si se quiere asignar a una variable el nombre de  un archivo en una carpeta en particular
# se usa la expresion sig. y se convierte en el nombre de base de nuestro elemento
#ruta = 'c:\\users\\usuario\\desktop\\otro\\prueba.txt'
#elemento = os.path.basename(ruta)
#print(elemento)

#Si se quire asignar a una variable la direccion de una ruta donde esta un archivo
# se usa la expresion
#ruta = 'c:\\users\\usuario\\desktop\\otro\\prueba.txt'
#elemento = os.path.dirname(ruta)
#print(elemento)

#Si se quiere asignar a una tupla la direccion y el archivo, en ese orden se usa la expresion
#Quedando ('c:\\users\\usuario\\desktop\\otro', 'prueba.txt')
#ruta = 'c:\\users\\usuario\\desktop\\otro\\prueba.txt'
#elemento = os.path.split(ruta)
#print(elemento)

#Si se quiere eliminar un directorio
#os.rmdir( 'c:\\users\\usuario\\desktop\\otro\\nuevacarpeta')

#Abriendo archivo y viendo el contenido
#otro_archivo = open('c:\\users\\usuario\\desktop\\otro\\prueba.txt')
otro_archivo = open(r'c:\users\usuario\desktop\otro\prueba.txt')
print(otro_archivo.read())


