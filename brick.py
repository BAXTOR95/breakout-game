import turtle


class Brick:
    def __init__(self, color, x, y):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1, stretch_len=2)
        self.brick.penup()
        self.brick.goto(x, y)
        self.brick.dy = (
            -0.2
        )  # TODO: Add some special effects, like falling bricks or something

    def destroy(self):
        self.brick.goto(2000, 2000)  # Effectively remove the brick from the game screen
        self.brick.hideturtle()

    def ycor(self):
        return self.brick.ycor()

    def xcor(self):
        return self.brick.xcor()