day = input("Enter the day of the week: ")
exam = False


if day == 'monday' or day == 'tuesday' or day == 'wednesday':
    selection = input(f"press 'Y' if there was an exam on {day}, else press other key: ")
    if selection == 'y' or selection == 'Y':
        exam = True
elif day == 'thursday':
    assistance = input(f"Percentage of assistance on {day}:")
    if assistance > 50:
        print(f"Most of students attended on {day}")
    else:
        print(f"Most of students did not attend on {day}")
elif day == 'friday':
    print(f"{day.capitalize()} is quiz day.")
    assistance = int(input(f"Enter the number of students: "))
    price = int(input("Enter the fee for quiz day: "))
    print("Quiz day total income: " + str(assistance*price) + " Usd")


if exam == True:
    approved = int(input(f"Enter how many they passed the exam on {day}: "))
    disapproved = int(input(f"Enter how many did not pass the exam on {day}: "))
    print(f"The percentage of approval on {day} is: " + str(round(approved*100/(approved+disapproved),1)) + "%")

