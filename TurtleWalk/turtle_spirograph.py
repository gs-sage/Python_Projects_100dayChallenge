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
tim.speed("fastest")
tim.pensize(2)
turtle.colormode(255)

# creating two loops to have a better effect
for i in range(20):
    tim.color(random_color())
    tim.circle(100)
    tim.left(30)

for i in range(20):
    tim.color(random_color())
    tim.circle(100)
    tim.left(20)


screen.exitonclick()
