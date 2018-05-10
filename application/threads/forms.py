from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, TextAreaField, BooleanField, IntegerField

class ThreadForm(FlaskForm):
    name = StringField("Thread name", [validators.InputRequired(), validators.Length(min=2, max=40, message="Too long! 2-40 characters limit!")])
    desc = TextAreaField("Description", [validators.Length(min=0, max=400, message="Too long! 400 characters limit!")])
    hidden = BooleanField("Hidden")
    section_id = HiddenField()

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    search = StringField("Search")
    select = BooleanField("For User")

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    name = StringField("Thread name", [validators.InputRequired(), validators.Length(min=2, max=40, message="Too long! 2-40 characters limit!")])
    desc = TextAreaField("Description", [validators.Length(min=0, max=400, message="Too long! 400 characters limit!")])
    hidden = BooleanField("Hidden")
    section_id = IntegerField("Section", [validators.InputRequired()])
    
    class Meta:
        csrf = False
