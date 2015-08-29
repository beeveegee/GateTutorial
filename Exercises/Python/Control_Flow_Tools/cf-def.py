#GateTutorial
#http://samolds.github.io/gate/guide/python.html#control-flow

#def functions

import random

def print_random_color():
  colors = ["red", "orange", "yellow", "green", "blue", "purple"]
  print random.choice(colors)

for i in range(5):
  print_random_color()
