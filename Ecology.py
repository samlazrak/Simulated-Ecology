import settings, random

from Forest import Forest
from Tree import Tree
from Bear import Bear
from Lumberjack import Lumberjack

class Ecology:
  def __init__(self):
    self.Forest = Forest(settings.grid_size, settings.grid_dimensions)
    self.tree_count = self.Forest.grid_dimensions / 2  # 50%
    self.lumberjack_count = self.Forest.grid_dimensions / 100 * 10 # 10%
    self.bear_count = self.Forest.grid_dimensions / 100 * 2 # 2%
    self.map = [[[['.','.','.'] for x in range(0, settings.grid_size)]for x in range(0, settings.grid_size)] for x in range(0, settings.grid_size)]
    self.grid(self)

  @staticmethod
  def position_generator():
    x = random.randint(0, settings.grid_size-1)
    return x

  @staticmethod
  def grid(self):
    for x in range(0, settings.grid_size):
      for y in range(0, settings.grid_size):
        for z in range(0, settings.grid_size):
          self.map[x][y][z] = (y, z, x)
    if settings.multiple_forests is False:
      for x in range(0, settings.grid_size-1):
        self.map.pop()
    elif settings.multiple_forests is True:
      for x in range(0, settings.grid_size-settings.number_of_forests):
        self.map.pop()

  def populate(self):
    for x in range(0, int(self.tree_count)):
      self.Forest.trees.append(Tree(self.position_generator(),self.position_generator(), x))
    for x in range(0, int(self.lumberjack_count)):
      self.Forest.lumberjacks.append(Lumberjack(self.position_generator(),self.position_generator(), x))
    for x in range(0, int(self.bear_count)):
      self.Forest.bears.append(Bear(self.position_generator(),self.position_generator(), x))

  def position(self):
    for i in range(0, len(self.Forest.trees)):
      x = self.Forest.trees[i].x
      y = self.Forest.trees[i].y
      z = self.Forest.trees[i].z
      self.map[0][x][y] = (x,y,z)
    for i in range(0, len(self.Forest.lumberjacks)):
      x = self.Forest.lumberjacks[i].x
      y = self.Forest.lumberjacks[i].y
      z = self.Forest.lumberjacks[i].z
      self.map[0][x][y] = (x,y,z)
    for i in range(0, len(self.Forest.bears)):
      x = self.Forest.bears[i].x
      y = self.Forest.bears[i].y
      z = self.Forest.bears[i].z
      self.map[0][x][y] = (x,y,z)

