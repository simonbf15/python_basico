#condiciones y bucles

print('primero el if')
num1 = 10
num2= 10

if num1 < num2:
    print(num1, 'es menor que', num2)
else:
    print(num1,'es mayor o igual que', num2)



texto1 = "el lineage2 es un juegazo pero la gente no lo juega mucho"
if len(texto1) >= 10:
    print("el texto ingresado es mayor o igual a 10 caracteres")
else:
    print('el texto ingresado es menor a 10 caracteres')


print('----------------')
print('----------------')
print('----------------')
print('----------------')

print('ahora vamos con elif')
if num1 < num2:
    print(num1, 'es menor que', num2)
elif num1==num2:
    print(num1,'es igual que',num2)
else:
    print(num1,'es mayor que', num2)