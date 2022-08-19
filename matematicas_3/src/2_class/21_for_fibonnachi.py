# 4. Muestre los N primeros números de la secuencia de Fibonacci, siendo n un dato entero.

fibonnachiSucession = list(range(int(input("Enter a number, whe show you the first N numbers in fibonnachi sucession: "))))

for i in range(len(fibonnachiSucession)):
    if i == 0: fibonnachiSucession[i] = 0
    if i == 1: fibonnachiSucession[i] = 1
    if i > 1: fibonnachiSucession[i] = fibonnachiSucession[i-2]+fibonnachiSucession[i-1]
    

print(fibonnachiSucession)