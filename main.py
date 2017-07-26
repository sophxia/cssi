import jinja2
import os
import webapp2
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.api import mail


env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
env1=jinja2.Environment(loader=jinja2.FileSystemLoader(''))

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
            if (c.num_people+temp.num_people)%4==0 and c.toppings == temp.toppings and c.location == temp.location:
                print "You found a match!"
                print c.email
                print temp.email

                dic1 = c.get_mail_info(temp)
                dic2 = temp.get_mail_info(c)

                self.send_mail(dic1)
                self.send_mail(dic2)

                # EmailHandler(c, temp);
                temp.key.delete()
                self.response.write(env.get_template('results.html').render())
                return
        c.put()
        self.response.write(env.get_template('results.html').render())

    def send_mail (self, dic):
        template = env.get_template('resources/mailTemplate.txt')
        mail.send_mail(sender= "Slice@slice-cssi.appspotmail.com",
                           to= dic['email'],
                           subject="You've been Matched!",
                           body= template.render(dic))


class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('results.html')
        self.response.write(template.render())

class Customer(ndb.Model):
    num_people = ndb.IntegerProperty()
    toppings = ndb.StringProperty()
    location = ndb.StringProperty()
    email = ndb.StringProperty()

    def get_mail_info (self, temp):
        dic = {'email' : self.email, 'match_email' : temp.email, 'toppings' : self.toppings, 'location' : self.location, 'num_people' : self.num_people}
        return dic

class EmailHandler(webapp2.RequestHandler):
    def get(self, c2):



        # test_dic = {'email' : 'testymail@gmail.com', 'toppings' : 'cheese', 'location' : 'MIT'}




        template = env.get_template('resources/mailTemplate.txt')
        mail.send_mail(sender= "Slice@slice-cssi.appspotmail.com",
                           to= "austinmejia12@gmail.com",
                           subject="You've been Matched!",
                           body= template.render(test_dic))

        # mail.send_mail(sender= "Slice@slice-cssi.appspotmail.com",
        #                    to= "  < " + c2.email + " >",
        #                    subject="You've been Matched! -Slice",
        #                    body=template.render(c2))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getstarted', FormHandler),
    ('/results', ResultsHandler),
    ('/email', EmailHandler)
], debug=True)
