"""
Intersection example
Brayan Pineda Méndez - 18390039
Examen de recuperación 3D - Enero 01, 2021
"""
#Se importan las librerías
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import keyboard as keyboard

#------------ Coordenadas iniciales
xg = []
yg = []
zg = []

#----------- Coordenadas centrales
xc = 80
yc = 40
zc = 40

#----------- Plotear el sistema
#------ Tamaño de la ventana
def plotPlaneLine(xg, yg, zg):
    plt.axis([0, 200, 350, -100])
    plt.axis('on')
    plt.grid(True)

    #----- Formar el triángulo
    plt.plot([xg[0], xg[1]], [yg[0], yg[1]], color='k')
    plt.plot([xg[0], xg[2]], [yg[0], yg[2]], color='k')
    plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k')

    #----- Triangulo Hit point
    plt.plot([xg[0], xg[3]], [yg[0], yg[3]], linestyle=':', color='r')
    plt.plot([xg[1], xg[3]], [yg[1], yg[3]], linestyle=':', color='r')
    plt.plot([xg[2], xg[3]], [yg[2], yg[3]], linestyle=':', color='r')

    #----- HitPoint con formula de Heron
    #Area de A
    a = xg[0] - xg[1] #Distancia del punto 0 al 1
    b=yg[0]-yg[1]
    d01=sqrt(a*a+b*b)

    a=xg[0]-xg[2] #Distancia del punto 0 al 2
    b=yg[0]-yg[2]
    d02=sqrt(a*a+b*b)

    a=xg[1]-xg[2] #Distancia entre 1 al 2
    b=yg[1]-yg[2]
    d12=sqrt(a*a+b*b)

    s=(d01+d12+d02)/2
    A=sqrt(abs(s*(s-d01)*(s-d12)*(s-d02))) #Area de A


    #Area de A1
    a=xg[1]-xg[3] #Distancia del punto 1 al 3
    b=yg[1]-yg[3]

    d13=sqrt(a*a+b*b)

    a=xg[0]-xg[3] #Distancia del punto 0 al 2
    b=yg[0]-yg[3]

    d03=sqrt(a*a+b*b)

    s=(d01+d13+d03)/2
    A1=sqrt(abs(s*(s-d01)*(s-d13)*(s-d03))) #Area de A1


    #Area de A2
    a=xg[2]-xg[3]
    b=yg[2]-yg[3]

    d23=sqrt(a*a+b*b)

    s=(d01+d13+d03)/2
    A2=sqrt(abs(s*(s-d23)*(s-d02)*(s-d03)))

    sumaArea = A1 + A2

    if(sumaArea < A):
        validar='Dentro'
    else:
        validar='Fuera'

    plt.text(10, 60, A)
    plt.text(10, 45, A1)
    plt.text(10, 30, A2)
    plt.text(10, 15, validar)

    plt.show()


#Pedir los datos del punto donde se desea plotear el gráfico
print('Presiona ENTER para ingresar los datos.')
print('Presiona ESC para salir del programa.')
while True:
    if keyboard.is_pressed('ENTER'): #Se requiere instalar Keyboard
        input()
        axis = int(input('Valor del hitpoint 1: '))
        x = [40, 30, 80, axis]
        axis = int(input('Valor del hitpoint 2: '))
        y = [60, 10, 60, axis]
        z = [-10, 10, 10, -10]

        for i in range(len(x)):
            xg.append(x[i]+xc)
            yg.append(y[i]+yc)
            zg.append(z[i]+zc)

        plotPlaneLine(xg, yg, zg)

    elif keyboard.is_pressed('ESC'): #Se valdia si se ha presionado Esc
        break