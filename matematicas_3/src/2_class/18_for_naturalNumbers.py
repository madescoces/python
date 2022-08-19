# 1. Escribe un programa que le permita realizar la escritura de los primeros 100 números naturales.

naturalNumbers = list(range(100))

for i in range(len(naturalNumbers)):
    naturalNumbers[i] = i+1

print(naturalNumbers)