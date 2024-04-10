import turtle


class Paddle:
    def __init__(self, screen_height):
        self.screen_height = screen_height
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)  # Animation speed, 0 is the fastest
        self.paddle.shape("square")
        self.paddle.color("white")
        # Default paddle size is 20x20 in Turtle, stretch to make it paddle-like
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        # Position the paddle at the bottom center of the screen
        self.paddle.goto(0, -screen_height / 2 + 20)
        print('paddle created')

    def move_left(self):
        x = self.paddle.xcor() - 20
        if x < -290:  # TODO: Check to prevent moving beyond the screen's left edge
            x = -290
        self.paddle.setx(x)

    def move_right(self):
        x = self.paddle.xcor() + 20
        if x > 290:  # TODO: Check to prevent moving beyond the screen's right edge
            x = 290
        self.paddle.setx(x)

    def get_x(self):
        return self.paddle.xcor()

    def get_y(self):
        return self.paddle.ycor()

    def reset(self):
        self.paddle.goto(0, -self.screen_height / 2 + 20)
