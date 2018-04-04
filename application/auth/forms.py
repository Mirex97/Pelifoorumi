from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    username = StringField("User Name", [validators.InputRequired()])
    name = StringField("Name", [validators.InputRequired()])
    oldpassword = PasswordField("Old Password", [validators.InputRequired()])
    newpassword = PasswordField("New Password", [validators.InputRequired()])

    class Meta:
        csrf = False;

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    passwordconfirm = PasswordField("Retype Password", [validators.InputRequired()])

    class Meta:
        csrf = False;
