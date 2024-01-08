from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-200, 260)
        self.printLevel()

    def printLevel(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def incrementLevel(self):
        self.level += 1
        self.printLevel()
