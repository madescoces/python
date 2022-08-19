# 8. Escribe un programa que pida números pares mientras el usuario indique que quiere seguir introduciendonúmeros. 
# Para indicar que quiere seguir escribiendo números, el usuario deberá contestar ‘S’ o ‘s’ a la pregunta.number = int(input(f"Enter any integer number between {min} and {max}: "))

continueLoop = 'y'

while continueLoop == 'y' or continueLoop == 'Y':
    number = int(input("Enter a even number: "))
    while number % 2 != 0:
        number = int(input(f"{number} is not a even number, plz enter another one."))
    
    continueLoop = input("Continue Y/N?.")
    
    

