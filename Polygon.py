
from typing import List
from Point import Point


class Polygon():
    def __init__(self, vertices: List[Point] = []):
        self.vertices = vertices

    def __getitem__(self, i: int):
        return self.vertices[i]

    def __setitem__(self, i: int, value: Point):
        self.vertices[i] = value

    def __len__(self):
        return len(self.vertices)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Polygon):
            return NotImplemented

        return self.vertices == o.vertices

    def ___repr__(self):
        vertices = list(map(repr, self.vertices))
        return f'Polygon({", ".join(vertices)})'

    def ___str__(self):
        vertices = list(map(str, self.vertices))
        return f'Polygon({", ".join(vertices)})'

    def area(self):
      """Calculates the area of a polygon"""
      area = 0
      for i in range(len(self) - 1):
        v1, v2 = self[i], self[i+1]
        ai = v1.x * v2.y - v2.x * v1.y
        area += ai
      
      area /= 2
      return area

    def centroid(self):
        """Calculates the centroid of a polygon"""
        xmean = 0
        ymean = 0

        for i in range(len(self) - 1):
          v1, v2 = self[i], self[i+1]
          ai = v1.x * v2.y - v2.x * v1.y
          xmean += 

