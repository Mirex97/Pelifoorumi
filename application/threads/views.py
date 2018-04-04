from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.threads.forms import ThreadForm
from application.auth.models import User
from application.comments.models import Comment
from application.comments.forms import CommentForm


@app.route("/threads", methods=["GET"])
def threads_index():
    threads = Thread.query.order_by(Thread.date_created.desc()).all()
    if current_user.is_authenticated == False:
        return render_template("threads/list.html", threads = threads,
                           users = User.query.all())
    mythreads = Thread.query.order_by(Thread.date_created.desc()).filter_by(account_id=current_user.id)
    return render_template("threads/list.html", threads = threads,
                           users = User.query.all(),
                           mythreads = mythreads)

@app.route("/threads/new/")
@login_required
def threads_form():
    return render_template("threads/new.html", form = ThreadForm())
  
@app.route("/threads/<thread_id>/", methods=["POST", "GET"])
def show_thread(thread_id):
    thread = Thread.query.get(thread_id)
    form = CommentForm()
    form.thread_id.data = thread.id
    #Sisältää kommenttien katselun!
    return render_template("threads/thread.html",
                           thread = Thread.query.get(thread_id),
                           owner = User.query.get(thread.account_id),
                           comments = Comment.query.filter_by(thread_id=thread.id),
                           form = form,
                           users = User.query.all())


@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form = form)

    t = Thread(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("threads_index"))
