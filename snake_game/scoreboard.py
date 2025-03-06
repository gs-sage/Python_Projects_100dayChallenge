from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        #self.write(f"Score : {self.score}", align="center", font=("Arial", 12, "normal")) # moving this to a function since we repeat it
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)


    def score_tracker(self):
        self.clear()
        self.score += 1
        # self.write(f"Score : {self.score}", align="center", font=("Arial", 12, "normal")) moving to a function instead
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)




