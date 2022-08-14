day = input("Enter a day of the week: ")

if day == "monday":
    print(f"{day} is the second day of the week!")
elif day == "friday":
    print(f"yay is {day}!!")
elif day == "saturday" or day == "sunday":
    print(f"Have a nice {day}!!")
else: 
    print(f"Your enter {day}, enter monday, friday, sunday or saturday for new messages!")