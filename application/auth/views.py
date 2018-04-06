from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, ModifyForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register")
def auth_form():
    return render_template("auth/register.html", form = RegisterForm())

@app.route("/auth/register", methods = ["POST"])
def auth_register():
    form = RegisterForm(request.form)


    user = User.query.filter_by(username=form.username.data).first()
    if user:
        form.username.data = ""
        return render_template("auth/register.html",
                               form = form,
                               error = "Username already taken!")

    if form.password.data != form.passwordconfirm.data:
        return render_template("auth/register.html",
                               form = form,
                               error = "Passwords did not match!")

    if not form.validate():
        return render_template("auth/register.html", form = form)
    
    user = User(form.name.data, form.username.data, form.password.data)
    db.session().add(user)
    db.session().commit()

    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))
    

@app.route("/auth/view")
@login_required
def auth_view():
    user = User.query.get(current_user.id)
    return render_template("auth/view.html", user = user)
    

@app.route("/auth/modify", methods = ["GET"])
@login_required
def auth_modify():
    form = ModifyForm()
    form.name.data = current_user.name
    
    return render_template("auth/modify.html", form = form)

@app.route("/auth/modify", methods = ["POST"])
@login_required
def auth_confirm():
    form = ModifyForm(request.form)
    if current_user.password != form.oldpassword.data:
        return render_template("auth/modify.html", form = form,
                               error = "Password did not match.")

    if not form.validate():
        return render_template("auth/modify.html", form = form,
                               error = "No Empty Fields Allowed!")
    
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        form.username.data = ""
        return render_template("auth/modify.html",
                               form = form,
                               error = "Username already taken!")
    
    user = User.query.get(current_user.id)
    user.name = form.name.data
    user.username = form.username.data
    user.password = form.newpassword.data
    db.session().commit()
    return redirect(url_for("auth_view"))

@app.route("/auth/list")
def auth_list():
    return render_template("auth/list.html", users = User.query.all())
    

@app.route("/auth/delete", methods = ["POST"])
@login_required
def auth_remove():
    user = User.query.get(current_user.id)
    logout_user()
    db.session().delete(user)
    db.session().commit()
    return redirect(url_for("index"))
