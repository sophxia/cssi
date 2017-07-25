from google.appengine.api import mail
import jinja2
import os
import webapp2
from google.appengine.api import images
from google.appengine.ext import ndb

env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class emailHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('resources/mailTemplate.txt')
        mail.send_mail(sender= "Slice@slice-cssi.appspotmail.com"
                           to= name + "  < " email + " >",
                           subject="You've been Matched! -Slice",
                           body=template.render())
