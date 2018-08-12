from Ecology import Ecology
import time

Ecology = Ecology()

def treeAgeTest():
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

def forestStatCheck():
  print(Ecology.Forest.trees[0].__dict__)
  print(Ecology.Forest.lumberjacks[0].__dict__)
  print(Ecology.Forest.bears[0].__dict__)

def test():
  Ecology.populate()
  forestStatCheck()

  for x in range(0, 121):
    treeAgeTest()

test()