import settings
import time
import random

from Forest import Forest
from Tree import Tree
from Bear import Bear
from Lumberjack import Lumberjack

The_Forest = Forest(settings.grid_size, settings.grid_dimensions)
tree_count = The_Forest.grid_dimensions / 2  # 50%
lumberjack_count = The_Forest.grid_dimensions / 100 * 10 # 10%
bear_count = The_Forest.grid_dimensions / 100 * 2 # 2%

def position_generator():
  x = random.randint(0, settings.grid_dimensions)
  y = random.randint(0, settings.grid_dimensions)
  position = (x, y)
  return position

def populate():
  for x in range(0, int(tree_count)):
    The_Forest.trees.append(Tree(position_generator()))
  for x in range(0, int(lumberjack_count)):
    The_Forest.lumberjacks.append(Lumberjack(position_generator()))
  for x in range(0, int(bear_count)):
    The_Forest.bears.append(Bear(position_generator()))

def test():
  populate()
  print(The_Forest.trees[0].__dict__['position'])
  print(The_Forest.lumberjacks[0].__dict__['position'])
  print(The_Forest.bears[0].__dict__['position'])
  print(The_Forest.lumberjacks[0].__dict__['lumber'])

test()