from turtle import Turtle
import random
from scoreboard import Scoreboard

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        # random_x = random.randint(-280,280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        self.refresh()

    # creating a function that creates food at random location and now we can call it inside the initializer instead of the whole random process
    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
        # scoreboard = Scoreboard()
        # scoreboard.score_tracker()
