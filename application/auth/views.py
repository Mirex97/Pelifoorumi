from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, ModifyForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    if request.method == "GET":
        form = LoginForm()
        form.referrer.data = request.referrer
        return render_template("auth/loginform.html", form = form)

    
    form = LoginForm(request.form)
    
    
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")
        
    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(form.referrer.data)

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register")
def auth_form():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("auth/register.html", form = RegisterForm())

@app.route("/auth/register", methods = ["POST"])
def auth_register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    
    form = RegisterForm(request.form)
    form.name.data = form.name.data.replace(" ", "")
    form.username.data = form.username.data.replace(" ", "")
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

    print("User " + user.name + " recognized")
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
    form.name.data = form.name.data.replace(" ", "")
    form.username.data = form.username.data.replace(" ", "")
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

@app.route("/auth/promote/<user_id>", methods = ["POST"])
@login_required
def auth_promote(user_id):
    if current_user.role != 'Admin':
        return redirect(url_for("auth_list"))
    user = User.query.get(user_id)
    user.role = 'Admin'
    db.session().commit()
    return redirect(url_for("auth_list"))

@app.route("/auth/list")
def auth_list():
    if not current_user.is_authenticated:
        
        return render_template("auth/list.html", users = User.find_usernames())
    return render_template("auth/list.html", users = User.find_users_not_me(current_user.id))
    

@app.route("/auth/delete/<user_id>", methods = ["POST", "GET"])
@login_required
def auth_remove(user_id):
    user = User.query.get(user_id)
    if (user.id == current_user.id or current_user.role == 'Admin'):
        if (user.role == 'Admin' and user.id != current_user.id):
            return redirect(url_for("auth_list"))
        if (user.id == current_user.id):
            logout_user()
        db.session().delete(user)
        db.session().commit()
        return redirect(url_for("index"))
    return redirect(url_for("index"))
