from Point import Point
from math import sqrt

#TODO refactor to use some Segment/Line/Path class instead of two points
def distance_point_line(p: Point, p1: Point, p2: Point) -> float:
  """
  Calculate the distance from p to the line defined by p1, p2. 
  p1 and p2 must be different points.
  """
  if p1 == p2: 
    raise ValueError(f"p1 and p2 must be different Points. received p1: {p1} and p2: {p2}")

  # Find the line ax + by + c = 0 that goes through p1, p2
  a = p1.y - p2.y
  b = p1.x - p2.x
  c = -(a * p1.x + b * p1.y) # Because p1 is on the line, therefore a*p1.x + b*p1.y + c = 0

  return abs(a*p.x + b*p.y + c) / sqrt(a**2 + b**2)