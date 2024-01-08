from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.printLevel()

    def printLevel(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def gameOver(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
