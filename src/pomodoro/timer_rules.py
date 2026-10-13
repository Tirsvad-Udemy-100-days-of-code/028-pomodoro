"""Pomodoro timer rules.

@brief Pure rules of the session cycle, with no user interface.
"""

import enum

from pomodoro.constants import (
    CHECK_MARK,
    LONG_BREAK_MIN,
    SECONDS_PER_MINUTE,
    SESSIONS_PER_CYCLE,
    SESSIONS_PER_PAIR,
    SHORT_BREAK_MIN,
    WORK_MIN,
)


class SessionKind(enum.Enum):
    """@brief The kinds of session in a Pomodoro cycle."""

    WORK = "work"
    SHORT_BREAK = "short_break"
    LONG_BREAK = "long_break"


_MINUTES: dict[SessionKind, int] = {
    SessionKind.WORK: WORK_MIN,
    SessionKind.SHORT_BREAK: SHORT_BREAK_MIN,
    SessionKind.LONG_BREAK: LONG_BREAK_MIN,
}


def session_kind(reps: int) -> SessionKind:
    """@brief Tell which kind of session a repetition number is.

    @param reps Number of the session, counted from 1 at the first work session.
    @return The kind of that session.
    @throws ValueError When reps is below 1.
    """
    if reps < 1:
        raise ValueError(f"reps must be at least 1, got {reps}")
    if reps % SESSIONS_PER_CYCLE == 0:
        return SessionKind.LONG_BREAK
    if reps % SESSIONS_PER_PAIR == 0:
        return SessionKind.SHORT_BREAK
    return SessionKind.WORK


def session_minutes(kind: SessionKind) -> int:
    """@brief Give the length of a session.

    @param kind Kind of session.
    @return Length in minutes.
    """
    return _MINUTES[kind]


def format_time(total_seconds: int) -> str:
    """@brief Format seconds as minutes and zero-padded seconds, e.g. 4:05.

    @param total_seconds Time in seconds, not negative.
    @return The text "M:SS".
    @throws ValueError When total_seconds is negative.
    """
    if total_seconds < 0:
        raise ValueError(f"total_seconds must not be negative, got {total_seconds}")
    minutes, seconds = divmod(total_seconds, SECONDS_PER_MINUTE)
    return f"{minutes}:{seconds:02d}"


def check_marks(reps: int) -> str:
    """@brief Give one check mark for each completed work session.

    @param reps Number of the session being started.
    @return The check marks as text.
    """
    return CHECK_MARK * (reps // SESSIONS_PER_PAIR)
