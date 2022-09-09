# 3. Codifica un programa que escriba en un archivo los siguientes datos:
# "Nombre","Apellido","Telefono","Cumpleaños"

import os

os.chdir('matematicas_3/src/3_class/FileSystem')

option = 'y'
addressDict = {}

while option != 'n' and option != 'N':
    addressDict['First Name: '] = str(input("Enter first name: "))
    addressDict['Last Name: '] = str(input("Enter last name: "))
    addressDict['Phone Number: '] = int(input("Enter phone number: "))
    addressDict['Birth Date: '] = str(input("Enter birthdate: "))

    print()
    option = str(input("Continue y/n: "))


with open('lista.txt',mode='w', encoding='utf-8') as f:
    for item in addressDict:
        f.write(str(item) + str(addressDict[item]) + '\n')