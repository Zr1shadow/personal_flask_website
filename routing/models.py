# from routes import db
from __main___ import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), unique = True, nullable = False)
    chapters = db.Column(db.String(20), unique = True, nullable = False)
    chapter_links = db.Column(db.String(40), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}')"
