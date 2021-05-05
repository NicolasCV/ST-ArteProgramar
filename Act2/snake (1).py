import turtle
from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
rav = vector(0, 0)

#Se escogen los colores para las vibora
colors = ['black','yellow','green','blue','orange']
co = random.choice(colors)

#Se escoge uno nuevo hasta que no sean iguales
while True:
  co2 = random.choice(colors)

  if co2 != co:
    break

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, co)
        

    square(food.x, food.y, 9, co2)
    update()
    ontimer(move, 100)

def moveFood():
    #Random choice para escoger a donde ir
    moves = [(10,0),(-10, 0),(0, 10),(0, -10)]
    ra = random.choice(moves)

    if not inside(food):
        #Si no esta adentro se regresa al centro
        food.x = 0
        food.y = 0

    #Se utiliza uno que no sea el aim para mover el cubo si no se mueven hacia donde mismo
    rav.x = ra[0]
    rav.y = ra[1]

    #Cada segundo se corre
    food.move(rav)
    update()
    ontimer(moveFood, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()