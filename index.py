from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ojiukg89j1po1l1h2v36aj2h41oq235qk3hg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)  

login_manager = LoginManager(app)
 
from routing import routes