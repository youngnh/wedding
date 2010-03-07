import os
import spam

from google.appengine.api import images
from google.appengine.api import users

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from datetime import datetime
from ustimezones import Central, utc

authorized = ["paige2987", "youngnh"]

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), self.getPath())
        self.response.out.write(template.render(path, {}))

class AuthPage(webapp.RequestHandler):
    def checkAuth(self):
        user = users.get_current_user()

        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return False

        if user.nickname() not in authorized:
            self.redirect('/welcome')
            return False

        return True

    def get(self):
        if self.checkAuth():
            self.doGet()

    def post(self):
        if self.checkAuth():
            self.doPost()

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

class SpamGreeting(Greeting):
    pass

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
        self.response.headers["Content-Type"] = "image/jpeg"
        self.response.out.write(photo.img)

class DisplayThumb(webapp.RequestHandler):
    def get(self, id):
        photo = Photo.get_by_id(int(id))
        img = images.Image(photo.img)
        img.resize(int(img.width * 0.3), int(img.height * 0.3))
        img.im_feeling_lucky()
        thumbnail = img.execute_transforms(output_encoding=images.JPEG)

        self.response.headers["Content-Type"] = "image/jpeg"
        self.response.out.write(thumbnail)

def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        yield val

class Section(db.Model):
    photos = db.ListProperty(db.Key)
    name = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    def __getattr__(self, attrname):
        if attrname == "rows":
            return self._rows()

    def _rows(self):
        photos = Photo.get(self.photos)
        for photo in photos:
            photo.src = photo.key().id()

        rows = list(group(photos, 4))
        return rows

class PhotoAlbumPage(webapp.RequestHandler):
    def get(self):
        sections_query = Section.all().order('created')
        sections = sections_query.fetch(50)

        template_values = { 'sections': sections }

        path = os.path.join(os.path.dirname(__file__), 'photoalbum.html')
        self.response.out.write(template.render(path, template_values))

class ManagePhotoAlbumPage(AuthPage):
    def doGet(self):
        path = os.path.join(os.path.dirname(__file__), 'uploadphoto.html')
        self.response.out.write(template.render(path, {}))

class UploadPhotoPage(AuthPage):
    def doPost(self):
        photo = Photo()

        photo.img = self.request.get('file')
        photo.title = self.request.get('title')
        photo.put()

        # decide if we have to create a new section
        section_name = self.request.get('section')
        section = Section.get_by_key_name(section_name)
        if not section:
            section = Section(key_name=section_name, name=section_name)

        # add photo to the section, and save
        section.photos.append(photo.key())
        section.put()

        self.redirect('/photoalbum/manage')

class ReceptionPage(MainPage):
    def getPath(self):
        return 'reception.html'

class RegistryPage(MainPage):
    def getPath(self):
        return 'registry.html'

class SignGuestbookPage(webapp.RequestHandler):
    def post(self):
        author = self.request.get('author')
        message = self.request.get('message')
        message = getMessageModel(author, message)
        message.put()
        self.redirect('/guestbook')

def getMessageModel(author, message):
    if spam.isSpam(message):
        greeting = SpamGreeting()
    else:
        greeting = Greeting()

    greeting.author = author
    greeting.message = message
    return greeting

class WeddingPartyPage(MainPage):
    def getPath(self):
        return 'weddingparty.html'

class WelcomePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template_values = { 'signed_in': True,
                                'logout_url': users.create_logout_url(self.request.uri) }
        else:
            template_values = {}

        path = os.path.join(os.path.dirname(__file__), self.getPath())
        self.response.out.write(template.render(path, template_values))

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
