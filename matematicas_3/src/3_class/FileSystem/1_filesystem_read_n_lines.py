# 1. Codifica un programa que reciba un archivo de texto y emita las primeras N líneas del archivo. 
# Las N líneas deben ser ingresadas por teclado.

#with open ("dummy.txt","r",encoding='utf8') as dummyText:
#    text = dummyText

#print (text)
import os

os.chdir('matematicas_3/src/3_class/FileSystem')

i = 0
print()
n = int(input("Enter the number of lines to print: "))
print()

with open('dummy.txt','r', encoding='utf-8') as f:
    for linea in f:
        if i < n:
            print(linea, end='')
        i += 1
    