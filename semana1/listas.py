#listas
print('----------------')
lista1 = ['python', 15, 333, True]
#tipo de variable
print (type(lista1))
#imprimiendo la lista completa
print(lista1)
#imprimiendo el primer item de la lista
print(lista1[0])



print('----------------')
print('agregar con append')
lista1.append('agregando un item en la lista')
print(lista1)


print('----------------')
print('agregar con insert en determinado lugar')
lista1.insert(1, 'agregando en el segundo lugar')
print(lista1)


print('----------------')
print('eliminar con remove')
lista1.remove(15)
print(lista1)


print('----------------')
print('imprimo lista completa')
print(lista1)


print('----------------')
print('iterando sobre lista')
i=0
for row in lista1:
    print (lista1[i])
    i+=1
print('----------------')

#cuantas veces aparece la palabra python en la lista
print(lista1.count('python'))

