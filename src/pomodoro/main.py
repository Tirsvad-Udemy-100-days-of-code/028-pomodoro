"""Entry point.

@brief Composition root of the Pomodoro timer.
"""

from pomodoro.app import PomodoroApp


def main() -> None:
    """@brief Create the Pomodoro window and run it."""
    PomodoroApp().run()
