from random import randint

class Agente:

    def __init__(self, estado):

        self.tiempo = randint(3, 6)     # Tiempo dentro del buffer, Se consume o produce un elemento por segundo
        self.activo = estado            # Dormido = False, Activo = True
        self.indice = 0                 # Indice en el que trabajara

    def avanzar(self):

        self.indice += 1
        if self.indice == 20:
            self.indice = 0

    def calcular_tiempo(self):
        self.tiempo = randint(3, 6)     # Tiempo dentro del buffer, Se consume o produce un elemento por segundo

    
