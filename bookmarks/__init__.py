import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x87&X\x1d\x11\xf7\x91\xd6\xd6\xdf\xaa9\xfd\xfc}\x81w\tW[=\xd3\x8a\x89'
app.config['DEBUG'] = True

# database config
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bookmarks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# authentication config
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

import bookmarks.models
import bookmarks.views
