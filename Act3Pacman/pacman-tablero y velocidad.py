# Ana Lucia Vea Téllez - A00227499
# Rodrigo Montelongo Pinales - A00827757
# Reflexión - qué aprendieron
# 06/05/2021

# Se hacen los import de todas las librerias
from random import choice
from turtle import *
from freegames import floor, vector

writer = Turtle(visible=False)
# Almacena cantidad de galletas comidas por pacman
state = {'score': 0}

# Hace invisible la -> de turtle, se crean dos objetos de la clase turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)

# Dirección del pacman
aim = vector(5, 0)

# Crea pacman en la posición (-40,-80)
pacman = vector(-40, -80)

# Se crea una lista de listas que posiciona a los fantasmas en las posiciones y direcciones indicadas
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

# En una lista se crea el tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Dibuja un square con su esquina inferior izquierda en (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Retornar True si point es un tile válido, que no tenga alguna pared
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    # Si la celda es 0 return False = Pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    # Si la celda es 0 return False = Pared
    if tiles[index] == 0:
        return False

    # retorna True ?
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    # Recorre toda la lista de (tiles)
    for index in range(len(tiles)):

        # Extrae el valor que existe en la posición index
        tile = tiles[index]

        # Si el valor es 1
        if tile > 0:
            # Calcula la x, y donde se dibuja el square
            x = (index % 20) * 20 - 200 # Si index es (21 % 20) * 20 - 200 = -180
            y = 180 - (index // 20) * 20 # 180 - (21 // 20) * 20 = 160
            square(x, y)                #Dibuja el square(-180,160)

            # Dibuja la galleta sobre el square
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    colores = ['red', 'green', 'pink', 'white']
    "Move pacman and all ghosts."
    writer.undo()
    #writer.write(state['score'])

    valor = state['score']
    writer.write(f'Score: {valor}')
    writer.write(f'Nicolas Cardenas A01114959')
    writer.write(f'Score: {valor}')

    # Limpia la ventana
    clear()

    # Si es una posición valida, quiere decir, no es una pared, pacman.move(aim) en esa dirección
    if valid(pacman + aim):
        pacman.move(aim)

    # Retorna la posición del pacman en el tablero
    index = offset(pacman)

    # 1 - camino
    if tiles[index] == 1:
        # A esa posición se le asigna un 2, para saber que el pacman ya comio su galleta
        tiles[index] = 2
        # Se incrementa el score
        state['score'] += 1
        # Calcula la posición x,y del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        # Para volver a dibujar el square sin la galleta
        square(x, y)

    up()
    # Se va la posición del pacman
    goto(pacman.x + 10, pacman.y + 10)
    # Dibuja el pacman
    dot(20, 'yellow')

    k = 0
    # [vector(-180,160), vector(5,0)]
    for point, course in ghosts:
        # Valida si el fantasma point se puede mover en course
        if valid(point + course):
            point.move(course)
        #Si no se puede mover el fantasma en esa dirección 
        else: 
            #Se actualiza la dirección del movimiento
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            # En plan guarda la nueva dirección del fantasma aleatoriamente de la lista options
            # Aqui se tiene que cambiar para hacer a los fantasmas inteligentes
            # los fantasmas no siempre se moveran porque puede que el nueva choice no es valido            
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        # Levanta el lapiz    
        up()
        # Se mueve a la posición del fantasma
        goto(point.x + 10, point.y + 10)
        # Se dibuja el fantasma de los colores de la lista colores
        dot(20, colores[k])
        k = k + 1

    update()

    # Recorre la lista de fantasmas para ver si coinciden las posiciones del pacman y algun fantasma
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-120,10)
            writer.write('GAME OVER', font = ('Arial',30,'normal'))
            return

    # Vuelve a llamar a move cada 100 milisegundos
    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# El setup inicializa y determina el tamaño de la ventana, alto=420, ancho=420, 
# posición en la que se inicia a dibujar, esquina inferior izquierda 370,0
setup(420, 420, 370, 0)

# Esconde la >
hideturtle()
# Oculta toda la forma de dibujar
tracer(False)
# Mueve la turtle writer a la posición (160,160)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
# Activar el escuchar los elementos del teclado
listen()
# En caso de que el usuario oprima la tecla indicada
# llama a la función change con los argumentos de la nueva dirección del pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
# Llama a la función world(), que crea al tablero
world()
# Llama a la función que move
move()
# Llama a la función para terminar
done()