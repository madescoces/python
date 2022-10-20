from datetime import *

class Maquina:
    nombre = ''
    id = ''
    fecha = ''
    
    def __init__ (self, nombre, id, fecha):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha

    def parar(self):
        print('ZZZZzzzzzzzzz')

    def marcha(self):
        print('blablablaaaaa')
    
    def contar(self,tope):
        for i in range(1,tope+1):
            print(f'{i}')
    
    def age(self,birthdate):
        today = date.today()
        
        #Guarda uno o cero para manejar los años biciestos
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
       
        year_difference = today.year - birthdate.year
        age = year_difference - one_or_zero
        
        return age

    def emitir(self):
        print(f'\nNombre de la maquina: {self.nombre}')
        print(f'Antiguedad de la máquina: {self.age(self.fecha)} años')

opcion = str(input('Desea crear una nueva máquina? s/n '))

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%d-%m-%Y").strftime('%d-%m-%Y'):
            raise ValueError
        return True
    except ValueError:
        return False

def startDate():
    fecha = str(input("Ingrese la fecha de puesta en marcha DD-MM-YYYY: "))
    if(validate(fecha)):
        return datetime.strptime(fecha, "%d-%m-%Y").strftime('%d-%m-%Y') 
    else: 
        print("Fecha incorrecta, ingrese dia/mes/año, ej.: 01-05-1978")

maquina = ''

while (opcion != 'n' and opcion != 'N'):
    maquina = (Maquina(nombre=str(input('Nombre: ? ')), id=str(input('Id: ? ')), fecha=startDate()))
    opcion = str(input('Desea crear una nueva máquina? s/n '))

print(f'Nombre de la máquina: {maquina.nombre}') if (str(input('Desea mostrar el nombre de la máquina? s/n '))=='s') else False
maquina.marcha() if (str(input('Quiere encenderla?: s/n '))=='s') else False
maquina.parar() if (str(input('Quiere detenerla?: s/n '))=='s') else False
maquina.contar(int(input('Hasta que número?: '))) if (str(input('Quiere hacerla contar?: s/n '))=='s') else False