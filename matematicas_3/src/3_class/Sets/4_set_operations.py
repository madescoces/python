# 4. Diseña un programa que facilite el trabajo con conjuntos. Recuerda que un conjunto es una lista en 
# la que no hay elementos repetidos. Debes implementar:
#   • lista_a_conjunto(lista): Devuelve un conjunto con los mismos elementos que hay en lista, pero sin repeticiones.
# (Ejemplo: lista_a_conjunto([1,1,3,2,3]) devolverá la lista [1, 2, 3] (aunque también se acepta como equivalente
# cualquier permutación de esos mismos elementos, como [3,1,2] o [3,2,1]).
#   • union(A, B): devuelve el conjunto resultante de unir los conjuntos A y B.
#   • interseccion(A, B): devuelve el conjunto cuyos elementos pertenecen a A y a B.
#   • diferencia(A, B): devuelve el conjunto de elementos que pertenecen a A y no a B.
#   • iguales(A, B): devuelve cierto si ambos conjuntos tienen los mismos elementos, y falso en caso contrario.

import random

# fill a list, random size & random numbers
firstList = list(range(random.randrange(0,20)))
for i in range(random.randrange(0,10)):
    firstList.append((random.randrange(0,20)))

# fill a second list, random size & random numbers
secondList = list(range(random.randrange(0,20)))
for i in range(random.randrange(0,10)):
    secondList.append((random.randrange(0,20)))

print("1. Set union (A, B)")
print("2. Set intersection (A, B)")
print("3. Set substraction (A, B)")
print("4. Set compare (A, B)")
print("5. Press 0 to exit")
option = int(input("Choose a operation: "))

while option != 0:
    print()
    if option == 1:
        print("Union of (A + B) = " + str(set(firstList) | set(secondList)))
    if option == 2:
        print("Intersection of (A & B) = " + str(set(firstList) & set(secondList)))
    if option == 3:
        print("Substraction of (A - B) = " + str(set(firstList) - set(secondList)))
    if option == 4:
        print("Comparison of (A & B) = " + str(set(firstList) == set(secondList)))
    print()
    print(f"Original set was: {set(firstList)}.")
    print(f"Original set two was: {set(secondList)}.")

    print()
    print("1. Set union (A, B)")
    print("2. Set intersection (A, B)")
    print("3. Set substraction (A, B)")
    print("4. Set compare (A, B)")
    print("5. Press 0 to exit")
    option = int(input("Choose another operation: "))
