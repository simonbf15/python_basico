#ejercicio: hacer un programa que pida 3 numeros, 
#los guarde en una lista y muestre el mayor sin usar max()

def max_de_lista(lista1):
    maximo=lista1[0]
    for number in lista1:
     if number>maximo:
        maximo = number   

    return maximo

lista =[]
for num in range(3):
    lista.append(int(input('ingrese un numero ')))

print("Lista:", lista)
print('el maximo de la lista es: ',max_de_lista(lista))

