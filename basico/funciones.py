#funciones

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def restar(num1, num2):
    resultado = num1 - num2
    return resultado


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    if num2 == 0:
        return int(-1)
    
    resultado = num1 / num2
    return resultado


#Lo comento para importar las funciones en modulos.py

#num1 = int(input('escribe el primer numero '))
#num2 = int(input('escribe el segundo numero '))

#print('la suma de los numeros es',sumar(num1,num2))
#print('la multiplicacion de los numeros es',multiplicar(num1,num2))
#print('la resta de los numeros es',restar(num1,num2))
#print('la division de los numeros es',dividir(num1,num2))