"""Tests for the Pomodoro timer rules."""

import ast
from pathlib import Path

import pytest

from pomodoro import timer_rules
from pomodoro.constants import CHECK_MARK
from pomodoro.timer_rules import (
    SessionKind,
    check_marks,
    format_time,
    session_kind,
    session_minutes,
)

WORK = SessionKind.WORK
SHORT = SessionKind.SHORT_BREAK
LONG = SessionKind.LONG_BREAK


def test_module_does_not_import_tkinter() -> None:
    tree = ast.parse(Path(timer_rules.__file__).read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported.add(node.module.split(".")[0])
    assert "tkinter" not in imported


def test_session_kind_follows_the_eight_session_order() -> None:
    kinds = [session_kind(reps) for reps in range(1, 9)]
    assert kinds == [WORK, SHORT, WORK, SHORT, WORK, SHORT, WORK, LONG]


@pytest.mark.parametrize(
    ("reps", "expected"),
    [(9, WORK), (10, SHORT), (15, WORK), (16, LONG), (24, LONG)],
)
def test_session_kind_repeats_the_cycle(reps: int, expected: SessionKind) -> None:
    assert session_kind(reps) is expected


@pytest.mark.parametrize("reps", [0, -1])
def test_session_kind_rejects_reps_below_one(reps: int) -> None:
    with pytest.raises(ValueError, match="reps"):
        session_kind(reps)


@pytest.mark.parametrize(("kind", "minutes"), [(WORK, 25), (SHORT, 5), (LONG, 20)])
def test_session_minutes_per_kind(kind: SessionKind, minutes: int) -> None:
    assert session_minutes(kind) == minutes


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [(1500, "25:00"), (245, "4:05"), (0, "0:00"), (59, "0:59"), (1200, "20:00")],
)
def test_format_time(seconds: int, expected: str) -> None:
    assert format_time(seconds) == expected


def test_format_time_rejects_negative_seconds() -> None:
    with pytest.raises(ValueError, match="negative"):
        format_time(-1)


@pytest.mark.parametrize(
    ("reps", "count"), [(1, 0), (2, 1), (3, 1), (4, 2), (7, 3), (8, 4)]
)
def test_check_marks_count_completed_work_sessions(reps: int, count: int) -> None:
    assert check_marks(reps) == CHECK_MARK * count
