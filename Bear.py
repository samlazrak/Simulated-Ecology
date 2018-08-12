class Bear:
  def __init__(self, x, y, z):
    self.x: int = x
    self.y: int = y
    self.z: int = z
    self.maulings = 0

  def location(self):
    return self.position

  def maul(self):
    self.maulings = self.maulings+1
    return self.maulings


