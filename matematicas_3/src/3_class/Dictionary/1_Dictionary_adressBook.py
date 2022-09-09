# 1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar).
# Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. No se podrán ingresar nombres
# repetidos.

addressBook = {}
option = 's'

while option == 's' or option == 'S':
    print()
    userName = str(input("Enter user name: "))
    
    while userName in addressBook:
        print(f"{userName} already used.")
        userName = str(input("Enter a diferent name: "))        
    else: 
        addressBook[userName] = int(input("Enter phone number: "))
    
    option = input("Continue? s/n.")
    
print(addressBook)