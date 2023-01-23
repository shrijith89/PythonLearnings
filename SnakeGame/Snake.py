from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
segments = []
MOVE_DISTANCE = 50


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_body()

    def snake_body(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)