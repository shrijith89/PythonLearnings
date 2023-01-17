import random
import turtle
from turtle import *

colors = ["red", "orange red", "crimson", "indigo", "dark slate blue", "blue violet"]
direction = [90, 180, 270, 360]
screen = Screen()


def walk():
    for _ in range(30):
        turtle.color(random.choice(colors))
        turtle.forward(50)
        turtle.setheading(random.choice(direction))

walk()
screen.exitonclick()