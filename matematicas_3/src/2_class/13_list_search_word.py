# 2. Escribe un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.

myList = list(range(int(input("Enter the number of words to include in the list: "))))
count = 0

for i in myList :
    myList[i] = input(f"Enter any word to store in the position {i}: ")

word = input("Type the word for search: ")

for i in myList:
    if i == word:
        count += 1

print(f"The word {word} appears {count} times in the list.")