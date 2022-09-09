# 2. Codifica un programa que copie el contenido de un archivo (sea de texto o binario) a otro, de modo que quede
# exactamente igual.

import os

os.chdir('matematicas_3/src/3_class/FileSystem')

fileTwo = open('dummy_copy.txt','w')

with open('dummy.txt',mode='r', encoding='utf-8') as f:
    for linea in f:
        fileTwo.write(str(linea))