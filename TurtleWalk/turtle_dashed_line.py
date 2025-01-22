from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# draw a triangle
# for i in range(3):
#     tim.forward(100)
#     tim.left(120)

# my version i came on the fly
# for k in range(15):
#     tim.pencolor("black")
#     for i in range(5):
#         tim.forward(10)
#         tim.pencolor("white")

# i can simplify this by removing the inner loop

for k in range(15):
    tim.pencolor("black")
    tim.forward(10)
    tim.pencolor("white")
    tim.forward(10)

screen.exitonclick()

