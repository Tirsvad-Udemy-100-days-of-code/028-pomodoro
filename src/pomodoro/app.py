"""Pomodoro window.

@brief Builds the Tkinter user interface of the Pomodoro timer.
"""

import tkinter as tk
from pathlib import Path

from pomodoro.constants import (
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    CHECK_FONT_SIZE,
    FONT_NAME,
    GREEN,
    IMAGE_FILE_NAME,
    INITIAL_TIMER_TEXT,
    RESET_BUTTON_TEXT,
    START_BUTTON_TEXT,
    TIMER_FONT_SIZE,
    TIMER_FONT_WEIGHT,
    TIMER_TEXT_X,
    TIMER_TEXT_Y,
    TITLE_FONT_SIZE,
    TITLE_TEXT,
    WINDOW_PADDING_X,
    WINDOW_PADDING_Y,
    WINDOW_TITLE,
    YELLOW,
)

IMAGE_PATH = Path(__file__).parent / IMAGE_FILE_NAME


class PomodoroApp:
    """@brief The Pomodoro timer window and its widgets."""

    def __init__(self, window: tk.Tk | None = None) -> None:
        """@brief Build the user interface.

        @param window Window to build in; a new one is created when None.
        """
        self.window: tk.Tk = window if window is not None else tk.Tk()
        self._configure_window()
        self._build_canvas()
        self._build_labels()
        self._build_buttons()
        self._layout()

    def run(self) -> None:
        """@brief Show the window and block until it is closed."""
        self.window.mainloop()

    def _configure_window(self) -> None:
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, bg=YELLOW)

    def _build_canvas(self) -> None:
        self.canvas = tk.Canvas(
            self.window,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=YELLOW,
            highlightthickness=0,
        )
        # Kept on self: Tkinter does not hold a reference to the image.
        self.tomato_image = tk.PhotoImage(file=str(IMAGE_PATH))
        self.canvas.create_image(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.tomato_image
        )
        self.timer_text: int = self.canvas.create_text(
            TIMER_TEXT_X,
            TIMER_TEXT_Y,
            text=INITIAL_TIMER_TEXT,
            fill="white",
            font=(FONT_NAME, TIMER_FONT_SIZE, TIMER_FONT_WEIGHT),
        )

    def _build_labels(self) -> None:
        self.title_label = tk.Label(
            self.window,
            text=TITLE_TEXT,
            fg=GREEN,
            bg=YELLOW,
            font=(FONT_NAME, TITLE_FONT_SIZE),
        )
        self.check_label = tk.Label(
            self.window,
            text="",
            fg=GREEN,
            bg=YELLOW,
            font=(FONT_NAME, CHECK_FONT_SIZE),
        )

    def _build_buttons(self) -> None:
        # The commands are wired in a later milestone.
        self.start_button = tk.Button(
            self.window, text=START_BUTTON_TEXT, highlightthickness=0
        )
        self.reset_button = tk.Button(
            self.window, text=RESET_BUTTON_TEXT, highlightthickness=0
        )

    def _layout(self) -> None:
        self.title_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.check_label.grid(row=3, column=1)
