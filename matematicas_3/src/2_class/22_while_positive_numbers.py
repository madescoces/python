# 1. Escribe un programa que pida la cantidad de números positivos que 
# se tienen que ingresar y a continuación pida números hasta que se hayan 
# ingresado la cantidad de números indicada.

positiveNumbers = list(range(int(input("How much positive numbers you want to enter?: "))))

i = 0
while i < len(positiveNumbers) :
    positiveNumbers[i] = int(input("Enter a positive number:"))
    if positiveNumbers[i] > 0:
        i +=1
    else: 
        print(f"Invalid entry in the list postion {i}, you input {positiveNumbers[i]}, a number bigger then 0 is expected.")

print(positiveNumbers)