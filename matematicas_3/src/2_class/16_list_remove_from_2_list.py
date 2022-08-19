# 5. Escribe un programa que permita crear dos listas de palabras y que, 
# a continuación, elimine de la primera lista los nombres de la segunda lista.

# Create the first list
firstList = list(range(int(input("Enter the number of words to include in the list: "))))

for i in firstList:
    firstList[i] = input(f"Enter any word to store in the position {i}: ")


# Create the second list
secondList = list(range(int(input("Enter the number of words to include in the list: "))))

for i in secondList:
    secondList[i] = input(f"Enter any word to store in the position {i}: ")

for i in range(len(firstList)-1,-1,-1):
    for j in range(len(secondList)):
        if firstList[i] == secondList[j]:
            firstList.pop(i)

print(firstList)
