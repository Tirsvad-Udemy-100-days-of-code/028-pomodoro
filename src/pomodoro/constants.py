"""Constants of the Pomodoro timer.

@brief Colours, font and session lengths from the course starting file.
"""

from typing import Final

PINK: Final[str] = "#e2979c"
"""@brief Pink colour as a hex string."""

RED: Final[str] = "#e7305b"
"""@brief Red colour as a hex string."""

GREEN: Final[str] = "#9bdeac"
"""@brief Green colour as a hex string."""

YELLOW: Final[str] = "#f7f5dd"
"""@brief Yellow colour as a hex string."""

FONT_NAME: Final[str] = "Courier"
"""@brief Font family used for the timer text."""

WORK_MIN: Final[int] = 25
"""@brief Length of a work session in minutes."""

SHORT_BREAK_MIN: Final[int] = 5
"""@brief Length of a short break in minutes."""

LONG_BREAK_MIN: Final[int] = 20
"""@brief Length of a long break in minutes."""

WINDOW_TITLE: Final[str] = "Pomodoro"
"""@brief Title of the main window."""

WINDOW_PADDING_X: Final[int] = 100
"""@brief Horizontal window padding in pixels."""

WINDOW_PADDING_Y: Final[int] = 50
"""@brief Vertical window padding in pixels."""

CANVAS_WIDTH: Final[int] = 200
"""@brief Width of the tomato canvas in pixels."""

CANVAS_HEIGHT: Final[int] = 224
"""@brief Height of the tomato canvas in pixels."""

IMAGE_FILE_NAME: Final[str] = "tomato.png"
"""@brief File name of the tomato image, stored next to the app module."""

TIMER_TEXT_X: Final[int] = 100
"""@brief Horizontal position of the timer text on the canvas."""

TIMER_TEXT_Y: Final[int] = 130
"""@brief Vertical position of the timer text on the canvas."""

TIMER_FONT_SIZE: Final[int] = 35
"""@brief Font size of the timer text."""

TIMER_FONT_WEIGHT: Final[str] = "bold"
"""@brief Font weight of the timer text."""

INITIAL_TIMER_TEXT: Final[str] = "00:00"
"""@brief Timer text shown before a session starts."""

TITLE_TEXT: Final[str] = "Timer"
"""@brief Text of the title label."""

TITLE_FONT_SIZE: Final[int] = 50
"""@brief Font size of the title label."""

START_BUTTON_TEXT: Final[str] = "Start"
"""@brief Text of the start button."""

RESET_BUTTON_TEXT: Final[str] = "Reset"
"""@brief Text of the reset button."""

CHECK_MARK: Final[str] = "✔"
"""@brief Check mark shown for each completed work session."""

CHECK_FONT_SIZE: Final[int] = 20
"""@brief Font size of the check-mark label."""
