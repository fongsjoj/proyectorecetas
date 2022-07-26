#El metodo Path puede convertir parametros en forma de direcciones en el disco

from    pathlib import Path

#guia = Path("Barcelona","España")
#produce una salida como Barcelona\España)
#Si se coloca  guia = Path("Barcelona","España.txt") convierta la variable guia en una direccion
#PARCIAL de un archivo txt, o sea, Barcelona\España.txt

#Otro metodo llamado home() devuelve la direccion donde se esta trabajando en el  disco

base = Path.home()
#El metodo Path puede admitir tanto cadenas como constructores de Path para crear una
#Direccion en el disco, por ejemplo
#guia = Path(base, "Barcelona","España.txt" )
print(base)

#Adicionalmente se puede usar Path dentro de Path para conformar una ruta

guia = Path(base, "Europa", "Spain", Path("Barcelona","España.txt"))

#Se puede crear un acceso a otro archivo dentro de la misma direccion creada usando el
#metodo  with_name a partir de guia
guia2 = guia.with_name("guijon.txt")
print(guia)
print(guia2)

#Una propiedad de objetos Path es Parent que devuelve el antecesor mas inmediato de una
#ruta de archivos determinada

print(guia.parents[0])
#Se puede acceder al que antecede con otro .parent y otro .parent
print(guia.parent.parent)

#Path sirve tambien para enumerar archivos en un arbol de carpetas