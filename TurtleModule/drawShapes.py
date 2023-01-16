import random
import turtle
from turtle import *

t = turtle.Turtle()
screen = Screen()
colors = ["red", "orange red", "crimson", "indigo", "dark slate blue", "blue violet"]


def draw_shape(shapes):
    angle = 360 / shapes
    for _ in range(shapes):
        t.forward(100)
        t.right(angle)


for i in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(i)