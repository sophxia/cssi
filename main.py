import jinja2
import os
import webapp2
from google.appengine.api import images
from google.appengine.ext import ndb

env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())

class FormHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('form.html')
        self.response.write(template.render())
    def post(self):
        print "Yay"
        num_people = int(self.request.get("num_people"))
        toppings = self.request.get("toppings")
        location = self.request.get("location")
        email = self.request.get("email")
        c = Customer(num_people=num_people, toppings=toppings, location=location, email=email)
        for temp in Customer.query().fetch():
            if c.email == temp.email:
                temp.key.delete()
        for temp in Customer.query().fetch():
            if c.toppings == temp.toppings and c.location == temp.location:
                print "You found a match!"
                print c.email
                print temp.email
                temp.key.delete()
                self.response.write(env.get_template('results.html').render())
                return
        c.put()
        self.response.write(env.get_template('results.html').render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('results.html')
        self.response.write(template.render())

class Customer(ndb.Model):
    num_people = ndb.IntegerProperty()
    toppings = ndb.StringProperty()
    location = ndb.StringProperty()
    email = ndb.StringProperty()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getstarted', FormHandler),
    ('/results', ResultsHandler),
], debug=True)
