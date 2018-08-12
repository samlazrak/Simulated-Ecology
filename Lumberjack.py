class Lumberjack:
  def __init__(self, position):
    self.position = position
    self.lumber = 0

  def location(self):
    return self.position

  def chop(self):
    self.lumber = self.lumber + 1
    return self.lumber


