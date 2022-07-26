#Crear una funcion llamada abrir_leer() que abra  (open) un archivo indicando como
#parametro y devuelva su contenido (read)

def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()

file = r'C:\Users\usuario\Desktop\otro\prueba.txt'
contenido = abrir_leer(file)
print(contenido)