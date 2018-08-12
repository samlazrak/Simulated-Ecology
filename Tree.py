class Tree:
  def __init__(self, position, tag):
    self.position = position
    self.sapling: bool = True
    self.tree: bool = False
    self.elder_tree: bool = False
    self.age = 0
    self.tag: int = tag

  def location(self):
    return self.position

  def check_age(self):
    self.age = self.age + 1
    if self.sapling is True and self.age >= 12:
      self.grow()

    if self.tree is True and self.age >= 120:
      self.grow()

  def grow(self):
    if self.sapling and self.age >= 12:
      self.sapling = False
      self.tree = True

    if self.tree and self.age >= 120:
      self.tree = False
      self.elder_tree = True

  def spawn(self):
    if self.sapling is False and self.tree is True:
      print('I tried to spawn')

    if self.sapling is False and self.elder_tree is True:
      print('I tried to spawn elder style')
