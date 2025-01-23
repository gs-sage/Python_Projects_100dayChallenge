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

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

tim = turtle.Turtle()
screen = turtle.Screen()
tim.speed("fastest")
turtle.colormode(255)

draw_spirograph(5)

screen.exitonclick()
