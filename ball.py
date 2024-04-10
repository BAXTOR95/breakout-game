import turtle


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        # Ball movement speed
        self.ball.dx = 0.2
        self.ball.dy = -0.2

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        # Border checking
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.ball.dx *= -1

        if self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.ball.dx *= -1

    def invert_dy(self):
        self.ball.dy *= -1

    def get_x(self):
        return self.ball.xcor()

    def get_y(self):
        return self.ball.ycor()

    def reset(self):
        self.ball.goto(0, 0)
        self.ball.dx = 0.2
        self.ball.dy = -0.2

    def increase_speed(self, speed):
        if self.ball.dx > 0:
            self.ball.dx += speed
        else:
            self.ball.dx -= speed

        if self.ball.dy > 0:
            self.ball.dy += speed
        else:
            self.ball.dy -= speed
