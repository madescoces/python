"""2. Convertir a funciones los siguientes ejercicios:
a. Práctica de rangos-listas-for-while:
a) Ejercicio 6 de rangos
b) Ejercicio 6 de listas
c) Ejercicio 3 y 4 de ciclo for
d) Ejercicio 7 de ciclo while
b. Práctica de tuplas-conjuntos-diccionarios
e) Ejercicio 3 de tuplas
f) Ejercicio 4 de conjuntos
g) Ejercicio 3 de diccionarios"""

# 6. Escribe un programa que pida dos números enteros y emita la lista de números pares que hay 
# entre ellos(incluidos ellos mismos si son pares)
"""def even(a,b):
    evenList = []
    for i in range(a,b):
        if i % 2 == 0:
            evenList.append(i)
    return evenList

evenList = even(int(input("Enter the first Number: ")),int(input("Enter top number: ")))
print(evenList)"""

# 6. Escribe un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, pero al revés (crear una lista distinta).
"""listado = (str(input("Enter a list of words, space separated: "))).split(' ')          
def reverseList(anyList):
    lista = anyList 
    lista.reverse()  
    return lista

print(listado)
reversed = reverseList(listado)
print(reversed)"""

# 3. Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado.
"""def factorial(number):
    factorialNumber = 1
    for i in range(number+1):
        if i != 0: factorialNumber *= i
    
    return factorialNumber

print(factorial(int(input("Enter a number to calculate its factorial: "))))"""

# 4. Muestre los N primeros números de la secuencia de Fibonacci, siendo n un dato entero.
"""def fibonnachi(number):
    fibonnachiSucession = list(range(number))

    for i in range(len(fibonnachiSucession)):
        if i == 0: fibonnachiSucession[i] = 0
        if i == 1: fibonnachiSucession[i] = 1
        if i > 1: fibonnachiSucession[i] = fibonnachiSucession[i-2]+fibonnachiSucession[i-1]

    return fibonnachiSucession   

print(fibonnachi(int(input("Enter a number, whe show you the first N numbers in fibonnachi sucession: "))))"""

# 7. Escribe un programa que pida primero dos números enteros (mínimo y máximo) 
# y que después pida números enteros situados entre ellos. El programa terminará 
# cuando se escriba un número que no esté comprendido entre los dos valores iniciales
# y emitirá la cantidad de números ingresados.
"""def between(min,max,number):
    counter = 0

    while number >= min and number <= max:
        counter += 1
        number = int(input("Enter another integer number: "))

    return counter

min = int(input("Enter the min number: "))
max = int(input("Enter the max number: "))
number = int(input(f"Enter any integer number between {min} and {max}: "))

print(str(between(min,max,number)) + " numbers entered.")"""

# 3. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con 
# la siguiente forma: (nombre, dni, destino). 
# Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), 
# ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]

# Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
# Ejemplo: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), 
# ("Londres", "Inglaterra"), ("Madrid", "España")]

# Hacer un programa que permita al usuario realizar las siguientes operaciones:
# -Agregar pasajeros a la lista de viajeros.
# -Agregar ciudades a la lista de ciudades.
# -Dado el DNI de un pasajero, emitir a qué ciudad y país viaja.
# -Dado un país, mostrar cuántos pasajeros viajan a ese país.
# -Salir del programa.

#database = [("Manuel Juarez", 19823451, "Liverpool"),("Silvana Paredes", 22709128, "Buenos Aires"), ("Roxana Paredes", 22709135, "Rosario"), ("Rosa Ortiz", 15123978, "Glasgow"),("Luciana Hernandez", 38981374, "Lisboa")]
#countryAndCity = [("Buenos Aires", "Argentina"),("Glasgow", "Escocia"),("Lisboa", "Portugal"),("Londres", "Inglaterra"),("Madrid", "España"),("Rosario", "Argentina")]

#database.append((str(input("Enter the passenger name: ")), int(input("Enter passenger Id.: ")), str(input("Enter the fly destination:"))))
#countryAndCity.append((str(input("Enter city name: ")),str(input("Enter country name: "))))

def passenger():
    name, id, destiny = str(input("Enter the passenger name: ")), int(input("Enter passenger Id.: ")), str(input("Enter the fly destination: "))
    return (name,id,destiny)

def city():
    city, country = str(input("Enter city name: ")), str(input("Enter country name: "))
    return (city,country)


def databaseCreation(func):
    option = 'y'
    lista = []
    
    while not (option == 'n' or option == 'N'):
        lista.append()
        option = str(input("Enter another one: (y/n)"))

    return lista
    
passengerDatabase = databaseCreation(passenger())
cityDatabase = databaseCreation(city())

print(passengerDatabase)
print(cityDatabase)
"""idSearch = int(input("Enter the passenger id: "))

for name, id, destination in database:
    if id == idSearch:
        for city, country in countryAndCity:
            if destination == city:
                print(f"The passenger {name} fly to {city} in {country}")
   
countrySearch = input("Enter country name: ")
cityList = []

for city, country in countryAndCity:
    if country == countrySearch:
        cityList.append(city)

print(f"The number of passengers flying to {countrySearch} is {len(cityList)}")"""