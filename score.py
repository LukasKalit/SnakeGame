from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            content = int(file.read())
            self.high_score = content
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.speed(0)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()
