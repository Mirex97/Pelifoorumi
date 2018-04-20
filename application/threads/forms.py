from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, TextAreaField, BooleanField

class ThreadForm(FlaskForm):
    name = StringField("Thread name", [validators.InputRequired()])
    desc = TextAreaField("Description")
    section_id = HiddenField()

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    search = StringField("Search")
    select = BooleanField("For User")
    tag = BooleanField("Tag")

    class Meta:
        csrf = False
