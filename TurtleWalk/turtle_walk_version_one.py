import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

def draw_shapes(sides, color):
    angle = 360 / sides
    tim.color(color)
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

def random_steps(turn, color):
    # for j in range(10):
        tim.color(random.choice(color))
        steps = 30
        if turn == "right":
            tim.right(75)
            tim.forward(steps)
            tim.left(75)
            tim.forward(steps)
        elif turn == "left":
            tim.left(45)
            tim.forward(steps)
            tim.right(45)
            tim.forward(steps)
        elif turn == "backward":
            tim.backward(steps)
            tim.forward(steps)
        elif turn == "forward":
            tim.forward(steps)
            tim.backward(steps)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = ["right", "left", "forward", "backward"]

# side = 3
# while side <= 10:
#     draw_shapes(side, random.choice(colours))
#     side += 1

i = 0

while i<10:
    turns = random.choice(direction)
    print(turns)
    random_steps(turns, colours)
    i+=1


screen.exitonclick()
