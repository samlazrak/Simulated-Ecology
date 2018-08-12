from Ecology import Ecology
import time

Ecology = Ecology()


def tree_age_test():
  time.sleep(1)
  print('--------------------------')
  print('type of tree:')
  print('sapling:')
  print(Ecology.Forest.trees[0].__dict__['sapling'])
  print('tree:')
  print(Ecology.Forest.trees[0].__dict__['tree'])
  print('elder_tree:')
  print(Ecology.Forest.trees[0].__dict__['elder_tree'])
  print('Current age:')
  print(Ecology.Forest.trees[0].__dict__['age'])
  print('aging')
  Ecology.Forest.trees[0].check_age()
  print('new age:')
  print(Ecology.Forest.trees[0].__dict__['age'])


def forest_stat_check():
  print(Ecology.Forest.trees[0].__dict__)
  print(Ecology.Forest.lumberjacks[0].__dict__)
  print(Ecology.Forest.bears[0].__dict__)

def grid_test():
  print(Ecology.map)

def position_test():
  print(Ecology.map)

def test():
  Ecology.populate()
  Ecology.position()

  # grid_test()
  # position_test()
  # forest_stat_check()
  # for x in range(0, 121):
  #   tree_age_test()

test()
