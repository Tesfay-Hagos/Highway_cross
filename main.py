import random
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player= Player()

y_pos = []
car_move = []
start_y = -100
number_car = [0, 1, 2, 3, 4]

for _ in range(10):
    y_pos.append(start_y)
    start_y += 100


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for k in range(random.choice(number_car)):
        car_move.append(CarManager(y_pos[k]))
    for car in car_move:
        time.sleep(0.01)
        car.move_car()

