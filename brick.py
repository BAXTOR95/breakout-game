import turtle


class Brick:
    """
    Represents a brick in the Breakout game.

    Attributes:
        color (str): The color of the brick.
        x (int): The x-coordinate of the brick's position.
        y (int): The y-coordinate of the brick's position.
    """

    def __init__(self, color, x, y):
        """
        Initializes a Brick object.

        Parameters:
        - color (str): The color of the brick.
        - x (int): The x-coordinate of the brick's starting position.
        - y (int): The y-coordinate of the brick's starting position.
        """
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1, stretch_len=2)
        self.brick.penup()
        self.brick.goto(x, y)

    def destroy(self):
        """
        Destroys the brick by moving it off the game screen and hiding it.
        """
        self.brick.goto(2000, 2000)  # Effectively remove the brick from the game screen
        self.brick.hideturtle()

    def ycor(self):
        """Return the y-coordinate of the brick."""
        return self.brick.ycor()

    def xcor(self):
        """
        Returns the x-coordinate of the brick.
        """
        return self.brick.xcor()
