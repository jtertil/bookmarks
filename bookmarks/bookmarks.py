from flask import Flask, render_template, url_for, request, redirect, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x87&X\x1d\x11\xf7\x91\xd6\xd6\xdf\xaa9\xfd\xfc}\x81w\tW[=\xd3\x8a\x89'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bookmarks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from datetime import datetime
from forms import BookmarkForm
import models

# fake login
def logged_in_user():
    return models.User.query.filter_by(username='developer').first()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        if form.description.data == "":
            description = url
        else:
            description = form.description.data
        bm = models.Bookmark(user=logged_in_user(), url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')


# if __name__ == '__main__':
#     app.run(debug=True)
