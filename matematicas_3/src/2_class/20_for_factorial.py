# 3. Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado.
factorialNumber = 1

for i in range(int(input("Enter a number to calculate its factorial: "))+1):
    if i != 0: factorialNumber *= i

print(factorialNumber)