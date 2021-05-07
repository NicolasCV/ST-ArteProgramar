#Nicolas Cardenas Valdez A01114959
#Angel Ivan vargas Medina 

#Reflexiones:
#Nicolas
'''
Aprendi un poco mas a utilizar matrices en un ejemplo como este
Aprendi mas sobre la libreria turtle y como puede ser utilizada
Practique aun mas con Github
'''

#Angel
'''


'''

from random import *
from turtle import *
from freegames import path
from PIL import Image

#Lo que va a tener nuestro memorama
alumnos = """Tere
Luis Carlos
Alexandra
Nico
Edgar
Ricardo
Miguel
Ernesto
Frida
Tabatha
Marcelo
Dani
Omar
Héctor
Iván
Enrique
Adrián
Axel
Carlo
Alejandro
Cirino
Rodrigo
Abraham
Jesús
Rubén
Roberto
Diego
Ángel
Ana
José
Andrés
Ricardo"""
tiles = (alumnos.split('\n'))*2
shuffle(tiles)


state = {'mark': None}

#Matriz de estados (hidden or not)
hide = [True] * 64

tapCounter = 0

#Para dibujar el tablero
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'whitesmoke')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Regresa el tile en el que se le esta picando
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Regresa el xy del tile que se le esta picando
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


#Cuando hace click
def tap(x, y):
    global tapCounter
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    tapCounter+=1

    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        #Cuando son diferentes
        state['mark'] = spot
    else:
        #Si si son iguales ya no se esconde
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    global tapCounter
    clear()
    goto(0, 0)
    shape(tec)
    stamp()
    #Se coloca la imagen

    #Se hace la cuadricula
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    #Se escribe lo valido
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 10, y+10)
        color('blue')
        write(tiles[mark], font=('Arial', 15, 'normal'))

    #Para marcar que se gano
    if True not in hide:
        up()
        goto(-80,-210)
        color('blue')
        write('Ganaste!', font = ('Arial',30,'normal'))

    #Dibuja el numero de taps
    up()
    goto(0, 200)
    color('blue')
    write(f"Numero de taps: {tapCounter}", font=('Arial', 14, 'normal'))
    up()
    goto(-210,-215)
    write('Angel Vargas A00829204 / Nicolas Cardenas A01114959',font=('Arial', 10, 'normal'))

    update()
    #Se actualiza cada 100 ms
    ontimer(draw, 100)

#Ventana
setup(450, 450, 370, 0)

#Se carga la imagen
tec = 'TECm.gif'

#Se agrega la imagen
addshape(tec)

#Se esconde la turtle
hideturtle()
tracer(False)

#Cada vez que hay un click se ejecuta  tap
onscreenclick(tap)
draw()
done()