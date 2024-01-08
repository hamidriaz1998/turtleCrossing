from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.speed = STARTING_MOVE_DISTANCE

    def createCar(self):
        if random.randint(1, 3) == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.allCars.append(car)

    def moveCars(self):
        for car in self.allCars:
            car.forward(self.speed)

    def increaseSpeed(self):
        self.speed += MOVE_INCREMENT
