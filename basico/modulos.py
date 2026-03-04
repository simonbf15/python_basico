#modulos o import's

from funciones import sumar
from clases import persona

#hago un print de la funcion sumar
print(sumar(1,3))

#utilizo la clase persona y creo una instancia, luego utilizo un metodo de la misma
simon = persona('simon','bf', 1.75,17,80 )
simon.imprimir_datos()