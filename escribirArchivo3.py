#Uso de writelines([elemnto1,elemento2...]) para grabar una lista
# Si se hace un writelines(lista) directamente se graba cada elemento uno
#seguido del otro sin saltos de linea. No es muy usado??
#Una forma mas optima de hacer una grabacion de una lista con saltos de linea, con un FOR

archivo = open('prueba1.txt', 'w')

lista = ['primer nuevo registro','segundo registro','tercer registro']

for p in lista:
    archivo.writelines(p + '\n')

archivo.close()

