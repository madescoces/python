# 3. Escribe un programa que pida números decimales mientras el usuario escriba número mayores que el primero.

decimalNumberOne = float(input("Enter a decimal number: "))
decimalNumberTwo = float(input("Enter another decimal number: "))

while decimalNumberOne <= decimalNumberTwo:
    decimalNumberTwo = float(input("Enter another decimal number: "))

print(decimalNumberOne)
print(decimalNumberTwo)