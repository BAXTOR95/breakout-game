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

        self.is_running = True
        self.paused = False

        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.pause_game, "p")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.exit_game, "q")

    def setup_bricks(self):
        # Placeholder for creating and arranging bricks
        colors = ["red", "orange", "yellow", "green", "blue"]
        for y in range(5):
            for x in range(10):
                brick = Brick(colors[y], -380 + (x * 80), 250 - (y * 30))
                self.bricks.append(brick)

    def setup_game(self):
        # Reset paddle and ball positions without clearing the screen
        self.reset_bricks()
        self.paddle.reset()
        self.ball.reset()
        # Rebind keys in case they were cleared
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.pause_game, "p")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkey(self.exit_game, "Escape")

    def reset_bricks(self):
        for brick in self.bricks:
            brick.destroy()
        self.bricks.clear()
        self.setup_bricks()

    def play(self):
        while self.is_running:
            if not self.paused:
                self.screen.update()
                self.ball.move()
                self.check_collisions()
                if self.is_game_over() or self.is_game_won():
                    break
            self.screen.update()

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

    def is_game_over(self):
        if self.ball.get_y() < -290:

            print('Game Over!')
            return True
        return False

    def is_game_won(self):
        if len(self.bricks) == 0:
            print('You Won!')
            return True
        return False

    def pause_game(self):
        self.paused = not self.paused

    def restart_game(self):
        self.setup_game()  # Re-setup game elements without clearing the screen
        self.play()  # Restart the game loop

    def exit_game(self):
        self.is_running = False
        turtle.bye()


# Initialize and run the game
if __name__ == "__main__":
    game = Game()
    game.play()
