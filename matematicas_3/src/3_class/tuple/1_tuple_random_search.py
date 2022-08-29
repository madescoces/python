# 1. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

import random

myTuple = list(range(20))

for i in myTuple:
    myTuple[i] = (int(random.randrange(0,10)))

myTuple = tuple(myTuple)

myNumber = int(input("Enter a integer for search in the database: "))
print(str(myTuple) + " <- database")
print(str(type(myTuple)) + " <- database type")

count = 0
for i in myTuple:
    if myNumber == i:
        count += 1    

if count:    
    print(f"The number {myNumber} is {count} times in the database.")
else:
    print(f"The number {myNumber} isn't in the database.")