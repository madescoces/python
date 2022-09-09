# 4. Codifica un programa que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, 
# cuantas palabras y cuántos caracteres contiene el archivo.

import os

os.chdir('matematicas_3/src/3_class/FileSystem')

lines = 0
words = 0
chars = 0

with open('dummy.txt','r', encoding='utf-8') as f:
    for linea in f:
        lines += 1
        words += linea.count(' ')
        chars += len(linea)
        print()
        print(f"Line: {lines}")
        print(f"Words: {linea.count(' ')}")
        print(f"Chars: {len(linea)}")

        
            
print()
print("Results: ")
print(f"Total lines: {lines}")
print(f"Total words: {words}")
print(f"Total chars: {chars}")