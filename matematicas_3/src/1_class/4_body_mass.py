bodyWeigth = float(input("Enter your weigth in Kilo Grams: "))
bodyHeigth = float(input("Enter your heigth in meters: "))
bmi = bodyWeigth/bodyHeigth ** 2
print(f"Your body mass index is: {round(bmi,2)}")