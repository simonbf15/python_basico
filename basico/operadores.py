#operadores
num0 = 9
num1= 3

print("los numeros son: ",num0, "y",num1)
#suma
resul = num0 + num1
print("el resultado de la suma es:", resul)
#resta
resul = num0 - num1
print("el resultado de la resta es:",resul)
#multiplicacion
resul = num0 * num1
print("el resultado de la multiplicacion es:",resul)
#division
resul = num0 / num1 #num 1 != 0
print("el resultado de la division es:",resul)


#comparaciones

print(num0 > num1 ) #deberia devolver true
print(num0 < num1 ) #deberia devolver false
print(num0 == num1 ) #deberia devolver false

print ('hola' < 'mundo') #por codigo ascii es menor, no por la cantidad de letras

#tambien estan los operadores logicos

print ('operadores logicos')
print('--------and---------')
print (True and True) # FALSE
print (True and False)# FALSE
print(False and False) #FALSE
print('--------or--------')
print (True or True) #TRUE
print (True or False)#TRUE
#not --> convierte los resultados
print('------not-------')
print (not(True and True)) # true que pasa a ser FALSE
print (not(True and False))# false pasa a ser TRUE
print(not(False and False)) #false que pasa a ser TRUE
