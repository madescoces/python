dollWeigth = 75
clownWeigth = 112
packageWeigth = 0

numberOfDolls = int(input("Enter the number of dolls for this package: "))
numberOfClowns = int(input("Enter the number of clowns for this package: "))

packageWeigth = dollWeigth*numberOfDolls + clownWeigth*numberOfClowns

print(f"Total weigth of package is: {packageWeigth} grams.")