#Path sirve tambien para enumerar archivos en un arbol de carpetas


from pathlib import Path

#Para los efectos se debe colocar desktop en lugar de escritorio
#guia = Path(Path.home(),'desktop','curso2py','proyecto','pythonproject','secc6dia6')
guia = Path(Path.home(),'desktop','curso2py','proyecto')

#print(guia)

#Con la instruccion glob se puede mostrar todos los archivos de cierto tipo que se encuentren

#Donde la busqueda puede ser dentro de una carpeta en particular donde se quiere
#buscar los archivos de cierto tipo, por ejemplo, todos los TXT o PDF
# y guia = Path(Path.home(),'desktop'), por ejemplo. Busca en la carpeta desktop

#for txt in Path(guia).glob("*.txt"):
#    print(txt)

#En caso de que se quiera que se muestren todos los archivos en los diferentes directorios
#se usa la instruccion glob("**/*.txt") desde una carpeta anterior o cercana de lo que interesa
cuenta=0
for txt in Path(guia).glob("**/*.txt"):
    cuenta +=1
    print(txt)
    print(cuenta)

