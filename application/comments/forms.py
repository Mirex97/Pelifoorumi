from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField

class CommentForm(FlaskForm):
    message = StringField("Message", [validators.InputRequired()])
    thread_id = HiddenField()

    class Meta:
        csrf = False
