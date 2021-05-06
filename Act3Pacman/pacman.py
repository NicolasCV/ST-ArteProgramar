#Nicolas Cardenas Valdez A01114959
#Angel Ivan Vargas Medina A00829204
#6 de mayo 2021

#Reflexion - Que aprendimos?
#Nicolas:
'''
La parte de hacer mas inteligentes a los pacman fue un poco complicado ya que tuve que primero investigar como hacer uno mas inteligente
Tuve que primero entender el codigo lo cual estuvo tardado pero al final se implemento algo muy simple solo que tuve problema encontrando el angulo
Entre los dos para saber hacia donde deberia moverse el ghost, no fue complicado pero me estaba dando los angulos en radianes y no grados
aprendi a manejar mejor los vectores

#Angel Vargas
Una  parte importante  y escencial fue  entender  el codigo de una mejor manera para no perderse , una vez se logro entender  se realizaron los cambios del tablero
y de la velocidad, cosa que se tuvo que checar bien y mas en el tablero para que quedara  bien acomodado y sea jugable. Por ultimo en clase se agregaron mas funciones las
cuales siento que  implementaron muy bien el juego y lo hicieron mas divertido.
'''
from random import choice
from turtle import *
from freegames import floor, vector
import math

#Almacena el score - cantidad de galletas comidas por pacman
state = {'score': 0}

#Hace invisible la tortuga
path = Turtle(visible=False)
writer = Turtle(visible=False)


aim = vector(5, 0)
pacman = vector(-40, -80)

#Cada uno de los ghosts y su primer movimiento
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]


    




#Crea el tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
]

#Hace un cuadro con su esquina inferior izquierda en (x,y)
def square(x, y):
    #Draw square using path at (x, y).
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    #Return offset of point in tiles.
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    #Return True if point is valid in tiles.
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    #Draw world using path.
    bgcolor('black')
    path.color('blue')

    #Recorre toda la lista de tirles
    for index in range(len(tiles)):
        #Extrae el valor que existe en la posicion index
        tile = tiles[index]

        #Si el valor es 1
        if tile > 0:
            #Cakcyka a x,y donde se dibuja el square
            x = (index % 20) * 20 - 200 #Dibuja
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    #Move pacman and all ghosts.
    writer.undo()
    writer.write(state['score'])

    clear()

    #Si no es una pared pacman se mueve
    if valid(pacman + aim):
        pacman.move(aim)

    #Retorna la posicion del pacman en el tablero
    index = offset(pacman)

    #Camina
    if tiles[index] == 1:
        #A esta posicion se le asigna un 2 para indicar que ya se comio
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    
    #Se va a la posicion del pacman
    goto(pacman.x + 10, pacman.y + 10)

    #Primera vez que dibuja el pacman
    dot(20, 'yellow')

    #Por cada ghosts
    for point, course in ghosts:
        
        #Todo esto es para la interseccion, se usa un diccionario para indicar a que direccion mas facil
        options = {
                'right' : vector(5, 0),
                'left' : vector(-5, 0),
                'up' : vector(0, 5),
                'down' : vector(0, -5),
            }
        optionsL = [vector(5, 0),vector(-5,0),vector(0, 5),vector(0, -5)]

        #Variables para la interseccion
        intersection = False
        goodPaths=[]

        for i in optionsL:
            goodPaths.append(valid(point+i))

        #Si hay mas opciones que dos paths
        if sum(goodPaths) > 2:
            intersection = True
        
        #Cuando esta en una interseccion escoge a donde va a ir
        if intersection:

            #Encontramos el angulo del ghost al pacman en degrees
            dx=pacman.x-point.x
            dy=pacman.y-point.y
            ang = math.degrees(math.atan2(dy, dx))

            #Dependiendo a donde esta es el movimiento que va a escoger, los angulos son partidos como una X y no un MAS porque estorba mas el grid
            if -45 <= ang < 45:
                plan = options['right']
                course.x = plan.x
                course.y = plan.y

            elif 45 <= ang < 135:
                plan = options['up']
                course.x = plan.x
                course.y = plan.y

            elif 135 <= ang < 180 or -135 <= ang <-180:
                plan = options['left']
                course.x = plan.x
                course.y = plan.y

            elif -135 <= ang < -45:
                plan = options['down']
                course.x = plan.x
                course.y = plan.y

        #Si es valido se mueve
        if valid(point + course):
            point.move(course)

        #Si no es valido escogemos una al azar
        else:
            cho = choice(optionsL)
            course.x = cho.x
            course.y = cho.y
            
        up()

        #Se mueve el ghost
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 40)

def change(x, y):
    #Change pacman aim if valid.
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

#Inicializa la ventana ancho y alto 420,420
#0,0 Indica la ubicacion de la esquina superior izquierda de la ventana en mi pantalla
setup(420, 420, 370, 0)

#Esconde la flechita
hideturtle()
tracer(False)

#Mueve la turtle writer a posicion 160,160
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])

listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
