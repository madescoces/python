# 3. Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán 
# los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa pedirá el número 
# de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número 
# negativo. Alfinal el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

option = 'y'
testList = []
califiCationDict = {}

while option != 'n' and option != 'N':
    i = 0
    studentName = str(input("Enter student name: "))
    testCalification = int(input("Enter calification for the test 1: "))
        
    while testCalification >= 0:
        testList.append(testCalification)
        i += 1
        testCalification = int(input(f"Enter calification for the test {i+2}, (negative to end): "))
        
    califiCationDict[studentName] = testList
    option = str(input("Continue y/n?"))

print(califiCationDict)
