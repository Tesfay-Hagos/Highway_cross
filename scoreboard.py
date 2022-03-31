from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-300, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game-over", align="center", font=FONT)

