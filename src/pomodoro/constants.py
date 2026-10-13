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
