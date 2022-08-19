# 1. Escribe un programa que permita crear una lista de palabras. Para ello, 
# el programa tiene que pedir un número y luego solicitar esa cantidad de palabras 
# para crear la lista. Por último, el programa tiene que emitir la lista.

myList = list(range(int(input("Enter the number of words to include in the list: "))))

for i in myList :
    myList[i] = input(f"Enter any word to store in the position {i}: ")

print("Items inside list: " + str(myList))