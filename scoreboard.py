from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_increase(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.home()
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=FONT)

