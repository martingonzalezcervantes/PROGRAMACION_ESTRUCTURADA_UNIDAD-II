# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()

nom="Daniel"
ape="Carreon"

nombre,apellido=modulos.funcion4(nom,ape)
print(f"Nombre: {nombre}\nApellido: {apellido}")


# 2da formar de utilizar modulos
from modulos import borrarPantalla,funcion4

borrarPantalla()

nom="Daniel"
ape="Carreon"

nombre,apellido=funcion4(nom,ape)
print(f"Nombre: {nombre}\nApellido: {apellido}")
