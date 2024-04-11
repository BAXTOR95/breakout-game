import turtle


class Paddle:
    """
    Represents a paddle in the Breakout game.

    Attributes:
        screen_height (int): The height of the game screen.
        paddle (turtle.Turtle): The turtle object representing the paddle.

    Methods:
        __init__(self, screen_height): Initializes a new instance of the Paddle class.
        move_left(self): Moves the paddle to the left.
        move_right(self): Moves the paddle to the right.
        get_x(self): Returns the x-coordinate of the paddle.
        get_y(self): Returns the y-coordinate of the paddle.
        reset(self): Resets the paddle position to the bottom center of the screen.
    """

    def __init__(self, screen_height):
        """
        Initializes a Paddle object.

        Parameters:
        screen_height (int): The height of the game screen.

        Returns:
        None
        """
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

    def move_left(self):
        """
        Move the paddle to the left by 20 units.

        This method updates the x-coordinate of the paddle's position by subtracting 20 units.
        If the new x-coordinate is less than -320, it is set to -320 to prevent the paddle from going off the screen.

        Parameters:
        None

        Returns:
        None
        """
        x = self.paddle.xcor() - 20
        if x < -320:
            x = -320
        self.paddle.setx(x)

    def move_right(self):
        """
        Move the paddle to the right by 20 units.

        This method updates the x-coordinate of the paddle's position by adding 20 units.
        If the new x-coordinate exceeds the maximum x-coordinate of 320, it is capped at 320.

        Parameters:
        None

        Returns:
        None
        """
        x = self.paddle.xcor() + 20
        if x > 320:
            x = 320
        self.paddle.setx(x)

    def get_x(self):
        """
        Returns the x-coordinate of the paddle.

        Returns:
            float: The x-coordinate of the paddle.
        """
        return self.paddle.xcor()

    def get_y(self):
        """
        Returns the y-coordinate of the paddle.

        Returns:
            float: The y-coordinate of the paddle.
        """
        return self.paddle.ycor()

    def reset(self):
        """
        Resets the position of the paddle to the starting position.
        """
        self.paddle.goto(0, -self.screen_height / 2 + 20)
