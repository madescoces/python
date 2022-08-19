one = int(input("Enter any natural number: "))
two = int(input(f"Enter another natural number different to {one}: "))

if one < two:
    if one % 2 == 0:
        myList = list(range(one,two,2))
    else:
        myList = list(range(one+1,two,2))
else:
    if two % 2 == 0:
        myList = list(range(two,one,2))
    else:
        myList = list(range(two+1,one,2))

print(myList)
