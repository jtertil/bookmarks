from bookmarks import app, db
from flask_script import Manager, prompt_bool

from models import User

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="developer", email="some@email.com"))
    db.session.add(User(username="developer2", email="some2@email.com"))
    db.session.commit()
    print('Initialized the database')

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want lose all your data"):
        db.drop_all()
        print('Dropped database')

if __name__ == "__main__":
    manager.run()
