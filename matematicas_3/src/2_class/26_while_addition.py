# 5. Escribe un programa que pida números mientras no se escriba un número 
# negativo. El programa terminará emitiendo la suma de los números ingresados.

acumulator = 0

number = int(input("Enter any positive integer number: "))

while number >= 0:
    acumulator += number
    number = int(input("Enter another positive integer number: "))

print(f"The addition of all numbers is: {acumulator}")