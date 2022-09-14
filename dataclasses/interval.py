class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"Interval(start={self.start}, end={self.end})"

    def __str__(self) -> str:
        return f"[{self.start}, {self.end}]"

    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end

    def convert_to_int_array(self) -> list:
        return [self.start, self.end]

    def __lt__(self, other) -> bool:
        return self.end < other.end
