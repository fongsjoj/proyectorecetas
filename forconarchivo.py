mi_archivo = open('prueba.txt')

#for l in mi_archivo:
#    print("Aqui dice: " + l)

todas = mi_archivo.readlines()
#Readlines convierte una variable en una lista
#En este caso todas es una lista y se puede aplicar todps los metodos sobre las listas

print(todas)
ultima = todas.pop()
print(ultima)
#Elimina la ultima y se muestras los 2 primeros registros o lineas o filas
print(todas)

mi_archivo.close()