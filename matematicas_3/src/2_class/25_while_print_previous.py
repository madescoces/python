# 4. Escribe un programa que pida números enteros mientras el usuario 
# ingresa números cada vez más grandes,el programa emite en cada iteración 
# el número anterior ingresado y finaliza ingresando un número menor.

numberOne = int(input("Enter a integer number: "))
numberTwo = int(input("Enter another integer number: "))

while numberOne <= numberTwo:
    print(f"Previous number was: {numberOne}")
    numberOne = numberTwo
    numberTwo = int(input("Enter another integer number: "))
    