from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TagForm(FlaskForm):
    name = StringField("Tag name", [validators.InputRequired()])

    class Meta:
        csrf = False
