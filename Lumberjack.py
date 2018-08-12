class Lumberjack:
  def __init__(self, position, tag):
    self.position = position
    self.lumber = 0
    self.tag: int = tag

  def location(self):
    return self.position

  def chop(self):
    self.lumber = self.lumber + 1
    return self.lumber


