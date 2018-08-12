import settings
import random

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

  @staticmethod
  def position_generator():
    x = random.randint(0, settings.grid_dimensions)
    y = random.randint(0, settings.grid_dimensions)
    position = (x, y)
    return position

  def populate(self):
    for x in range(0, int(self.tree_count)):
      self.Forest.trees.append(Tree(self.position_generator()))
    for x in range(0, int(self.lumberjack_count)):
      self.Forest.lumberjacks.append(Lumberjack(self.position_generator()))
    for x in range(0, int(self.bear_count)):
      self.Forest.bears.append(Bear(self.position_generator()))

