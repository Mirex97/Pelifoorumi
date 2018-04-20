from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, HiddenField


class SectionForm(FlaskForm):
    name = StringField("Section name", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    priority = IntegerField("Priority", [validators.InputRequired()])
    section_id = HiddenField()

    class Meta:
        csrf = False
