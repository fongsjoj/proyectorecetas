#Para limpiar la pantalla se tiene que importar el metodo system desde OS
#Luego se tiene que colocar la palabra system('cls')
#En el menu se selecciona RUN y luego DEBUG luego EDIT CONFIGURATION luego en
#EJECUCION ---> EMULATE TERMINAL IN OUTPUT CONSOLE

from os import system

nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad:  ")

system('cls')

print(f'Su nombre es {nombre} y su edad es {edad} años')