import turtle

BALL_SPEED = 2.0


class Ball:
    """
    A class representing a ball in a breakout game.

    Attributes:
        ball (turtle.Turtle): The turtle object representing the ball.
        dx (int): The horizontal movement speed of the ball.
        dy (int): The vertical movement speed of the ball.

    Methods:
        __init__(): Initializes the Ball object.
        move(): Moves the ball based on its current speed.
        invert_dx(): Inverts the horizontal movement direction of the ball.
        invert_dy(): Inverts the vertical movement direction of the ball.
        get_x(): Returns the x-coordinate of the ball.
        get_y(): Returns the y-coordinate of the ball.
        reset(): Resets the ball to its initial position and speed.
        increase_speed(speed): Increases the speed of the ball by the given amount.
        adjust_dx(difference): Adjusts the horizontal movement speed of the ball based on the paddle collision.
    """

    def __init__(self):
        """
        Initializes a new instance of the Ball class.

        The Ball class represents the game ball in the Breakout game.

        Attributes:
        - ball: A turtle object representing the ball.
        - dx: The horizontal movement speed of the ball.
        - dy: The vertical movement speed of the ball.
        """
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        # Ball movement speed
        self.ball.dx = BALL_SPEED
        self.ball.dy = -BALL_SPEED

    def move(self):
        """
        Move the ball based on its current velocity.

        This method updates the position of the ball by adding the current velocity
        values to its x and y coordinates. It also performs border checking to ensure
        that the ball stays within the game window.

        Returns:
            None
        """
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

    def invert_dx(self):
        """
        Inverts the horizontal velocity of the ball.
        """
        self.ball.dx *= -1

    def invert_dy(self):
        """
        Inverts the dy (vertical) velocity of the ball.
        """
        self.ball.dy *= -1

    def get_x(self):
        """
        Returns the x-coordinate of the ball's current position.

        Returns:
            float: The x-coordinate of the ball's current position.
        """
        return self.ball.xcor()

    def get_y(self):
        """
        Returns the y-coordinate of the ball.

        Returns:
            float: The y-coordinate of the ball.
        """
        return self.ball.ycor()

    def reset(self):
        """
        Resets the ball's position and velocity.

        This method moves the ball to the center of the screen and sets its
        horizontal velocity to `BALL_SPEED` and vertical velocity to `-BALL_SPEED`.
        """
        self.ball.goto(0, 0)
        self.ball.dx = BALL_SPEED
        self.ball.dy = -BALL_SPEED

    def increase_speed(self, speed):
        """
        Increases the speed of the ball in both the x and y directions.

        Args:
            speed (float): The amount by which to increase the speed.

        """
        if self.ball.dx > 0:
            self.ball.dx += speed
        else:
            self.ball.dx -= speed

        if self.ball.dy > 0:
            self.ball.dy += speed
        else:
            self.ball.dy -= speed

    def adjust_dx(self, difference):
        """
        Adjusts the horizontal velocity of the ball based on the difference between the ball's position and the paddle's position.

        Args:
            difference (float): The difference between the ball's position and the paddle's position. Positive values indicate that the ball hit the paddle on the right side, while negative values indicate that the ball hit the paddle on the left side.

        Returns:
            None
        """
        # 'difference' can be positive or negative based on where the ball hits the paddle
        # This adjustment factor controls how much the ball's direction changes
        adjustment_factor = 0.1
        self.ball.dx += difference * adjustment_factor
        # Limit the dx to prevent the ball from moving too horizontally
        max_dx = BALL_SPEED * 2
        if self.ball.dx > max_dx:
            self.ball.dx = max_dx
        elif self.ball.dx < -max_dx:
            self.ball.dx = -max_dx
