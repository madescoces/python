# 6. Escribe un programa que pida un valor límite positivo y a continuación pida números hasta que 
# la suma de los números introducidos supere el límite inicial.


acumulator = 0

max = int(input("Enter the max number: "))
number = int(input("Enter any integer number: "))

while acumulator <= max:
    acumulator += number
    number = int(input("Enter another integer number: "))

print(f"The addition of all numbers is: {acumulator}")