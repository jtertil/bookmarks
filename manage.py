from bookmarks import app, db
from bookmarks.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="developer", email="some@email.com", password="test"))
    db.session.add(User(username="developer2", email="some2@email.com", password="test2"))
    db.session.commit()
    print('Initialized the database')

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want lose all your data"):
        db.drop_all()
        print('Dropped database')

if __name__ == "__main__":
    manager.run()
