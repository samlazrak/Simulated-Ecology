class Bear:
  def __init__(self, position, tag):
    self.position = position
    self.maulings = 0
    self.tag: int = tag

  def location(self):
    return self.position

  def maul(self):
    self.maulings = self.maulings+1
    return self.maulings


