import os

from google.appengine.api import images

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from datetime import datetime
from ustimezones import Central, utc

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
    message = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class GuestbookPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(50)
        for greeting in greetings:
            utc_date = greeting.date.replace(tzinfo=utc)
            greeting.date = utc_date.astimezone(Central)

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

class Photo(db.Model):
    img = db.BlobProperty()
    title = db.StringProperty()

class DisplayImage(webapp.RequestHandler):
    def get(self, id):
        photo = Photo.get_by_id(int(id))
        self.response.headers.add_header("Content-Type", "image/jpeg")
        self.response.out.write(photo.img)

class DisplayThumb(webapp.RequestHandler):
    def get(self, id):
        photo = Photo.get_by_id(int(id))
        img = images.Image(photo.img)
        img.resize(int(img.width * 0.3), int(img.height * 0.3))
        img.im_feeling_lucky()
        thumbnail = img.execute_transforms(output_encoding=images.JPEG)

        self.response.headers.add_header("Content-Type", "image/jpeg")
        self.response.out.write(thumbnail)

def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        yield val

class PhotoAlbumPage(webapp.RequestHandler):
    def get(self):
        photos_query = Photo.all()
        photos = photos_query.fetch(50)
        for photo in photos:
            photo.src = photo.key().id()

        rows = list(group(photos, 4))

        template_values = { 'rows': rows }

        path = os.path.join(os.path.dirname(__file__), 'photoalbum.html')
        self.response.out.write(template.render(path, template_values))

class ManagePhotoAlbumPage(MainPage):
    def getPath(self):
        return 'uploadphoto.html'

class UploadPhotoPage(webapp.RequestHandler):
    def post(self):
        photo = Photo()

        photo.img = self.request.get('file')
        photo.title = self.request.get('title')
        photo.put()
        self.redirect('/photoalbum/manage')

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
        self.redirect('/guestbook')

class WeddingPartyPage(MainPage):
    def getPath(self):
        return 'weddingparty.html'

class WelcomePage(MainPage):
    def getPath(self):
        return 'welcome.html'

application = webapp.WSGIApplication([('/aboutus', AboutUsPage),
                                      ('/ceremony', CeremonyPage),
                                      ('/guestbook', GuestbookPage),
                                      ('/guestinformation', GuestInformationPage),
                                      ('/honeymoon', HoneymoonPage),
                                      ('/ourproposal', OurProposalPage),
                                      ('/photoalbum', PhotoAlbumPage),
                                      ('/photoalbum/manage', ManagePhotoAlbumPage),
                                      ('/photoalbum/upload', UploadPhotoPage),
                                      ('/photoalbum/images/(.*)', DisplayImage),
                                      ('/photoalbum/thumbs/(.*)', DisplayThumb),
                                      ('/reception', ReceptionPage),
                                      ('/reception', ReceptionPage),
                                      ('/registry', RegistryPage),
                                      ('/signguestbook', SignGuestbookPage),
                                      ('/weddingparty', WeddingPartyPage),
                                      ('/welcome', WelcomePage),
                                      ('/', WelcomePage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
