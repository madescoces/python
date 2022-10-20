from clases_maquina import *

class Actividad(Maquina):
    def __init__(self, nombre, id, fecha):
        super().__init__(nombre, id, fecha)

    def mostrar_info(self):
        print('Información....')
        print(f'Nombre:{self.nombre}')
        print(f'Id:{self.id}')
        print(f'Fecha arranque:{self.fecha}')

    