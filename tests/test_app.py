"""Tests for the Pomodoro window."""

from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from pomodoro.constants import GREEN, YELLOW

if TYPE_CHECKING:
    from pomodoro.app import PomodoroApp

SKIP_REASON = "Tkinter or a display is not available"


@pytest.fixture
def app() -> Iterator["PomodoroApp"]:
    tk = pytest.importorskip("tkinter", reason=SKIP_REASON)
    from pomodoro.app import PomodoroApp

    try:
        window = tk.Tk()
    except tk.TclError:
        pytest.skip(SKIP_REASON)
    window.withdraw()
    yield PomodoroApp(window)
    window.destroy()


def test_window_has_title(app: "PomodoroApp") -> None:
    assert app.window.title() == "Pomodoro"


def test_window_background_is_yellow(app: "PomodoroApp") -> None:
    assert app.window.cget("bg") == YELLOW


def test_timer_text_shows_zero(app: "PomodoroApp") -> None:
    options = app.canvas.itemconfigure(app.timer_text)
    assert options is not None
    assert options["text"][-1] == "00:00"


def test_canvas_has_no_highlight_and_yellow_background(app: "PomodoroApp") -> None:
    assert int(app.canvas.cget("highlightthickness")) == 0
    assert app.canvas.cget("bg") == YELLOW


def test_title_label_is_timer_in_green(app: "PomodoroApp") -> None:
    assert app.title_label.cget("text") == "Timer"
    assert app.title_label.cget("fg") == GREEN


def test_buttons_have_texts(app: "PomodoroApp") -> None:
    assert app.start_button.cget("text") == "Start"
    assert app.reset_button.cget("text") == "Reset"


def test_check_label_is_empty(app: "PomodoroApp") -> None:
    assert app.check_label.cget("text") == ""


def test_widgets_are_placed_on_grid(app: "PomodoroApp") -> None:
    placed = {
        "title": (app.title_label, 0, 1),
        "canvas": (app.canvas, 1, 1),
        "start": (app.start_button, 2, 0),
        "reset": (app.reset_button, 2, 2),
        "check": (app.check_label, 3, 1),
    }
    for widget, row, column in placed.values():
        info = widget.grid_info()
        assert (int(info["row"]), int(info["column"])) == (row, column)


def test_tomato_image_is_kept_on_app(app: "PomodoroApp") -> None:
    assert app.tomato_image.width() == 200


def test_run_enters_main_loop(
    app: "PomodoroApp", monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[str] = []
    monkeypatch.setattr(app.window, "mainloop", lambda: calls.append("mainloop"))
    app.run()
    assert calls == ["mainloop"]
