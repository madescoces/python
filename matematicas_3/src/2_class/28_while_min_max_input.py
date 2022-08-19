# 7. Escribe un programa que pida primero dos números enteros (mínimo y máximo) 
# y que después pida números enteros situados entre ellos. El programa terminará 
# cuando se escriba un número que no esté comprendido entre los dos valores iniciales
# y emitirá la cantidad de números ingresados.

counter = 0

min = int(input("Enter the min number: "))
max = int(input("Enter the max number: "))
number = int(input(f"Enter any integer number between {min} and {max}: "))

while number >= min and number <= max:
    counter += 1
    number = int(input("Enter another integer number: "))

print(f"{counter} numbers were entered.")