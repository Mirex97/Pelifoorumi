from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThreadForm(FlaskForm):
    name = StringField("Thread name", [validators.InputRequired()])

    class Meta:
        csrf = False
