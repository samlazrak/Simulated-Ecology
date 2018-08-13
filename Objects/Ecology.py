import random
import time

from Config import settings
from Objects.Bear import Bear
from Objects.Forest import Forest
from Objects.Lumberjack import Lumberjack
from Objects.Tree import Tree


class Ecology:
  def __init__(self):
    self.Forest = Forest(settings.grid_size, settings.grid_dimensions)
    self.tree_count = self.Forest.grid_dimensions / 2  # 50%
    self.lumberjack_count = self.Forest.grid_dimensions / 100 * 10  # 10%
    self.bear_count = self.Forest.grid_dimensions / 100 * 2  # 2%
    self.map = [[[['.', '.', '.'] for x in range(0, settings.grid_size)] for x in range(0, settings.grid_size)] for x in
                range(0, settings.grid_size)]
    self.grid(self)

  @staticmethod
  def position_generator():
    x = random.randint(0, settings.grid_size - 1)
    return x

  # Iterated through x, y, z and then input in reverse z, y, x into x, y, z to get normal x, y, z coords
  @staticmethod
  def grid(self):
    for x in range(0, settings.grid_size):
      for y in range(0, settings.grid_size):
        for z in range(0, settings.grid_size):
          self.map[x][y][z] = (z, y, x)
    if settings.multiple_forests is False:
      for x in range(0, settings.grid_size - 1):
        self.map.pop()
    elif settings.multiple_forests is True:
      for x in range(0, settings.grid_size - settings.number_of_forests):
        self.map.pop()

  def populate(self):
    for i in range(0, int(self.tree_count)):
      self.Forest.trees.append(Tree(self.position_generator(), self.position_generator(), i))
    for i in range(0, int(self.lumberjack_count)):
      self.Forest.lumberjacks.append(Lumberjack(self.position_generator(), self.position_generator(), i))
    for i in range(0, int(self.bear_count)):
      self.Forest.bears.append(Bear(self.position_generator(), self.position_generator(), i))

  def position(self):
    # input as y, x, z ( x = y, y = x, z = z ), will fix later.
    for i in range(0, len(self.Forest.trees)):
      x = self.Forest.trees[i].x
      y = self.Forest.trees[i].y
      z = self.Forest.trees[i].z
      self.map[0][x][y] = (y, x, z)
    for i in range(0, len(self.Forest.lumberjacks)):
      x = self.Forest.lumberjacks[i].x
      y = self.Forest.lumberjacks[i].y
      z = self.Forest.lumberjacks[i].z
      self.map[0][x][y] = (y, x, z)
    for i in range(0, len(self.Forest.bears)):
      x = self.Forest.bears[i].x
      y = self.Forest.bears[i].y
      z = self.Forest.bears[i].z
      self.map[0][x][y] = (y, x, z)

  def cycle(self):
    time.sleep(1)
    for i in range(0, 1):
      print(self.map)
      x = self.Forest.trees[i].x
      y = self.Forest.trees[i].y
      z = self.Forest.trees[i].z
      self.Forest.trees[i].check_age()

      # Needs correction, x is y and y is x
      print('space of the tree')
      print(self.map[0][x][y])
      if y >= 1:
        print('space to the left of tree')
        print(self.map[0][x][y - 1])
      if y <= 8:
        print('space to the right of tree')
        print(self.map[0][x][y + 1])
      if x >= 1:
        print('space to the above of tree')
        print(self.map[0][x + 1][y])
      if x <= 8:
        print('space to the below of tree')
        print(self.map[0][x - 1][y])
