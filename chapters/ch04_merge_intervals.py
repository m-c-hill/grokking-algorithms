from typing import List

from data_structures.interval import Interval


# Problem 1 - Merge Intervals
def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    if len(intervals) < 2:
        return intervals

    merged_intervals = []

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals[1:]:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals


# Problem 2 - Insert Interval
def insert_interval(
    intervals: List[Interval], new_interval: Interval
) -> List[Interval]:
    merged = []

    new_interval_start = new_interval.start
    new_interval_end = new_interval.end
    i = 0  # pointer to find position of new interval

    while i < len(intervals) and new_interval_start > intervals[i].end:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and new_interval_end >= intervals[i].start:
        new_interval_start = min(new_interval_start, intervals[i].start)
        new_interval_end = max(new_interval_end, intervals[i].end)
        i += 1

    merged.append(Interval(new_interval_start, new_interval_end))

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


# Problem 3 - Interval Intersection
def intervals_intersection(
    arr1: List[Interval], arr2: List[Interval]
) -> List[Interval]:
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        interval_1 = arr1[i]
        interval_2 = arr2[j]

        if (interval_2.start <= interval_1.start <= interval_2.end) or (
            interval_1.start <= interval_2.start <= interval_1.end
        ):
            start = max(interval_1.start, interval_2.start)
            end = min(interval_1.end, interval_2.end)
            result.append(Interval(start, end))

        if interval_1.end <= interval_2.end:
            i += 1
        else:
            j += 1

    return result


# Problem 4 - Conflicting Appointments
def conflicting_appointments(appointments: List[Interval]) -> bool:
    if len(appointments) <= 1:
        return True

    # Sort by interval start time
    appointments.sort(key=lambda x: x.start)

    for i in range(1, len(appointments)):
        appointment = appointments[i]
        prev_appointment = appointments[i - 1]
        if appointment.start < prev_appointment.end:
            return False

    return True
