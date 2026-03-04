#ejercicio: crear una funcion que reciba una lista de numeros y devuelva el maximon, minimo y
#el promedio, sin usar las funciones max(), min () ni sum(). No se puede recorrer la lista mas
#de una vez

def analizar_lista(lista):
    if not lista:
        raise ValueError('la lista no puede estar vacia')

    sumatoria = 0
    maximo = lista[0]
    minimo = lista [0]
        
    for num in lista:
        if not isinstance(num,(int,float)):
            raise TypeError('todos los elementos deben ser numeros')
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

        sumatoria += num
            
    promedio = sumatoria / len(lista)

    return(maximo, minimo, promedio)

        

    


lista = [3,7,1,9]

maximo,minimo,promedio = analizar_lista(lista)
print('Lista: ', lista)
print('maximo: ', maximo)
print('minimo: ', minimo)
print('promedio: ', promedio)