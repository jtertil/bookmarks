from bookmarks import app, db
from bookmarks.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    admin = User(username="developer", email="developer@mail.com", password="test")
    db.session.add(admin)

    testUser = User(username="developer2", email="developer2@mail.com", password="test")
    db.session.add(testUser)

    for name in ["python", "flask", "webdev", "tools"]:
        db.session.add(Tag(name=name))

    db.session.commit()

    # def add_bookmark(url, description, tags):
    #     db.session.add(Bookmark(url=url, description=description, user=admin, _tags=tags))


    # add_bookmark("https://www.python.org/", "The official home of the Python Programming Language.", "python")
    # add_bookmark("http://flask.pocoo.org/", "Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.", "python,flask,webdev")
    # add_bookmark("https://www.sqlalchemy.org/", "SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.", "python,webdev")
    # add_bookmark("http://werkzeug.pocoo.org/", "Werkzeug is a WSGI utility library for Python. It's widely used and BSD licensed.", "python,flask")
    # add_bookmark("http://jinja.pocoo.org/", "Jinja2 is a full featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.", "python,webdev")


if __name__ == '__main__':
    manager.run()
