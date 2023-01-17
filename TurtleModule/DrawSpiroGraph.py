import turtle as trtl

trtl.pensize(2.5)
trtl.speed(10)

for j in range(6):
    for color in ('violet', 'white', 'blue',
                  'green', 'yellow', 'orange',
                  'red'):
        trtl.color(color)
        trtl.circle(80)
        trtl.left(10)
trtl.hideturtle()
