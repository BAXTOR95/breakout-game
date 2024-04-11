import os
import turtle
import random
from paddle import Paddle
from ball import Ball
from brick import Brick
from dashboard import Dashboard
from timer_manager import Timer
from sound_manager import SoundManager

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BALL_LOST_SOUND = os.path.join(CURRENT_DIRECTORY, "assets", "sounds", "ball_lost.wav")
BRICK_SOUND = os.path.join(CURRENT_DIRECTORY, "assets", "sounds", "brick.wav")
GAME_OVER_SOUND = os.path.join(CURRENT_DIRECTORY, "assets", "sounds", "game_over.wav")
LEVEL_UP_SOUND = os.path.join(CURRENT_DIRECTORY, "assets", "sounds", "levelup.wav")
PADDLE_SOUND = os.path.join(CURRENT_DIRECTORY, "assets", "sounds", "paddle.wav")


class Game:
    """
    Represents the Breakout game.

    Attributes:
    - screen: The turtle screen object.
    - sound_manager: The sound manager object.
    - paddle: The paddle object.
    - ball: The ball object.
    - dashboard: The dashboard object.
    - timer: The timer object.
    - floors: The number of floors in the game.
    - columns: The number of columns in the game.
    - bricks: A list of brick objects.
    - is_running: A boolean indicating if the game is running.
    - paused: A boolean indicating if the game is paused.
    """

    def __init__(self):
        """
        Initializes the Breakout Game.

        This method sets up the game window, initializes the game objects,
        loads the sound manager, sets up the bricks, and sets the initial game state.

        Parameters:
            None

        Returns:
            None
        """
        self.screen = turtle.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # Turn off automatic screen updates

        self.sound_manager = SoundManager()

        self.sound_manager.load_sound("ball_lost", BALL_LOST_SOUND)
        self.sound_manager.load_sound("brick", BRICK_SOUND)
        self.sound_manager.load_sound("game_over", GAME_OVER_SOUND)
        self.sound_manager.load_sound("level_up", LEVEL_UP_SOUND)
        self.sound_manager.load_sound("paddle", PADDLE_SOUND)

        self.paddle = Paddle(self.screen.window_height())
        self.ball = Ball()
        self.dashboard = Dashboard()
        self.timer = Timer(self.dashboard.update_time)

        self.floors = 5
        self.columns = 16

        self.bricks = []
        self.setup_bricks()

        self.is_running = True
        self.paused = False

        self.timer.start()

        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.pause_game, "p")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.exit_game, "q")

    def setup_bricks(self):
        """
        Set up the bricks for the Breakout game.

        This method generates a list of random colors and creates Brick objects
        with the corresponding colors at specific positions on the screen.

        Parameters:
        - self: The Game object.

        Returns:
        - None
        """
        # Generate a list of random colors
        colors = [
            "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
            for _ in range(self.floors)
        ]
        for y in range(self.floors):
            for x in range(self.columns):
                brick = Brick(colors[y], -380 + (x * 50), 250 - (y * 30))
                self.bricks.append(brick)

    def setup_game(self):
        """
        Resets the game by resetting the positions of the paddle, ball, and bricks.
        Also rebinds the keys for controlling the paddle and game actions.
        """
        # Reset paddle and ball positions without clearing the screen
        self.reset_bricks()
        self.paddle.reset()
        self.ball.reset()
        self.dashboard.reset()
        # Rebind keys in case they were cleared
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.pause_game, "p")
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.onkeypress(self.exit_game, "q")

    def reset_bricks(self):
        """
        Resets the bricks in the game by destroying all existing bricks and setting up new ones.
        """
        for brick in self.bricks:
            brick.destroy()
        self.bricks.clear()
        self.setup_bricks()

    def play(self):
        """
        Starts the game and runs the game loop until the game is over or the player chooses to exit.
        The game loop updates the screen, moves the ball, checks for collisions, updates the timer display,
        checks if the game is over, and checks if the game is won. It also handles pausing the game and
        restarting the game after it's over.

        Parameters:
            None

        Returns:
            None
        """
        while self.is_running:
            if not self.paused:
                self.screen.update()
                self.ball.move()
                self.check_collisions()
                self.timer.update_display()
                if self.is_game_over():
                    self.dashboard.update_high_score()
                    self.prompt_restart_game()
                    break
                self.is_game_won()

            self.screen.update()

            # This condition helps exit the loop cleanly if the game is no longer running
            if not self.is_running:
                break

    def check_collisions(self):
        """
        Checks for collisions between the ball and other game objects.

        This method checks for collision between the ball and the paddle, as well as
        collision between the ball and the bricks. It calls the respective collision
        checking methods to handle the collisions.

        Parameters:
            None

        Returns:
            None
        """
        # Check collision with paddle
        self.check_paddle_collision()

        # Check collision with bricks
        self.check_brick_collision()

    def check_paddle_collision(self):
        """
        Check if the ball collides with the paddle and perform necessary actions.

        This method checks if the ball's y-coordinate is within a certain range of the paddle's y-coordinate,
        and if the absolute difference between the ball's x-coordinate and the paddle's x-coordinate is less than 50.
        If the conditions are met, the ball's vertical direction is inverted, and its x direction is adjusted based on
        the difference in x position between the ball and the paddle. Additionally, a sound effect is played.

        Parameters:
            None

        Returns:
            None
        """
        paddle_center_x = self.paddle.get_x()  # Get the paddle"s center x-coordinate
        ball_center_x = self.ball.get_x()  # Get the ball"s center x-coordinate

        if (
            abs(self.ball.get_y() - self.paddle.get_y()) <= 20
            and abs(ball_center_x - paddle_center_x) < 50
        ):
            self.ball.invert_dy()  # Invert ball"s vertical direction
            # Calculate the difference in x position between ball and paddle
            diff = ball_center_x - paddle_center_x
            # Adjust the ball"s x direction based on the difference
            self.ball.adjust_dx(diff)
            self.sound_manager.play_sound("paddle")

    def check_brick_collision(self):
        """
        Checks for collision between the ball and the bricks.
        If a collision is detected, it determines whether it's a horizontal or vertical collision
        and updates the ball's direction accordingly. It also removes the collided brick,
        plays a sound, and updates the score.

        Parameters:
            None

        Returns:
            None
        """
        for brick in self.bricks:
            if (
                abs(self.ball.get_y() - brick.ycor()) < 20
                and abs(self.ball.get_x() - brick.xcor()) < 50
            ):
                # Determine if the collision is more likely horizontal or vertical
                # This simplification assumes that if the ball"s center is vertically aligned within the brick"s bounds,
                # the collision is vertical; otherwise, it"s horizontal.
                if abs(self.ball.get_x() - brick.xcor()) < 25:
                    self.ball.invert_dy()  # Vertical collision
                else:
                    self.ball.invert_dx()  # Horizontal collision

                brick.destroy()  # Remove the brick
                self.bricks.remove(brick)
                self.sound_manager.play_sound("brick")
                self.dashboard.update_score(10)  # Update the score

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        if self.ball.get_y() < -290 and self.dashboard.get_lives() > 0:
            self.dashboard.lose_life()
            self.sound_manager.play_sound("ball_lost")
            self.ball.reset()
            self.paddle.reset()
        elif self.dashboard.get_lives() == 0:
            self.sound_manager.play_sound("game_over")
            print("Game Over!")
            return True
        return False

    def is_game_won(self):
        """
        Checks if the game is won by determining if there are no more bricks left.
        If the game is won, it prints the level that was beaten, levels up the game,
        plays a sound effect, resets the ball, and resets the bricks.
        """
        if len(self.bricks) == 0:
            print(f"You beat level {self.dashboard.get_level()}!")
            self.level_up()
            self.sound_manager.play_sound("level_up")
            self.ball.reset()
            self.reset_bricks()

    def level_up(self):
        """
        Increases the level, ball speed, and number of floors (every 2 levels).
        """
        self.dashboard.next_level()  # Increase the level
        speed_increase = 0.5
        self.ball.increase_speed(speed_increase)  # Increase the ball speed
        # every 2 levels, increase the number of floors by 1
        if self.dashboard.get_level() % 2 == 0:
            self.floors += 1

    def pause_game(self):
        """
        Pauses or resumes the game.

        If the game is currently paused, this method resumes the game by starting the timer.
        If the game is currently running, this method pauses the game by pausing the timer.

        """
        self.paused = not self.paused
        if self.paused:
            self.timer.pause()  # Pause the timer
        else:
            self.timer.start()  # Resume the timer

    def restart_game(self):
        """
        Restarts the game by resetting the timer, re-setting up game elements without clearing the screen,
        and restarting the game loop.
        """
        self.timer.reset()  # Reset the timer
        self.setup_game()  # Re-setup game elements without clearing the screen
        self.timer.start()
        self.play()  # Restart the game loop

    def prompt_restart_game(self):
        """
        Prompts the user to start a new game or exit the current game.

        This method displays a message box to the user asking if they want to start a new game or exit the current game.
        If the user chooses to start a new game, the `restart_game` method is called.
        If the user chooses to exit the game, the `exit_game` method is called.
        """
        # Prompt the user
        restart = self.screen.textinput(
            "Game Over", "Start a new game? (yes/no)"
        ).lower()
        if restart == "yes":
            self.restart_game()
        else:
            self.exit_game()

    def exit_game(self):
        """
        Exits the game by updating the high score and setting the `is_running` flag to False.
        """
        self.dashboard.update_high_score()
        self.is_running = False


# Initialize and run the game
if __name__ == "__main__":
    game = Game()
    game.play()
