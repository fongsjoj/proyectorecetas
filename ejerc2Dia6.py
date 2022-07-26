#Crea una funcion llamada sobreescribir() que abra (open) un archivo indicado como
#parametro y sobreescriba cualquier contenido anterior por el texto
# 'contenido eliminado'

def sobreescribir(archivo):
    archivo = open(archivo,'w')
    archivo.write("contenido eliminado")
    archivo.close()
    return
sobreescribir("nuevo.txt")

