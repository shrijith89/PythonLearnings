from random import randrange, random
import random, turtle
from turtle import *


def color():
    screen.colormode(255)
    rand_color = [randrange(255), randrange(255), randrange(255)]
    return rand_color


direction = [90, 180, 270, 360]
screen = Screen()


def walk():
    for _ in range(30):
        turtle.color(color())
        turtle.forward(50)
        turtle.setheading(random.choice(direction))


walk()
screen.exitonclick()