import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # Turn off automatic screen updates

        self.paddle = Paddle(self.screen.window_height())
        self.ball = Ball()

        self.bricks = []
        self.setup_bricks()

        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")

    def setup_bricks(self):
        # Placeholder for creating and arranging bricks
        colors = ["red", "orange", "yellow", "green", "blue"]
        for y in range(5):
            for x in range(10):
                brick = Brick(colors[y], -380 + (x * 80), 250 - (y * 30))
                self.bricks.append(brick)

    def play(self):
        while True:
            self.screen.update()
            self.ball.move()
            self.check_collisions()
            if self.is_game_over():
                break
            if self.is_game_won():
                break
            # TODO: Implement a way to pause the game
            # TODO: Implement a way to restart the game
            # TODO: Implement a way to exit the game
            # TODO: Implement a way to display the score
            # TODO: Implement a way to display the level and level up
            # TODO: Implement a way to display the lives
            # TODO: Implement a way to display the time
            # TODO: Implement a way to display the high score
            # TODO: Add Visual & Sound Effects

    def check_collisions(self):
        # Check collision with paddle
        if (
            abs(self.ball.get_y() - self.paddle.get_y()) <= 20
            and abs(self.ball.get_x() - self.paddle.get_x()) < 50
        ):
            self.ball.invert_dy()  # Invert ball's vertical direction

        # Check collision with bricks
        for brick in self.bricks:
            # Check if ball is within vertical and horizontal bounds of the brick
            if (
                abs(self.ball.get_y() - brick.ycor()) < 10
                and abs(self.ball.get_x() - brick.xcor()) < 50
            ):
                self.ball.invert_dy()  # Invert ball's vertical direction
                brick.destroy()  # Remove the brick
                self.bricks.remove(brick)

    def reset_bricks(self):
        for brick in self.bricks:
            brick.destroy()
        self.bricks.clear()
        self.setup_bricks()

    def is_game_over(self):
        if self.ball.get_y() < -290:
            self.ball.reset()
            self.reset_bricks()
            print('Game Over!')
            return True
        return False

    def is_game_won(self):
        if len(self.bricks) == 0:
            print('You Won!')
            return True
        return False


# Initialize and run the game
if __name__ == "__main__":
    game = Game()
    game.play()
