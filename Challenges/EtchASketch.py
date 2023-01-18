from turtle import *

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(50)


def move_backwards():
    t.back(50)


def circle_anticlockwise():
    t.circle(50)


def circle_clockwise():
    t.circle(-50)


def clear_drawings():
    t.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=circle_anticlockwise)
screen.onkey(key="d", fun=circle_clockwise)
screen.onkey(key="c", fun=clear_drawings)
screen.exitonclick()