from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
           self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.create_board()

    def create_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.create_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="high_score.txt", mode="w") as file:
                file.write(str(self.high_score))


        self.score = 0
        self.create_board()

    # def game_over(self):
    #    self.goto(x=0, y=0)
    #    self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
