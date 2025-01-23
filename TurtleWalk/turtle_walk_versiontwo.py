from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# creating a direction list that will have numbers as East, west, north, south
direction = [0, 90, 180, 270]

# creating turtle object
tim = Turtle()
screen = Screen()

# increasing pen width
tim.pensize(15)

# using loop to run as many times as needed
for i in range(300):
  tim.color(random.choice(colours))
  tim.forward(35)
  tim.setheading(random.choice(direction))

screen.exitonclick()
