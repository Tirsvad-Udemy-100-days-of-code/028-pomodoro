"""Tests for the Pomodoro window."""

from collections.abc import Callable, Iterator
from typing import TYPE_CHECKING

import pytest

from pomodoro.constants import CHECK_MARK, GREEN, PINK, RED, YELLOW

if TYPE_CHECKING:
    from pomodoro.app import PomodoroApp

SKIP_REASON = "Tkinter or a display is not available"


class FakeScheduler:
    """Records scheduled calls and cancelled ids instead of waiting."""

    def __init__(self) -> None:
        self.scheduled: list[tuple[int, Callable[..., object], tuple[object, ...]]] = []
        self.cancelled: list[str] = []

    def after(self, ms: int, func: Callable[..., object], *args: object) -> str:
        self.scheduled.append((ms, func, args))
        return f"id{len(self.scheduled)}"

    def after_cancel(self, id_: str) -> None:
        self.cancelled.append(id_)

    def fire(self) -> None:
        """Run the most recently scheduled call."""
        _, func, args = self.scheduled[-1]
        func(*args)

    def fire_many(self, times: int) -> None:
        """Run the pending call, and each one it schedules, times in total."""
        for _ in range(times):
            self.fire()


@pytest.fixture
def scheduler() -> FakeScheduler:
    return FakeScheduler()


@pytest.fixture
def clocked_app(scheduler: FakeScheduler) -> Iterator["PomodoroApp"]:
    tk = pytest.importorskip("tkinter", reason=SKIP_REASON)
    from pomodoro.app import PomodoroApp

    try:
        window = tk.Tk()
    except tk.TclError:
        pytest.skip(SKIP_REASON)
    window.withdraw()
    yield PomodoroApp(window, scheduler)
    window.destroy()


def shown_time(app: "PomodoroApp") -> str:
    options = app.canvas.itemconfigure(app.timer_text)
    assert options is not None
    return str(options["text"][-1])


def shown_title(app: "PomodoroApp") -> tuple[str, str]:
    return str(app.title_label.cget("text")), str(app.title_label.cget("fg"))


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


def test_start_shows_work_session(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_timer()
    assert shown_title(clocked_app) == ("Work", GREEN)
    assert shown_time(clocked_app) == "25:00"
    assert clocked_app.reps == 1
    assert len(scheduler.scheduled) == 1
    assert scheduler.scheduled[0][0] == 1000
    assert clocked_app.timer == "id1"


def test_ticking_updates_timer_text(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_timer()
    scheduler.fire()
    assert shown_time(clocked_app) == "24:59"
    scheduler.fire_many(59)
    assert shown_time(clocked_app) == "24:00"


def test_finished_work_session_rolls_on_to_break(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_timer()
    scheduler.fire_many(25 * 60)
    assert clocked_app.reps == 2
    assert shown_title(clocked_app) == ("Break", PINK)
    assert shown_time(clocked_app) == "5:00"
    assert clocked_app.check_label.cget("text") == CHECK_MARK
    assert clocked_app.timer is not None


def test_eight_sessions_follow_the_cycle(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    seen: list[tuple[str, str]] = []
    clocked_app.start_timer()
    for minutes in [25, 5, 25, 5, 25, 5, 25]:
        seen.append(shown_title(clocked_app))
        scheduler.fire_many(minutes * 60)
    seen.append(shown_title(clocked_app))
    assert seen == [
        ("Work", GREEN),
        ("Break", PINK),
        ("Work", GREEN),
        ("Break", PINK),
        ("Work", GREEN),
        ("Break", PINK),
        ("Work", GREEN),
        ("Break", RED),
    ]
    assert clocked_app.reps == 8
    assert shown_time(clocked_app) == "20:00"
    assert clocked_app.check_label.cget("text") == CHECK_MARK * 4


def test_second_start_while_running_is_ignored(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_timer()
    clocked_app.start_timer()
    assert clocked_app.reps == 1
    assert len(scheduler.scheduled) == 1


def test_reset_cancels_and_clears(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_timer()
    scheduler.fire_many(25 * 60)
    pending = clocked_app.timer
    clocked_app.reset_timer()
    assert scheduler.cancelled == [pending]
    assert clocked_app.timer is None
    assert clocked_app.reps == 0
    assert shown_time(clocked_app) == "00:00"
    assert shown_title(clocked_app) == ("Timer", GREEN)
    assert clocked_app.check_label.cget("text") == ""


def test_start_after_reset_begins_new_work_session(
    clocked_app: "PomodoroApp",
) -> None:
    clocked_app.start_timer()
    clocked_app.reset_timer()
    clocked_app.start_timer()
    assert shown_title(clocked_app) == ("Work", GREEN)
    assert shown_time(clocked_app) == "25:00"
    assert clocked_app.reps == 1


def test_reset_without_running_timer_cancels_nothing(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.reset_timer()
    assert scheduler.cancelled == []


def test_buttons_are_wired_to_timer(
    clocked_app: "PomodoroApp", scheduler: FakeScheduler
) -> None:
    clocked_app.start_button.invoke()
    assert clocked_app.reps == 1
    assert shown_time(clocked_app) == "25:00"
    clocked_app.reset_button.invoke()
    assert clocked_app.reps == 0
    assert scheduler.cancelled == ["id1"]


def test_scheduler_defaults_to_window(app: "PomodoroApp") -> None:
    app.start_timer()
    assert app.timer is not None
    app.reset_timer()
    assert app.timer is None
