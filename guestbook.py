import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Greeting(db.Model):
    author = db.StringProperty()
    message = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(50)

        template_values = { 'greetings': greetings }

        path = os.path.join(os.path.dirname(__file__), 'guestbook.html')
        self.response.out.write(template.render(path, template_values))

class Guestbook(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        greeting.author = self.request.get('author')
        greeting.message = self.request.get('message')
        greeting.put()
        self.redirect('/guestbook.html')

application = webapp.WSGIApplication([('/guestbook.html', MainPage),
                                      ('/signguestbook', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
