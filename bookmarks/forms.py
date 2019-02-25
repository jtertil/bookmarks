from flask_wtf import FlaskForm
from wtforms import StringField
# from wtforms.fields.html5 import URLField
# from wtforms.validators import DataRequired, url
# from wtforms.fields import StringField
# from wtforms.fields.html5 import URLField
# from wtforms.validators import DataRequired, url

class BookmarkForm(FlaskForm):
    # url = URLField('url', validators=[DataRequired(), url()])
    url = StringField('url')
    description = StringField('description')

    def validate (self):
        # if not self.url.data.startswith("http://"):
        #     self.url.data = "http://" + self.url.data

        if self.url.data.startswith("http://") == False and self.url.data.startswith("https://") == False :
            self.url.data = "http://" + self.url.data


        # if not FlaskForm.validate(self):
        #     return False
        #
        # if not self.description.data:
        #     self.description.data = self.url.data

        return True
