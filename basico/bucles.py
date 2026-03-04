#bucles 

num1 = 0
resul=0

print('vamos con el WHILE')
while num1 < 5:
    num1 +=1
    print(num1)
    if num1 < 3:
        print('es menor que 3')
    else:
        print('no es menor que 3')
    resul= resul+num1


print('la suma de los numeros iterados es:',resul)

print('---------------------------------')
print('---------------------------------')

print('vamos con el FOR')

#recorremos la lista con un for, segun el rango de la lista.
lista = [15,30,22,8,4]
for number in lista:
    print(number)
    if(number == 22):
        print('el numero es igual a 22, finaliza el FOR')
        break


#se utiliza el range para recorrer desde 0 a el valor que le pasemos
for character in range(25):
    print(character)
    if (character==5):
        print('encontraste el 5, saliendo del for...')
        break