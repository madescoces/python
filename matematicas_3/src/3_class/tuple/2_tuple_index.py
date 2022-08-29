# 2. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por 
# teclado y muestra los valores de la tupla.

myTupla = (10,9,7,8,5,6,4,2,3,1)

myIndex = int(input("Enter a index number: "))

print(f"Database type: {type(myTupla)}")
print(f"The number stored in {myIndex} is: {myTupla[myIndex]}.")