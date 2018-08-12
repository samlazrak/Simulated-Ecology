class Tree():
  def __init__(self, position):
    self.position = (position)
    self.sapling: bool = True
    self.tree: bool = False
    self.elder_tree: bool = False
    self.age = 0

  def location(self):
    return self.position

  def check_age(self):
    self.age = self.age + 1
    if self.sapling == True and self.age >= 12:
      self.grow()

    if self.tree == True and self.age >= 120:
      self.grow()

  def grow(self):
    if self.sapling:
      self.sapling = False
      self.tree = True
      self.age = 0

    if self.tree:
      self.tree = False
      self.elder_tree = True

  def spawn(self):
    if self.sapling == False and self.tree == True:
      print('I tried to spawn')

    if self.sapling == False and self.elder_tree == True:
      print('I tried to spawn elder style')