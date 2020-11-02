from flask import Flask,
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ojiukg89j1po1l1h2v36aj2h41oq235qk3hg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)  