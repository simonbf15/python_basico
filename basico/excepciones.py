#excepciones

try:
    num1= int(input('ingrese dos numeros, primero el numero a dividir '))
    num2 = int(input('ingrese el divisor '))
    resultado = num1 / num2
except ValueError as error:
    print('error de tipo ValueError')
    print(error)

except:
    print('error: no se puede dividir por 0 ')
else:
    print('el resultado de la division es: ',resultado)
 