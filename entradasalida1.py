#Manipulacion de archivos secuenciales o texto
mi_archivo = open('prueba.txt')

#mi_archivo.read()
#print(mi_archivo.readline())

una_lnea = mi_archivo.readline()
#como lo que se almacena en la variable una_linea es un string se pueden aplicar todos los
#metodos que se aplican a los string como upper
print(una_lnea.upper())

una_lnea = mi_archivo.readline()
#para que no haga un salto de linea al imprimir una linea (registro) del archivo
print(una_lnea.rstrip())

una_lnea = mi_archivo.readline()
print(una_lnea)




mi_archivo.close()

