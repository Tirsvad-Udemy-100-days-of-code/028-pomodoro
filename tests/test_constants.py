"""Tests for the Pomodoro constants."""

import re

import pytest

from pomodoro import constants

HEX_COLOUR = re.compile(r"#[0-9a-f]{6}")


def test_pink_has_course_value() -> None:
    assert constants.PINK == "#e2979c"


def test_red_has_course_value() -> None:
    assert constants.RED == "#e7305b"


def test_green_has_course_value() -> None:
    assert constants.GREEN == "#9bdeac"


def test_yellow_has_course_value() -> None:
    assert constants.YELLOW == "#f7f5dd"


def test_font_name_has_course_value() -> None:
    assert constants.FONT_NAME == "Courier"


def test_work_min_has_course_value() -> None:
    assert constants.WORK_MIN == 25


def test_short_break_min_has_course_value() -> None:
    assert constants.SHORT_BREAK_MIN == 5


def test_long_break_min_has_course_value() -> None:
    assert constants.LONG_BREAK_MIN == 20


@pytest.mark.parametrize(
    "colour",
    [constants.PINK, constants.RED, constants.GREEN, constants.YELLOW],
)
def test_colour_is_seven_char_hex_string(colour: str) -> None:
    assert len(colour) == 7
    assert HEX_COLOUR.fullmatch(colour) is not None


@pytest.mark.parametrize(
    "minutes",
    [constants.WORK_MIN, constants.SHORT_BREAK_MIN, constants.LONG_BREAK_MIN],
)
def test_duration_is_positive_int(minutes: int) -> None:
    assert isinstance(minutes, int)
    assert minutes > 0


def test_long_break_is_longer_than_short_break() -> None:
    assert constants.LONG_BREAK_MIN > constants.SHORT_BREAK_MIN
