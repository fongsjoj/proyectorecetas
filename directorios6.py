#Si se quiere mostrar rutas para llegar a un archivo en particular se puede usar la
#instruccion  relative_to
#Esto muestra los directorios desde donde se quiere llegar a un archivo desde dos
#subcarpetas
#Se deben colocar dos lineas con relative_to la segunda debe tener el nombre de la carpeta
#declarada en la primera y luego se colocan las carpetas desde donde se quiere que se
#muestre la ruta

from pathlib import Path

guia = Path('desktop','curso2py','proyecto','pythonproject','secc6dia6','prueba.txt')
en_desktop = guia.relative_to(Path("desktop"))
en_curso2py = guia.relative_to(Path("desktop","curso2py"))
print(en_desktop)
print(en_curso2py)

#Esto es lo que resulta
#curso2py\proyecto\pythonproject\secc6dia6\prueba.txt
#proyecto\pythonproject\secc6dia6\prueba.txt
