#ejercicio: escribir una funcion que muestre por consola los 
# numeros de 1 a 100 con un salto de linea entre cada impresion
#sustiyuendo los siguientes:
#multiplos de 3 por la palabra "fizz"
#multiplos de 5 por la palabra "buzz"
#multiplos de ambos por la palabra "fizzbuzz"

def funcion0():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print('fizz')
        elif num%5 == 0:
            print('buzz')
        else:
            print(num)
        
funcion0()