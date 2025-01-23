import turtle
import random

# creating a function that returns random rgb values
def random_color():
    """Returns random RGB values"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g,b)
    return my_color

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen.exitonclick()
