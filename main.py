import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_cars()
    #collission with upper and lower:
    for c in car.all_cars:
        if c.distance(timmy) < 20:
            scoreboard.game_over()
            game_is_on = False

    if timmy.is_win():
        timmy.comeback()
        car.speed_up()
        scoreboard.level_increase()

    screen.update()

screen.exitonclick()
