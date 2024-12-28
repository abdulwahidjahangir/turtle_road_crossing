import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        dice = random.randint(1, 6)
        if dice == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            num_x = 300
            nums_y = random.randint(-250, 250)
            car.goto(num_x, nums_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
