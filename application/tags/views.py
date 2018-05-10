from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.tags.models import Tag
from application.tags.forms import TagForm
from application.threads.models import Thread

@app.route("/tags", methods=["GET"])
def tags_index():
    tags = Tag.query.all();
    if current_user.is_authenticated:
        if current_user.role == 'Admin':
            form = TagForm()
            return render_template("tags/list.html", tags = tags, form = form)
    return render_template("tags/list.html", tags = tags)

@app.route("/tags/new/")
@login_required
def tag_form():
    if not current_user.role == 'Admin':
        redirect(url_for("tags_index"))
    return render_template("tags/new.html", form = TagForm())

@app.route("/tags/confirm/", methods=["POST"])
@login_required
def add_tag():
    if not current_user.role == 'Admin':
        redirect(url_for("tags_index"))
    form = TagForm(request.form)
    tags = Tag.find_with_tag(form.name.data)
    if tags:
        return redirect(request.referrer)
    if not form.validate():
        return redirect(request.referrer)
    t = Tag(form.name.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tags_index"))

@app.route("/tags/remove/<tag_id>", methods=["POST"])
@login_required
def tag_remove(tag_id):
    if not current_user.role == 'Admin':
        return redirect(url_for("tags_index"))
    tag = Tag.query.get(tag_id)
    db.session().delete(tag)
    db.session().commit()
    return redirect(url_for("tags_index"))

@app.route("/tags/find/<tag>", methods=["GET", "POST"])
def find_threads(tag):
    threads = Tag.find_threads_by_tag(tag);
    return render_template("threads/search.html", threads = threads)
