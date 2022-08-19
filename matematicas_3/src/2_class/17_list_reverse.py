# 6. Escribe un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, pero al revés (crear una lista distinta).

# Create the first list
firstList = list(range(int(input("Enter the number of words to include in the list: "))))

for i in firstList:
    firstList[i] = input(f"Enter any word to store in the position {i}: ")

# Create the second list
secondList = firstList[:]
secondList.reverse()

print(firstList)
print(secondList)
