from flask import render_template, flash, redirect, url_for
from routing.forms import RegistrationForm, LoginForm, PostNewMangaEntry
from routing.models import User, Post
from routing import app, db
from Scrapers.mangaScraper import Scaper
from flask_login import login_user, current_user, logout_user
from routing.queries import MangaQueries


@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.password:
                login_user(user, remember= form.remember.data)
                flash('You have been logged in!', 'success')
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
   
            return redirect(url_for('home'))
    return render_template('login.html', title = 'Login', form = form)
@app.route('/')
@app.route('/post/manga', methods = ['POST', 'GET'])
def manga_list():
    form = PostNewMangaEntry()
    query = MangaQueries()
    info = query.getAllMangaTitles()
    if form.validate_on_submit():
        
    
        scraper = Scaper(form.url.data)
        scraper.getAllChapterNum()
        title = scraper.getMangaTitle()
        flash('Manga has been found', 'success')
        return redirect(url_for('manga', manga_title = title))
        # return redirect(url_for('home'))
    return render_template('manga_list.html', title = 'New Manga Entry', form = form, info = info)


@app.route('/manga/<manga_title>')
def manga(manga_title):
    query = MangaQueries()
    info = query.getMangaContent(manga_title)
    return render_template('manga.html', title = manga_title, info = info)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/test')
def test():
    a = MangaQueries()
    a.dailyUpdate()
    return redirect(url_for('test'))

