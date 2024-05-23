import turtle as T

FONT = ("Courier", 24, "normal")


class Scoreboard(T.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level {self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.display_score()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("Game Over...", align="center", font=FONT)
