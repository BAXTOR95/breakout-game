import turtle


class Dashboard:
    """
    The Dashboard class represents the game dashboard that displays the score, lives, level, and high score.

    Attributes:
        score (int): The current score of the player.
        lives (int): The number of lives remaining.
        max_lives (int): The maximum number of lives the player can have.
        level (int): The current level of the game.
        high_score (int): The highest score achieved.
        display (turtle.Turtle): The turtle object used to display the dashboard.

    Methods:
        __init__(): Initializes the Dashboard object.
        update_dashboard(): Updates the dashboard display.
        update_score(points): Updates the score and updates the dashboard display.
        lose_life(): Decreases the number of lives by 1 and updates the dashboard display.
        next_level(): Increases the level by 1 and updates the dashboard display.
        reset(): Resets the score, lives, and level to their initial values and updates the dashboard display.
        load_high_score(): Loads the high score from a file.
        update_high_score(): Updates the high score if the current score is higher and saves it to a file.
        update_time(elapsed_time): Updates the dashboard display with the current time.
        get_lives(): Returns the number of lives.
        get_lives_formatted(): Returns a formatted string representing the lives using heart emojis.
        get_level(): Returns the current level.
    """

    def __init__(self):
        """
        Initializes the Dashboard object.

        The Dashboard object keeps track of the score, lives, level, and high score in the Breakout game.
        It also initializes a turtle object for displaying the dashboard on the screen.

        Parameters:
            None

        Returns:
            None
        """
        self.score = 0
        self.lives = 3
        self.max_lives = 3
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
        """
        Updates the dashboard display with the current score, high score, lives, and level.
        """
        self.display.clear()
        hearts = self.get_lives_formatted()
        self.display.write(
            f"Score: {self.score}  High Score: {self.high_score}  Lives: {hearts}  Level: {self.level}",
            align="left",
            font=("Courier", 14, "normal"),
        )

    def update_score(self, points):
        """
        Updates the score by adding the given points.

        Args:
            points (int): The number of points to add to the score.

        Returns:
            None
        """
        self.score += points
        self.update_dashboard()

    def lose_life(self):
        """
        Decreases the number of lives by 1 and updates the dashboard.

        If the number of lives is greater than 0, it subtracts 1 from the current
        number of lives and calls the `update_dashboard` method to update the
        dashboard display.

        """
        if self.lives > 0:
            self.lives -= 1
            self.update_dashboard()

    def next_level(self):
        """
        Increases the level by 1 and updates the dashboard.
        """
        self.level += 1
        self.update_dashboard()

    def reset(self):
        """
        Resets the game state.

        This method sets the score, lives, and level back to their initial values.
        It also updates the dashboard to reflect the new game state.
        """
        self.score = 0
        self.lives = 3
        self.level = 1
        self.update_dashboard()

    def load_high_score(self):
        """
        Load the high score from the 'highscore.txt' file.

        Returns:
            int: The high score loaded from the file. If the file doesn't exist, returns 0.
        """
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def update_high_score(self):
        """
        Updates the high score if the current score is higher.
        Writes the updated high score to a file named 'highscore.txt'.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.high_score))

    def update_time(self, elapsed_time):
        """
        Updates the time displayed on the dashboard.

        Args:
            elapsed_time (float): The elapsed time in seconds.

        Returns:
            None
        """
        # Convert seconds to minutes:seconds format
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        hearts = self.get_lives_formatted()
        self.display.clear()
        self.display.write(
            f"Score: {self.score}  High Score: {self.high_score}  Lives: {hearts}  Level: {self.level}  Time: {minutes:02d}:{seconds:02d}",
            align="left",
            font=("Courier", 14, "normal"),
        )

    def get_lives(self):
        """
        Returns the number of lives remaining.

        Returns:
            int: The number of lives remaining.
        """
        return self.lives

    def get_lives_formatted(self):
        """
        Returns a formatted string representing the player's remaining lives.

        The formatted string consists of filled hearts ('🖤') representing the remaining lives,
        followed by empty hearts ('💔') representing the remaining empty lives.

        Returns:
            str: A formatted string representing the player's remaining lives.
        """
        return '🖤' * self.lives + '💔' * (
            self.max_lives - self.lives
        )  # Combine filled and empty hearts

    def get_level(self):
        """
        Returns the current level of the game.

        Returns:
            int: The current level of the game.
        """
        return self.level
