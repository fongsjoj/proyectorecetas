###########################################################
#Ejemplo de como usar llibrerias disponibles.
#Uso de la libreria de pathlib, os, msvcrt
#Lo siguiente es un hipotetico caso de tener que controlar el menu de un restaurant
#donde se puede leer y crear  recetas por categorias
#
#jose jimenez/ 2022
##########################################################
#Para que funcione debe crear carpetas con la siguiente estructura en donde se
# guardaran las recetas
#C:\Users\usuario\Recetas\Carnes
#...................................Ensaladas
# ..................................etc
#En cada subcarpeta se debe crear las recetas en archivos txt
##########################################################
from os import system
from pathlib import Path
import msvcrt as m
from funciones import *
#crear_archivo()
limpiar_pantalla()
saludo()
linea()
ubicacion()
linea()
nrorecetas()
linea()
wait()
limpiar_pantalla()
menu()
opcion = 0
while opcion != 6:
    opcion = pedir_opcion()
    if opcion == 1:
        leer_receta()
    if opcion == 2:
        crear_receta()
    if opcion == 3:
        crear_categoría()
    if opcion == 4:
        eliminar_receta()
    if opcion == 5:
        eliminar_categoría()
    limpiar_pantalla()
    menu()
despedida()






