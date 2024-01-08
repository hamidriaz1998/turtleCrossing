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

# Player Controls
screen.listen()
screen.onkey(player.up, "Up")
# Game Loop
game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        carManager.createCar()
    carManager.moveCars()
    count += 1

screen.exitonclick()
