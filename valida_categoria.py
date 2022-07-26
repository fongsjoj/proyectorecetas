from pathlib import Path
import  os
categ = input("Escriba la categoria: ")
ruta=Path(Path.home(),'recetas',categ)
if ruta.exists():
    print("Categoria ya existe")
else:
    print("Categoria NO existe")