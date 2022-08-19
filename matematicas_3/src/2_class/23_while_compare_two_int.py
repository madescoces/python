# 2. Escribe un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras 
# no sea mayor que el primero. El programa termina y emitirá los números.

numberOne = int(input("Enter a integer number: "))
numberTwo = int(input(f"Enter another integer bigger than {numberOne}: "))

while numberOne >= numberTwo:
    print(f"Invalid input, expeted a number bigger than {numberOne}")
    numberTwo = int(input(f"Enter another please: "))

print(f"The first number is {numberOne}")
print(f"The second number is {numberTwo}")