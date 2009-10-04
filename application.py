import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), self.getPath())
        self.response.out.write(template.render(path, {}))

class AboutUsPage(MainPage):
    def getPath(self):
        return 'aboutus.html'

class CeremonyPage(MainPage):
    def getPath(self):
        return 'ceremony.html'

class Greeting(db.Model):
    author = db.StringProperty()
    message = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class GuestbookPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(50)

        template_values = { 'greetings': greetings }

        path = os.path.join(os.path.dirname(__file__), 'guestbook.html')
        self.response.out.write(template.render(path, template_values))

class GuestInformationPage(MainPage):
    def getPath(self):
        return 'guestinformation.html'

class HoneymoonPage(MainPage):
    def getPath(self):
        return 'honeymoon.html'

class OurProposalPage(MainPage):
    def getPath(self):
        return 'ourproposal.html'

class PhotoAlbumPage(MainPage):
    def getPath(self):
        return 'photoalbum.html'

class ReceptionPage(MainPage):
    def getPath(self):
        return 'reception.html'

class RegistryPage(MainPage):
    def getPath(self):
        return 'registry.html'

class SignGuestbookPage(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        greeting.author = self.request.get('author')
        greeting.message = self.request.get('message')
        greeting.put()
        self.redirect('/guestbook.html')

class WeddingPartyPage(MainPage):
    def getPath(self):
        return 'weddingparty.html'

class WelcomePage(MainPage):
    def getPath(self):
        return 'welcome.html'

application = webapp.WSGIApplication([('/aboutus.html', AboutUsPage),
                                      ('/ceremony.html', CeremonyPage),
                                      ('/guestbook.html', GuestbookPage),
                                      ('/guestinformation.html', GuestInformationPage),
                                      ('/honeymoon.html', HoneymoonPage),
                                      ('/ourproposal.html', OurProposalPage),
                                      ('/photoalbum.html', PhotoAlbumPage),
                                      ('/reception.html', ReceptionPage),
                                      ('/reception.html', ReceptionPage),
                                      ('/registry.html', RegistryPage),
                                      ('/signguestbook', SignGuestbookPage),
                                      ('/weddingparty.html', WeddingPartyPage),
                                      ('/welcome.html', WelcomePage),
                                      ('/', WelcomePage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
