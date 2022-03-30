

from turtle import Turtle
import random


class CarManager(Turtle):

    def __init__(self, new_position):
        super().__init__()
        self.shape("square")
        self.pos_y = new_position
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.colour_list = ["cyan", "purple", "green", "blue", "orange"]
        self.setx(-300)
        self.creat_car()

    def creat_car(self,):
        self.sety(self.pos_y)
        self.color(random.choice(self.colour_list))

    def move_car(self):
        new_x = self.xcor() + 30
        ycor = self.ycor()
        self.goto(new_x, ycor)