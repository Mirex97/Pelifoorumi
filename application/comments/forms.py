from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, HiddenField

class CommentForm(FlaskForm):
    message = TextAreaField("Message", [validators.InputRequired(),
                                        validators.Length(min=1, max=400, message="Too long! 400 characters limit!")])
    thread_id = HiddenField()

    class Meta:
        csrf = False
