"""Ejercicio 5.
Crear la clase Mate que describa el funcionamiento de la bebida.
a. El constructor debe recibir como parámetro n, la cantidad máxima de cebadas en base a la cantidad de yerba vertida en el recipiente que también debe ser un parámetro.
b. Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
c. Un atributo para el estado (lleno o vacío).
d. Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que imprima el mensaje: Uhh! Te quemaste!
e. Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío se debe lanzar una excepción que imprima el mensaje: El mate está vacío!...;"""

class Mate:
    cantYerba = 0
    cantCebadas = 0
    maxCebadas = 0
    lleno = False
    
    def __init__(self, cantYerba, maxCebadas):
        self.cantYerba = cantYerba
        self.cantCebadas = maxCebadas
    
    def cebar(self):
        try:
            if not self.lleno: 
                self.lleno = True
            else: 
                raise ValueError
        except ValueError:
            print("Uhh! Te quemaste!")

    def beber(self):
        try:
            if not self.lleno: 
                raise ValueError
            else: 
                self.lleno = False 
                self.restarCebada()
        
        except ValueError:
            print("El mate está vacío!...")
        
    def restarCebada(self):
        try:
            if not self.cantCebadas <= 0: 
                self.cantCebadas -= 1 
            else: 
                raise ValueError                
        
        except ValueError:
            print("No hay cebadas disponibles")