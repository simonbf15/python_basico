#ejercicio: hacer un programa que pida 3 numeros, 
#los guarde en una lista y muestre el mayor sin usar max()

def max_de_lista(lista1):
    max=lista1[0]
    for number in lista1:
     if number>max:
        max = number   

    return max

lista =[]
i=0
for num in range(3):
    lista.append(int(input('ingrese un numero')))

print(lista)
print('el maximo de la lista es: ',max_de_lista(lista))

