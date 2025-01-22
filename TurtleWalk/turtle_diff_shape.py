# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
import random

def turtle_triangle(color):
    tim.color(color)
    for i in range(3):
        tim.forward(100)
        tim.right(120)

def turtle_square(color):
    tim.color(color)
    for i in range(4):
        tim.forward(100)
        tim.right(90)

def turtle_pentagon(color):
    tim.color(color)
    for i in range(5):
        tim.forward(100)
        tim.right(72)

def turtle_hexagon(color):
    tim.color(color)
    for i in range(6):
        tim.forward(100)
        tim.right(60)

def turtle_heptagon(color):
    tim.color(color)
    for i in range(7):
        tim.forward(100)
        tim.right(51.42)

def turtle_octagon(color):
    tim.color(color)
    for i in range(8):
        tim.forward(100)
        tim.right(45)

def turtle_nonagon(color):
    tim.color(color)
    for i in range(9):
        tim.forward(100)
        tim.right(40)

def turtle_decagon(color):
    tim.color(color)
    for i in range(10):
        tim.forward(100)
        tim.right(36)

def draw_shapes(sides, color):
    angle = 360 / sides
    tim.color(color)
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

tim = Turtle()
screen = Screen()


turtle_color = ["black", "red", "blue", "green", "yellow", "pink"]

# turtle_triangle(random.choice(turtle_color))
# turtle_square(random.choice(turtle_color))
# turtle_pentagon(random.choice(turtle_color))
# turtle_hexagon(random.choice(turtle_color))
# turtle_heptagon(random.choice(turtle_color))
# turtle_octagon(random.choice(turtle_color))
# turtle_nonagon(random.choice(turtle_color))
# turtle_decagon(random.choice(turtle_color))


side = 3
while side <= 10:
    draw_shapes(side, random.choice(turtle_color))
    side += 1


screen.exitonclick()
