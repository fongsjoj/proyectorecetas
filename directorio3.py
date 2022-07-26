#Despues de import se puede pulsar 'ctrl+espacio' y aparecen otros metodos
#PureWindowsPath transforma cualquier ruta que se tenga en una ruta de windows. Se
#reproduce (autocompleta) el metodo siempre que se comience a escribir en mayuscula
#Es un metodo que esta incluido en los metodos de Path. Debe incluirse junto al import de
#Path

from pathlib import Path, PureWindowsPath
carpeta = Path('C:/Users/usuario/Desktop/otro/prueba.txt')
ruta_windows = PureWindowsPath(carpeta)
#Imprime con el formato de Windows-->  C:\Users\usuario\Desktop\otro\prueba.txt
print(ruta_windows)