class Tree:
  def __init__(self, x, y, z):
    self.x: int = x
    self.y: int = y
    self.z: int = z
    self.sapling: bool = True
    self.tree: bool = False
    self.elder_tree: bool = False
    self.age = 0
    self.alive: bool = True

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

  def spawn(self, position):
    print(position)

    if self.sapling is True and self.tree is False:
      return False
    elif self.sapling is False and self.tree is True:
      return True
    elif self.sapling is False and self.elder_tree is True:
      return True

  def kill(self):
    self.alive = False
    self.x = None
    self.y = None
    self.z = None
