from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.right(270)
        self.comeback()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        #self.forward(MOVE_DISTANCE)

    def comeback(self):
        self.goto(STARTING_POSITION)

    def is_win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


