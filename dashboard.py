import turtle


class Dashboard:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.high_score = self.load_high_score()
        self.display = turtle.Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(-380, 260)
        self.update_dashboard()

    def update_dashboard(self):
        self.display.clear()
        self.display.write(
            f"Score: {self.score}  High Score: {self.high_score}  Lives: {self.lives}  Level: {self.level}",
            align="left",
            font=("Courier", 14, "normal"),
        )

    def update_score(self, points):
        self.score += points
        self.update_dashboard()

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            self.update_dashboard()

    def next_level(self):
        self.level += 1
        self.update_dashboard()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.update_dashboard()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))

    def get_lives(self):
        return self.lives

    def get_level(self):
        return self.level
