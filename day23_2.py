import turtle as T

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10 
FINISH_LINE_Y = 260


class Player(T.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def upward(self):
        self.forward(10)
        
    def downward(self):
        self.forward(-10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
    