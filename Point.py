from typing import Literal
from math import sqrt
# TODO remove this when upgrading to Python 3.10+
from __future__ import annotations


class Point():
    """A point in a 2d cartesian coordinate systems."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # TODO: consider adding support for slices as well
    # See https://stackoverflow.com/questions/2936863/implementing-slicing-in-getitem
    def __getitem__(self, i: Literal[0, 1]):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif(type(i) == int):
            # i is an invalid value
            raise IndexError(f'i must be 0 or 1, received {i}')
        else:
            # i is an invalid type
            raise TypeError(
                f'i must be of type int, received {i} of type {type(i)}')

    def __setitem__(self, i: Literal[0, 1], value: float):
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        elif type(i) == int:
            # i is an invalid value
            raise IndexError(f'i must be 0 or 1, received {i}')
        else:
            # i is an invalid type
            raise TypeError(
                f'i must be of type int, received {i} of type {type(i)}')

    def __len__(self):
        return 2

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented

        return self.x == o.x and self.y == o.y

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented

        if self.x < o.x:
            return True
        elif self.x == o.x and self.y < o.y:
            return True
        # self.x > o.x or (self.x == o.x && self.y >= o.y)
        return False

    def __gt__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented

        # self > o iff o < self
        return o < self

    def __ge__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented

        return self > o or self == o

    def __le__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented

        return self < o or self == o

    def __repr__(self):
        return f'{round(self.x, 2)}, {round(self.y, 2)}'

    def distance(self, o: Point):
        return sqrt((self.x - o.x) ** 2 + (self.y - o.y) ** 2)
