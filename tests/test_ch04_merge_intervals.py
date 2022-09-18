import pytest

from chapters.ch04_merge_intervals import *
from data_structures.interval import Interval


# Problem 1 - Merge Intervals
@pytest.mark.parametrize(
    "intervals,expected",
    [
        (
            [Interval(1, 4), Interval(2, 5), Interval(7, 9)],
            [Interval(1, 5), Interval(7, 9)],
        ),
        (
            [Interval(6, 7), Interval(2, 4), Interval(5, 9)],
            [Interval(2, 4), Interval(5, 9)],
        ),
        ([Interval(1, 4), Interval(2, 6), Interval(3, 5)], [Interval(1, 6)]),
    ],
)
def test_merge_intervals_func(intervals, expected):
    res = merge_intervals(intervals)
    assert res == expected


# Problem 2 - Insert Interval
@pytest.mark.parametrize(
    "intervals,new_interval,expected",
    [
        (
            [Interval(1, 3), Interval(5, 7), Interval(8, 12)],
            Interval(4, 6),
            [Interval(1, 3), Interval(4, 7), Interval(8, 12)],
        ),
        (
            [Interval(1, 3), Interval(5, 7), Interval(8, 12)],
            Interval(4, 10),
            [Interval(1, 3), Interval(4, 12)],
        ),
        (
            [Interval(2, 3), Interval(5, 7)],
            Interval(1, 4),
            [Interval(1, 4), Interval(5, 7)],
        ),
    ],
)
def test_insert_interval(intervals, new_interval, expected):
    res = insert_interval(intervals, new_interval)
    assert res == expected


# Problem 3 - Intervals Intersection
@pytest.mark.parametrize(
    "arr1,arr2,expected",
    [
        (
            [Interval(1, 3), Interval(5, 6), Interval(7, 9)],
            [Interval(2, 3), Interval(5, 7)],
            [Interval(2, 3), Interval(5, 6), Interval(7, 7)],
        ),
        (
            [Interval(1, 3), Interval(5, 7), Interval(9, 12)],
            [Interval(5, 10)],
            [Interval(5, 7), Interval(9, 10)],
        ),
    ],
)
def test_intervals_intersection(arr1, arr2, expected):
    res = intervals_intersection(arr1, arr2)
    assert res == expected


# Problem 4 - Conflicting Appointments
@pytest.mark.parametrize(
    "appointments,expected",
    [
        ([Interval(1, 4), Interval(2, 5), Interval(7, 9)], False),
        ([Interval(6, 7), Interval(2, 4), Interval(8, 12)], True),
        ([Interval(4, 5), Interval(2, 3), Interval(3, 6)], False),
    ],
)
def test_conflicting_appointments(appointments, expected):
    res = conflicting_appointments(appointments)
    assert res == expected


# Problem 5 - Minimum Meeting Rooms
@pytest.mark.parametrize(
    "meetings,expected",
    [
        ([Interval(1, 4), Interval(2, 5), Interval(7, 9)], 2),
        ([Interval(6, 7), Interval(2, 4), Interval(8, 12)], 1),
        ([Interval(1, 4), Interval(2, 3), Interval(3, 6)], 2),
        ([Interval(4, 5), Interval(2, 3), Interval(2, 4), Interval(3, 5)], 2),
    ],
)
def test_minimum_meeting_rooms(meetings, expected):
    res = minimumum_meeting_rooms(meetings)
    assert res == expected


# Problem 6 - Maximum CPU Load
@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "jobs,expected",
    [
        ([[1, 4, 3], [2, 5, 4], [7, 9, 6]], 7),
        ([[6, 7, 10], [2, 4, 11], [8, 12, 15]], 15),
        ([[1, 4, 2], [2, 4, 1], [3, 6, 5]], 8),
    ],
)
def test_maximum_cpu_load(jobs, expected):
    res = maximum_cpu_load(jobs)
    assert res == expected


# Problem 7 - Employee Free Time
@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "working_hours,expected",
    [
        ([[[1, 3], [5, 6]], [[2, 3], [6, 8]]], [[3, 5]]),
        ([[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]], [[4, 6], [8, 9]]),
        ([[[1, 3]], [[2, 4]], [[3, 5], [7, 9]]], [[5, 7]]),
    ],
)
def test_employee_free_time(working_hours, expected):
    res = employee_free_time(working_hours)
    assert res == expected
