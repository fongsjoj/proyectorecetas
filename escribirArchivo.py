#Modos de abrir un archivo: 'r' (si no se indica, se abre solo lectura por defecto. El archivo
# tiene que existir 'w' sobreescritura si no existe se crea, borra el contenido del archivo,
# si ya existe, y permite escribir en el archivo
# y 'a' (se posiciona el apuntador al final del archivo para agregar nuevos registros, el archivo
#si no existe se crea
#"x" Create (Creación) Crea un archivo, y arroja un error si elmismo ya existe en el directorio

archivo = open('prueba1.txt', 'w')

archivo.write('primer nuevo registro')
#si se graba inmediatamente sin decir mas nada no agrega un salto de linea y graba seguido
#al registro anteriormente grabado
#O sea, primer nuevo registroahora otro registro
archivo.write('ahora otro registro')
#quedo: primer nuevo registroahora otro registro
archivo.close()