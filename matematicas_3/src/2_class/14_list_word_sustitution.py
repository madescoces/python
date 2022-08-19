# 3. Escribe un programa que permita crear una lista de palabras y que, a continuación, 
# pida dos palabras y sustituya la primera (que debe estar en la lista) por la segunda. Emitir la lista.

myList = list(range(int(input("Enter the number of words to include in the list: "))))
count = 0

for i in myList:
    myList[i] = input(f"Enter any word to store in the position {i}: ")

word = input("Type the word to replace: ")
replaceWord = input("Type the word that will replace it: ")

for i in myList:
    if i == word:
        break 
    count += 1

myList[count] = replaceWord

print(f"The word {word} was replace it by {replaceWord} in list position {count}, here is the final result: ")
print(myList)