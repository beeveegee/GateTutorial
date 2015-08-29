#GateTutorial
#http://samolds.github.io/gate/guide/python.html#control-flow

#function arguments

import random

def print_random_color(times):
  colors = ["red", "orange", "yellow", "green", "blue", "purple"]
  for i in range(times):
      print random.choice(colors)

print_random_color(5)
