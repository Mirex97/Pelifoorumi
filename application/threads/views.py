from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.threads.forms import ThreadForm
from application.auth.models import User
from application.comments.models import Comment
from application.comments.forms import CommentForm


@app.route("/threads", methods=["GET"])
@login_required
def threads_index():
    mythreads = Thread.find_my_threads(current_user.id)
    return render_template("threads/list.html",
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
                           comments = Comment.find_comments_with_thread(thread_id),
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
    t.section_id = form.section_id.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("show_thread", thread_id=t.id))

#Need modify!

@app.route("/threads/remove/<thread_id>", methods=["POST"])
@login_required
def thread_remove(thread_id):
    thread = Thread.query.get(thread_id)
    if (current_user.id != thread.account_id and current_user.role != 'Admin'):
        return redirect(url_for("threads_index"))
    db.session().delete(thread)
    db.session().commit()
    return redirect(url_for("threads_index"))
