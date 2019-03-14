from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Regexp, EqualTo, Email

class BookmarkForm(FlaskForm):
    url = URLField('url', validators=[DataRequired(), url()])
    # url = StringField('url')
    description = StringField('description')
    tags = StringField('Tags', validators=[Regexp(r'^[A-Za-z0-9, ]*$', message="Tags can only contain letters and numbers")])

    def validate (self):
        if self.url.data.startswith("http://") == False and self.url.data.startswith("https://") == False :
            self.url.data = "http://" + self.url.data

        if not FlaskForm.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        #fliter for empty and duplicate tags
        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]
        tagset = set(not_empty)
        self.tags.data = ",".join(tagset)

        return True

class LoginForm(FlaskForm):
    username = StringField('Your Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in...')
    submit = SubmitField('Log in')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80), Regexp('^[A-Za-z0-9_]{3,}$', message='Username consist of numbers, letters, and underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 120), Email()])

def validate_email(self, email_field):
    if User.query.filter_by(email=email_field.data).first():
        raise ValidationError('There already is a user with this email adress.')

def validate_username(self, username_field):
    if User.query.filter_by(username=username_field.data).first():
        raise ValidationError('This username already taken.')
