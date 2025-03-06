import turtle
from turtle import Turtle

# using tuples
# making this a constant
STARTING_POSITIONS =[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            # moving these to a different function
            # new_turtle = Turtle(shape="square")
            # new_turtle.color("white")
            # new_turtle.penup()
            # new_turtle.goto(position)
            # self.segments.append(new_turtle)
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        """add a new segment to snake"""
        self.add_segment(self.segments[-1].position()) # position is a method from the turtle class

    def move(self):
        # for seg_num in range(start=2, stop=0, step=-1), for understanding purposes this will give an error if we run it

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor() # decreasing 1 from seg_num to get the second from the last value
            # idea is to move each turtle object to the position of the turtle in front of it
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        # now we need to move the first one by certain amount so the others can follow along its coordinates
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

