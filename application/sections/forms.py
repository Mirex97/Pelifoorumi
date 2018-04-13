from flask_wtf import FlaskForm
from wtforms import StringField, validators


#Only for admin to see!
class SectionForm(FlaskForm):
    name = StringField("Section name", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])

    class Meta:
        csrf = False
