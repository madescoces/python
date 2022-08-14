time = int(input("Enter the number of seconds to convert in Hours, Minutes, Seconds: "))
hours = time/3600
minutes = ((hours - int(hours))*60)
seconds = ((minutes - int(minutes))*60)

print(f"{time} seconds equals to: " + str(int(hours)) + \
    " hours " + str(int(round(minutes))) + " minutes " + str(int(round(seconds))) + " seconds")