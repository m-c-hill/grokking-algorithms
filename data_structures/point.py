import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance_from_origin(self) -> int:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __lt__(self, other):
        return self.distance_from_origin > other.distance_from_origin

    def __gt__(self, other):
        return self.distance_from_origin < other.distance_from_origin

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
