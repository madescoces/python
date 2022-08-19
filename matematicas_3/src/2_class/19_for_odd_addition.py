# 2. Escribe un programa que le permita realizar la suma de los primeros N números impares. 
# El N debe ingresarse por teclado.

oddNumberAddition = 0

for i in range(int(input("Enter any number, whe add all odd numbers from 1 to that number: "))+1):
    if i%2 != 0: oddNumberAddition += i

print(oddNumberAddition)