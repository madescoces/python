yearNumber = int(input("Enter a year number, and we'll tell you if it's a leap year: "))

if yearNumber % 4 == 0 and yearNumber % 100 != 0:
    print(f"{yearNumber} is leap year")
elif yearNumber % 400 == 0:
    print(f"{yearNumber} is leap year")
else:
    print(f"{yearNumber} isn't leap year")   
    