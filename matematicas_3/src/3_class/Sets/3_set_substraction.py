# 3. Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen al primero pero noal segundo,
# sin repetir ninguno. Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolverá la lista [1].print("We will add elements to the set one: ")

_input = int(input("Enter any number or 0 to cancel: "))
setOne = {_input,}

while _input != 0:
    _input = int(input("Enter another number for the set, or press 0 to exit: "))
    if _input: setOne.add(_input)

print("We will add elements to the set two: ")
_input = int(input("Enter any number or 0 to cancel: "))
setTwo = {_input,}

while _input != 0:
    _input = int(input("Enter another number for the set, or press 0 to exit: "))
    if _input: setTwo.add(_input)

print(setOne - setTwo)
