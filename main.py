import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize Objects
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

# Player Controls
screen.listen()
screen.onkey(player.up, "Up")
# Game Loop
isGameOn = True
count = 0
while isGameOn:
    time.sleep(0.1)
    screen.update()

    if count % 6 == 0:
        carManager.createCar()
    carManager.moveCars()
    count += 1

    # Check if player has reached the end
    if player.ycor() > 279:
        scoreboard.incrementLevel()
        player.resetPos()

    # Check player collision with a car (game over)
    if any(map(lambda i: player.distance(i) < 20, carManager.allCars)):
        isGameOn = False
        scoreboard.gameOver()


screen.exitonclick()
