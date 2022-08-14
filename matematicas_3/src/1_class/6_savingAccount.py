firstDeposit = float(input("Enter the first deposit made in the savings account: "))
INTEREST = 0.04
totalBalance = 0

totalBalance = firstDeposit + firstDeposit*INTEREST
print("In the first year your account have: " + str(round(totalBalance,2)))
print()
totalBalance = totalBalance + totalBalance*INTEREST
print("In the second year your account have: " + str(round(totalBalance,2)))
print()
totalBalance = totalBalance + totalBalance*INTEREST
print("In the third year your account have: " + str(round(totalBalance,2)))
print()
