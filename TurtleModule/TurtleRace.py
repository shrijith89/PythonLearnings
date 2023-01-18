import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
colors = ["blue", "red", "black", "indigo", "violet", "green"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []
is_on_race = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (blue,red,"
                                                          "black,indigo,violet,green)").lower()
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    all_turtles.append(tim)
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_position[i])

if user_bet:
    is_on_race = True

while is_on_race:
    for turtles in all_turtles:
        turtles.forward(random.randint(1, 50))
        if turtles.xcor() >= 230:
            if turtles.pencolor() == user_bet:
                print("You won")
            else:
                print("You lost")
            is_on_race = False
            break

screen.exitonclick()
