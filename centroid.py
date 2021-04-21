from Point import Point

def centroid(polygon):
  """
  Calculates the centroid and area of a polygon
  """
  area = 0
  xmean = 0
  ymean = 0

  for i in range(len(polygon))