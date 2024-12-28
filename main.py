import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_manger = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.add_car()
    car_manger.move()

    for car in car_manger.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manger.level_up()
        scoreboard.update_level()


screen.exitonclick()
