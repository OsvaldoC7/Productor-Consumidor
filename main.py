from time import sleep
from agente import Agente

barra = ""
#contenedor = ["*", "*", "*", "*", "*", "*", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
contenedor = []

for i in range(20):
    contenedor.append("_")

for i in contenedor:
    barra = barra + i + "  "
    #print("_", end="  ")

print (barra)

for i in range(20):
    if i+1 < 10:
        print(i+1, end="  ")
    else:
        print(i+1, end=" ")

productor = Agente(True)
consumidor = Agente(False)
while True:
    

    if productor.activo == True:           #Produce
        pass

    if consumidor.activo == True:          #Consume
        pass

    for i in range(productor.tiempo):


        productor.avanzar()

    for i in range(consumidor.tiempo):


        consumidor.avanzar()

    sleep(1)
