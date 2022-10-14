#Escribe tres programas que emitan las siguientes secuencias de números:
#• En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento.
#• En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos.
#• En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos.

for i in range(10):
    print(f"el valor de i es: {i}")

print("\n")
for i in range(10,20):
    print(f"el valor de i es: {i}")

print("\n")
for i in range(10,20,2):
    print(f"el valor de i es: {i}")