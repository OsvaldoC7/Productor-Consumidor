from time import sleep
from agente import Agente
from random import randint
from os import system
import msvcrt
import sys

barra = ""
contenedor = []
espacio_disponible = True
vacio = True

for i in range(20):
    contenedor.append("_")

def imprimir_barra(barra):

    for i in contenedor:
        barra = barra + i + "  "

    print (barra)

    for i in range(20):
        if i+1 < 10:
            print(i+1, end="  ")
        else:
            print(i+1, end=" ")

    print()

def estado_contenedor():

    global vacio, espacio_disponible

    if "*" in contenedor:
        vacio = False
    if "_" in contenedor:
        espacio_disponible = True
    if contenedor.count("*") == 20:
        espacio_disponible = False
    if contenedor.count("_") == 20:
        vacio = True

def salir():

    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        if key_stroke==chr(27).encode():
            print ("Esc presionado, el programa se detuvo.")
            sys.exit()

productor = Agente(False)
consumidor = Agente(False)

while True:

    salir()
    r = randint(1, 14)

    if r%2 == 0:
        productor.activo = True
    else:
        consumidor.activo = True

    if productor.activo == True:           #Produce

        for i in range(productor.tiempo):

            salir()
            estado_contenedor()

            if espacio_disponible == True:

                contenedor[productor.indice] = "*"
                system("cls")
                print("Productor: Activo\tIndice: ", productor.indice)
                print("Consumidor: Dormido\tIndice: ", consumidor.indice)
                productor.avanzar()

            else:

                system("cls")
                print("Productor: Intentando entrar\tIndice: ", productor.indice)
                print("Consumidor: Dormido\tIndice: ", consumidor.indice)

            print("Espacio disponible: ", espacio_disponible, "Vacio: ", vacio)
            imprimir_barra(barra)
            sleep(1)

        productor.activo = False
        productor.calcular_tiempo()

    if consumidor.activo == True:          #Consume
        
        for i in range(consumidor.tiempo):

            salir()
            estado_contenedor()

            if vacio == False:

                contenedor[consumidor.indice] = "_"
                system("cls")
                print("Productor: Dormido\tIndice: ", productor.indice)
                print("Consumidor: Activo\tIndice: ", consumidor.indice)
                consumidor.avanzar()

            else:

                system("cls")
                print("Productor: Dormido\tIndice: ", productor.indice)
                print("Consumidor: Intentando Consumir\tIndice: ", consumidor.indice)

            print("Espacio disponible: ", espacio_disponible, "Vacio: ", vacio)
            imprimir_barra(barra)
            sleep(1)

        consumidor.activo = False
        consumidor.calcular_tiempo()
