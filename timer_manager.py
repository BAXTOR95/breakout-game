import time


class Timer:
    """
    A class representing a timer.

    Attributes:
        start_time (float): The start time of the timer.
        elapsed_time (float): The elapsed time since the timer started.
        running (bool): Indicates whether the timer is currently running or paused.
        display_update_callback (function): A callback function to update the display with the elapsed time.

    Methods:
        start(): Starts the timer.
        pause(): Pauses the timer.
        reset(): Resets the timer.
        update_display(): Updates the display with the elapsed time.
        get_time(): Returns the elapsed time.
    """

    def __init__(self, display_update_callback):
        """
        Initializes a Timer object.

        Parameters:
        display_update_callback (function): A callback function that will be called to update the display.

        Attributes:
        start_time (float): The time when the timer was started.
        elapsed_time (float): The elapsed time since the timer was started.
        running (bool): Indicates whether the timer is currently running.
        display_update_callback (function): The callback function used to update the display.
        """
        self.start_time = time.time()
        self.elapsed_time = 0
        self.running = False
        self.display_update_callback = display_update_callback

    def start(self):
        """
        Starts the timer if it is not already running.
        """
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def pause(self):
        """
        Pauses the timer if it is currently running.
        """
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        """Resets the timer to its initial state.

        This method sets the start time to the current time,
        sets the elapsed time to 0, and sets the running flag to False.
        """

        self.start_time = time.time()
        self.elapsed_time = 0
        self.running = False

    def update_display(self):
        """
        Updates the display with the elapsed time if the timer is running.
        """
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        self.display_update_callback(self.elapsed_time)

    def get_time(self):
        """
        Returns the elapsed time.
        """
        return self.elapsed_time
