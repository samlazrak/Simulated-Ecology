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
    self.map = [[['.', '.', '.'] for x in range(0, settings.grid_size)] for x in range(0, settings.grid_size)]
    self.grid(self)

    # Iterated through x, y, z and then input in reverse z, y, x into x, y, z to get normal x, y, z coords

  @staticmethod
  def grid(self):
    for x in range(0, settings.grid_size):
      for y in range(0, settings.grid_size):
        self.map[x][y] = (x, y)
      # if settings.multiple_forests is False:
      #   for x in range(0, settings.grid_size - 1):
      #     self.map.pop()
      # elif settings.multiple_forests is True:
      #   for x in range(0, settings.grid_size - settings.number_of_forests):
      #     self.map.pop()

  @staticmethod
  def position_generator():
    x = random.randint(0, settings.grid_size - 1)
    return x

  def populate(self):
    for i in range(0, int(self.tree_count)):
      self.Forest.trees.append(Tree(self.position_generator(), self.position_generator(), i + 1))
    for i in range(0, int(self.lumberjack_count)):
      self.Forest.lumberjacks.append(Lumberjack(self.position_generator(), self.position_generator(), i + 1))
    for i in range(0, int(self.bear_count)):
      self.Forest.bears.append(Bear(self.position_generator(), self.position_generator(), i + 1))

  # def position(self):
  #   # input as y, x, z ( x = y, y = x, z = z ), will fix later.
  #   for i in range(0, len(self.Forest.trees)):
  #     x = self.Forest.trees[i].x
  #     y = self.Forest.trees[i].y
  #     z = self.Forest.trees[i].z
  #     self.map[0][x][y] = (x, y, z)
  #   for i in range(0, len(self.Forest.lumberjacks)):
  #     x = self.Forest.lumberjacks[i].x
  #     y = self.Forest.lumberjacks[i].y
  #     z = self.Forest.lumberjacks[i].z
  #     self.map[0][x][y] = (x, y, z)
  #   for i in range(0, len(self.Forest.bears)):
  #     x = self.Forest.bears[i].x
  #     y = self.Forest.bears[i].y
  #     z = self.Forest.bears[i].z
  #     self.map[0][x][y] = (x, y, z)

  def current_tree(self, x, y):
    tree_id = (self.map[0][x][y])[2]
    tree = self.tree_finder(tree_id)
    return tree

  def tree_finder(self, tree_id):
    for i in range(0, len(self.Forest.trees)):
      if self.Forest.trees[i].z == tree_id:
        print('found it!')
        print(self.Forest.trees[i].__dict__)
        return self.Forest.trees[i]

  def spot_checker(self, tree):
    print(self.map)
    print('dict')
    print(tree.__dict__)
    if tree.x < 9:
      print('right:')
      print(self.map[tree.x + 1][tree.y])
    else:
      print('no right')
      if tree.x > 0:
        print('left:')
        print(self.map[tree.x - 1][tree.y])
      elif tree.x == 0:
        print('no left')
    if tree.y < 9:
      print('above:')
      print(self.map[tree.x][tree.y + 1])
    else:
      print('no above')
      if tree.y > 0:
        print('below:')
        print(self.map[tree.x][tree.y - 1])
      elif tree.y == 0:
        print('no below')

  def spawn_sapling(self, tree, position):
    if tree.spawn(position) is False:
      print('Tree is too young')
    elif tree.spawn(position) is True:
      self.tree_planter(position)

  def tree_planter(self, position):
    self.Forest.trees.append(Tree(position[0], position[1], 1337))
    self.map[0][position[0]][position[1]] = [position[0], position[1], [1337]]
    self.tree_finder(1337)

  def cycle(self):
    time.sleep(1)
    for i in range(0, len(self.Forest.trees)):
      tree = self.Forest.trees[i]
      self.spot_checker(tree)

      # if y >= 1:
      #   tree = self.current_tree(x, y)
      #   print('----')
      #   print('Position to the left of the tree')
      #   print((self.map[0][x][y - 1]))
      #   print((self.map[0][x][y - 1])[2])
      #   if (self.map[0][x][y - 1])[2] == 0:
      #     print('Empty spot!')
      #     print('Trying to spawn a sapling to the left of the tree')
      #     self.spawn_sapling(tree, self.map[0][x][y - 1])
      # if y <= 8:
      #   tree = self.current_tree(x, y)
      #   print('----')
      #   print('Position to the right of the tree')
      #   print(self.map[0][x][y + 1])
      #   print((self.map[0][x][y + 1])[2])
      #   if (self.map[0][x][y + 1])[2] == 0:
      #     print('Empty spot!')
      #     print('Trying to spawn a sapling to the right of the tree')
      #     self.spawn_sapling(tree, self.map[0][x][y + 1])
      # if x >= 1:
      #   tree = self.current_tree(x, y)
      #   print('----')
      #   print('Position below the tree')
      #   print(self.map[0][x - 1][y])
      #   print((self.map[0][x - 1][y])[2])
      #   if (self.map[0][x - 1][y])[2] == 0:
      #     print('Empty spot!')
      #     print('Trying to spawn a sapling below the tree')
      #     self.spawn_sapling(tree, self.map[0][x - 1][y])
      # if x <= 8:
      #   tree = self.current_tree(x, y)
      #   print('----')
      #   print('Position above the tree')
      #   print(self.map[0][x + 1][y])
      #   print((self.map[0][x + 1][y])[2])
      #   if (self.map[0][x + 1][y])[2] == 0:
      #     print('Empty spot!')
      #     print('Trying to spawn a sapling above the tree')
      #     self.spawn_sapling(tree, self.map[0][x + 1][y])
