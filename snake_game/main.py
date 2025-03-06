import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")



# moved this part to the snake class
# using tuples
# starting_positions =[(0,0), (-20,0), (-40,0)]
# segments = []

# for position in starting_positions:
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(position)
#     segments.append(new_turtle)


game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    #if snake.segments[0].distance(food) < 15: # did this to understand that I could use the segment[0] index itself
    if snake.head.distance(food) < 15: # we defined the snake.head = self.segments[0] in the snake class
        score_board.score_tracker() # calling the score tracker here to increase count
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    # if head collides with any segment in the tail, we trigger game over segment

    # for segment in snake.segments: # using slice technique in python instead of this
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()

    # using slice to break the list into parts
    # starting with 1 as the first one needs to be separated for this to work and including the rest
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()




# moved this part to the snake file
    # # for seg_num in range(start=2, stop=0, step=-1), for understanding purposes this will give an error if we run it
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor() # decreasing 1 from seg_num to get the second from the last value
    #     # idea is to move each turtle object to the position of the turtle in front of it
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(x=new_x, y=new_y)
    #
    # # now we need to move the first one by certain amount so the others can follow along its coordinates
    # segments[0].forward(20)
    # segments[0].left(90)








screen.exitonclick()
