# 2. Crear un programa donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final 
# de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará
# si queremos hacer otra consulta.

fruitPriceBook = {"mandarina":150,"pera":160, "banana": 330, "frutilla": 900, "kiwi": 670, "lima": 250, "limón": 100, "manzana":300}
option = 's'

while option == 's' or option == 'S':
    print()
    fruitName = str(input("Enter fruit name: "))
    kilograms = 0

    while fruitName not in fruitPriceBook:
        print(f"{fruitName} is not available.")
        fruitName = str(input("Try another one: "))        
    else: 
        kilograms = int(input("Enter the quantity in kilograms:")) 
    
    print(f"You must pay {kilograms*fruitPriceBook[fruitName]} pesos for {kilograms} kilograms of {fruitName}")
    option = input("Continue? s/n.")