#GateTutorial
#http://samolds.github.io/gate/guide/python.html#scope

#visibility

x = "Hello, World!" #global variable

def local_one():
  y = "Hello locals."
  print x #global variables are visible here

def local_two():
  z = "Howdy folks."
  print z #printed from the same scope z was declared

print x 
print y #error! local_one() scope has ended, along with y
