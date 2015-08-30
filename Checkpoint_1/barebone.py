#GateTutorial
#http://samolds.github.io/gate/guide/hello_world.html#begin

#barebone.py

import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("Hello, World!")

class SecondPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("New Page!")

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/two', SecondPage),
], debug=True)
