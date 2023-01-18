from turtle import Turtle,Screen
import turtle, random

screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 800)
turtle = Turtle()


def snake():
    turtle.penup()
    turtle.fillcolor("white")
    turtle.shape("square")
    turtle.shapesize(0.5, 2)


def food():
    turtle.dot(20, "red")


screen.exitonclick()
