from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField

class ThreadForm(FlaskForm):
    name = StringField("Thread name", [validators.InputRequired()])
    section_id = HiddenField()

    class Meta:
        csrf = False
