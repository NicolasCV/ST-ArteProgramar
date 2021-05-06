from turtle import *
import turtle
from freegames import vector
import math


#La funcion para crear una linea
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Funcion para un cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Nuestra funcion para crear un circulo
def circle(start, end):
    "Draw circle from start to end."
    #PM = punto medio entre los puntos
    pmx=(start.x+end.x)/2
    pmy=(start.y+end.y)/2
    turtle.penup()
    turtle.setpos(start.x,start.y)
    turtle.pendown()
    ang = turtle.towards(end.x,end.y)
    turtle.setheading(ang)
    rad = math.hypot(abs(pmx-start.x),abs(pmy-start.y))
    
    begin_fill()
    turtle.circle(rad)
    end_fill()

    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    turtle.penup()
    turtle.setpos(start.x,start.y)
    turtle.pendown()
    begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    end_fill()
    pass  # TODO

#Funcion para crear un triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    turtle.penup()
    turtle.goto(start)
    begin_fill()
    turtle.pendown()
    turtle.goto(end)
    turtle.goto(start.x,end.y)
    turtle.goto(start)
    end_fill()
    pass  # TODO

#Nuestra funcion para marcar los vectores de inicio y final y saber que figura hacer
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Nuestra funcion para definir cual shape vamos a realizar
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

#Anadir color
onkey(lambda: color('yellow'), 'y')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
