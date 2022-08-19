# 4. Escribe un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y elimine esa palabra de la lista.

from os import remove


myList = list(range(int(input("Enter the number of words to include in the list: "))))

for i in myList:
    myList[i] = input(f"Enter any word to store in the position {i}: ")

wordToDelete = input("Type the word to remove from the list: ")
removeAll = input("Do you Want to remove all ocurrences on the list? y/n: ")

if removeAll == 'y' or removeAll == 'Y':
    j = 0
    for i in myList:
        if i == wordToDelete: myList.pop(j)
        j += 1
else:
    myList.remove(wordToDelete)

print(myList)
