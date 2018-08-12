class Lumberjack:
  def __init__(self, x, y, z):
    self.x: int = x
    self.y: int = y
    self.z: int = z
    self.lumber = 0

  def location(self):
    return self.position

  def chop(self):
    self.lumber = self.lumber + 1
    return self.lumber


