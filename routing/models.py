from routing import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import joinedload
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    chapters = db.Column(db.String(20), unique=True, nullable=False)
    chapter_links = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"


class MangaChapters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(30), nullable=False)
    chapter_link = db.Column(db.String(30),  nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('manga.id'),
        nullable=False)
    manga = db.relationship('Manga',
        backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return '<MangaChapters %r>' % self.chapter


class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    def __repr__(self):
        return '< Manga %r>' % self.title

