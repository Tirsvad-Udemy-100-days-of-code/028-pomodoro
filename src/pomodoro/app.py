"""Pomodoro window.

@brief Builds the Tkinter user interface of the Pomodoro timer.
"""

import tkinter as tk
from collections.abc import Callable
from pathlib import Path
from typing import Protocol

from pomodoro.constants import (
    BREAK_TITLE,
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    CHECK_FONT_SIZE,
    FONT_NAME,
    GREEN,
    IMAGE_FILE_NAME,
    INITIAL_TIMER_TEXT,
    PINK,
    RED,
    RESET_BUTTON_TEXT,
    SECOND_MS,
    SECONDS_PER_MINUTE,
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
    WORK_TITLE,
    YELLOW,
)
from pomodoro.timer_rules import (
    SessionKind,
    check_marks,
    format_time,
    session_kind,
    session_minutes,
)

IMAGE_PATH = Path(__file__).parent / IMAGE_FILE_NAME

_TITLE_BY_KIND: dict[SessionKind, tuple[str, str]] = {
    SessionKind.WORK: (WORK_TITLE, GREEN),
    SessionKind.SHORT_BREAK: (BREAK_TITLE, PINK),
    SessionKind.LONG_BREAK: (BREAK_TITLE, RED),
}


class Scheduler(Protocol):
    """@brief Port for running a function after a delay; tk.Tk satisfies it."""

    def after(self, ms: int, func: Callable[..., object], *args: object) -> str:
        """@brief Run func with args after ms milliseconds.

        @param ms Delay in milliseconds.
        @param func Function to call.
        @param args Arguments for func.
        @return Identifier of the pending call.
        """
        ...

    def after_cancel(self, id_: str) -> None:
        """@brief Cancel a pending call.

        @param id_ Identifier returned by after.
        """
        ...


class PomodoroApp:
    """@brief The Pomodoro timer window and its widgets."""

    def __init__(
        self, window: tk.Tk | None = None, scheduler: Scheduler | None = None
    ) -> None:
        """@brief Build the user interface.

        @param window Window to build in; a new one is created when None.
        @param scheduler Clock for the countdown; defaults to the window.
        """
        self.window: tk.Tk = window if window is not None else tk.Tk()
        self._scheduler: Scheduler = scheduler if scheduler is not None else self.window
        self.reps: int = 0
        self.timer: str | None = None
        self._configure_window()
        self._build_canvas()
        self._build_labels()
        self._build_buttons()
        self._layout()

    def run(self) -> None:
        """@brief Show the window and block until it is closed."""
        self.window.mainloop()

    def start_timer(self) -> None:
        """@brief Start the next session of the cycle.

        A click while a timer already runs is ignored, which fixes the
        double-click bug of the lecture version (two overlapping countdowns).
        """
        if self.timer is not None:
            return
        self.reps += 1
        kind = session_kind(self.reps)
        title, colour = _TITLE_BY_KIND[kind]
        self.title_label.config(text=title, fg=colour)
        self.check_label.config(text=check_marks(self.reps))
        self.count_down(session_minutes(kind) * SECONDS_PER_MINUTE)

    def count_down(self, count: int) -> None:
        """@brief Show the remaining time and schedule the next tick.

        @param count Remaining seconds of the session.
        """
        self.canvas.itemconfig(self.timer_text, text=format_time(count))
        if count > 0:
            self.timer = self._scheduler.after(SECOND_MS, self.count_down, count - 1)
        else:
            # Cleared first so the guard in start_timer lets the next session in.
            self.timer = None
            self.start_timer()

    def reset_timer(self) -> None:
        """@brief Stop the countdown and return to the initial state."""
        if self.timer is not None:
            self._scheduler.after_cancel(self.timer)
            self.timer = None
        self.canvas.itemconfig(self.timer_text, text=INITIAL_TIMER_TEXT)
        self.title_label.config(text=TITLE_TEXT, fg=GREEN)
        self.check_label.config(text="")
        self.reps = 0

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
        self.start_button = tk.Button(
            self.window,
            text=START_BUTTON_TEXT,
            highlightthickness=0,
            command=self.start_timer,
        )
        self.reset_button = tk.Button(
            self.window,
            text=RESET_BUTTON_TEXT,
            highlightthickness=0,
            command=self.reset_timer,
        )

    def _layout(self) -> None:
        self.title_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1)
        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2)
        self.check_label.grid(row=3, column=1)
