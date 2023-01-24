import random
import time
import turtle
from turtle import Screen
from Snake import *

game_is_on = True
screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 800)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


def food():
    turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
    turtle.dot(20, "red")


Snake.snake_body()
Snake.move()
screen.exitonclick()
