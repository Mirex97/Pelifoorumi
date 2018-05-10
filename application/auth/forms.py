from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    password = PasswordField("Password", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    referrer = HiddenField()

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    username = StringField("User Name", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    name = StringField("Name", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    oldpassword = PasswordField("Old Password", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    newpassword = PasswordField("New Password", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])

    class Meta:
        csrf = False;

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    username = StringField("Username", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    password = PasswordField("Password", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])
    passwordconfirm = PasswordField("Retype Password", [validators.InputRequired(),
                                        validators.Length(min=2, max=20, message="Length 2-20 characters!")])

    class Meta:
        csrf = False;
