from flask_wtf import FlaskForm
from wtforms import SelectField, validators

class TagForm(FlaskForm):
    tag_id = SelectField("Tag", [validators.InputRequired()])

    class Meta:
        csrf = False
