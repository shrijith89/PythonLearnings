import random
import turtle as t
ycordinate = 0
xcordinate = 0

color = [(249, 249, 249), (220, 210, 92), (232, 134, 158), (237, 57, 138), (0, 105, 141), (125, 80, 121), (239, 79, 58), (47, 189, 175), (123, 208, 243), (244, 251, 248), (248, 238, 243), (239, 245, 250), (126, 195, 226), (234, 162, 186), (242, 136, 127), (149, 220, 210), (96, 205, 191), (240, 172, 164), (90, 144, 164)]
screen = t.Screen()
screen.bgcolor("black")

for j in range(7):
    for i in range(10):
        screen.colormode(255)
        t.penup()
        ycordinate = t.ycor()
        t.dot(20, random.choice(color))
        t.forward(50)
    t.setx(xcordinate)
    t.sety(ycordinate + 50)

screen.exitonclick()