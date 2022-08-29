""" 3. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Ejemplo:
[("Manuel Juarez", 19823451, "Liverpool"),
("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"),
("Luciana Hernandez", 38981374, "Lisboa")
]
Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
[("Buenos Aires", "Argentina"),
("Glasgow", "Escocia"),
("Lisboa", "Portugal"),
("Londres", "Inglaterra"),
("Madrid", "España")
]
Hacer un programa que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, emitir a qué ciudad y país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa. """

database = [("Manuel Juarez", 19823451, "Liverpool"),("Silvana Paredes", 22709128, "Buenos Aires"), ("Roxana Paredes", 22709135, "Rosario"), ("Rosa Ortiz", 15123978, "Glasgow"),("Luciana Hernandez", 38981374, "Lisboa")]
countryAndCity = [("Buenos Aires", "Argentina"),("Glasgow", "Escocia"),("Lisboa", "Portugal"),("Londres", "Inglaterra"),("Madrid", "España"),("Rosario", "Argentina")]

#database.append((str(input("Enter the passenger name: ")), int(input("Enter passenger Id.: ")), str(input("Enter the fly destination:"))))
#countryAndCity.append((str(input("Enter city name: ")),str(input("Enter country name: "))))

idSearch = int(input("Enter the passenger id: "))

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

print(f"The number of passengers flying to {countrySearch} is {len(cityList)}")