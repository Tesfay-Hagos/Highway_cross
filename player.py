from turtle import Turtle, Screen

screen = Screen()
class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, -280)
        self.listen_player()

    def listen_player(self):
        screen.listen()
        screen.onkey(self.player_up_move, "Up")

    def player_up_move(self):
        self.setheading(90)
        self.forward(10)



