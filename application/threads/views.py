from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.tags.models import Tag
from application.threads.forms import ThreadForm
from application.threads.forms import SearchForm
from application.threads.forms import ModifyForm
from application.auth.models import User
from application.sections.models import Section
from application.comments.models import Comment
from application.comments.forms import CommentForm


@app.route("/threads", methods=["GET"])
@login_required
def threads_index():
    mythreads = Thread.find_my_threads(current_user.id)
    return render_template("threads/list.html",
                           users = User.query.all(),
                           mythreads = mythreads)

  
@app.route("/threads/<thread_id>/", methods=["GET"])
def show_thread(thread_id):
    thread = Thread.query.get(thread_id)
    if thread.hidden and not current_user.is_authenticated:
        print("NOT ALLOWED")
        return redirect(request.referrer)
    form = CommentForm()
    form.thread_id.data = thread.id
    return render_template("threads/thread.html",
                           thread = Thread.query.get(thread_id),
                           owner = User.query.get(thread.account_id),
                           comments = Comment.find_comments_with_thread(thread_id),
                           form = form,
                           tags = Tag.find_tags(),
                           users = User.query.all(),
                           threadtags = Tag.find_tags_with_thread(thread_id),
                           section = Section.query.get(thread.section_id))


@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)
    form.name.data = form.name.data.strip()

    if not form.validate():
        return redirect(request.referrer)

    t = Thread(form.name.data)
    t.desc = form.desc.data
    t.account_id = current_user.id
    t.section_id = form.section_id.data
    t.hidden = form.hidden.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("show_thread", thread_id=t.id))

@app.route("/threads/search/", methods=["POST"])
def threads_search():
    form = SearchForm(request.form)

    if form.select.data:
        threads = Thread.search_threads_by_user(form.search.data)
        return render_template("threads/search.html", threads = threads)
    else:
        threads = Thread.search_threads_by_thread(form.search.data)
        return render_template("threads/search.html", threads = threads)



@app.route("/threads/modify/<thread_id>", methods=["GET", "POST"])
@login_required
def thread_modify(thread_id):
    thread = Thread.query.get(thread_id)
    section = Section.query.get(thread.section_id)
    if (current_user.id != thread.account_id and current_user.role != 'Admin'):
        if thread.hidden:
            return redirect(url_for("threads_index"))
        else:
            return redirect(url_for("show_thread", thread_id = thread.id))
    else:
        if request.method == "GET":
            form = ModifyForm()
            form.name.data = thread.name
            form.desc.data = thread.desc
            form.hidden.data = thread.hidden
            return render_template("threads/modify.html", thread = thread, form = form, section = section, sections = Section.query.all())
        else:
            form = ModifyForm(request.form)
            form.name.data = form.name.data.strip()
            if not form.validate():
                return render_template("threads/modify.html", thread = thread, form = form, section = section, sections = Section.query.all())
            thread.name = form.name.data
            thread.desc = form.desc.data
            if current_user.role == 'Admin':
                thread.section_id = form.section_id.data
                print(form.section_id.data)
            if thread.locked:
                if current_user.role == 'Admin':
                    thread.hidden = form.hidden.data
            else:
                thread.hidden = form.hidden.data
            db.session.commit()
            return redirect(url_for("show_thread", thread_id = thread.id))


@app.route("/threads/pin/<thread_id>", methods=["GET"])
@login_required
def thread_pin(thread_id):
    thread = Thread.query.get(thread_id)
    if (current_user.role != 'Admin'):
        return redirect(url_for("show_thread", thread_id = thread.id))
    if thread.pinned:
        thread.pinned = False
    else:
        thread.pinned = True
    db.session.commit()
    return redirect(url_for("show_thread", thread_id = thread.id))


@app.route("/threads/lock/<thread_id>", methods=["GET"])
@login_required
def thread_lock(thread_id):
    thread = Thread.query.get(thread_id)
    if (current_user.role != 'Admin'):
        return redirect(url_for("show_thread", thread_id = thread.id))
    if thread.locked:
        thread.locked = False
    else:
        thread.locked = True
        
    db.session.commit()
    return redirect(url_for("show_thread", thread_id = thread.id))

@app.route("/threads/remove/<thread_id>", methods=["POST"])
@login_required
def thread_remove(thread_id):
    thread = Thread.query.get(thread_id)
    if (current_user.id != thread.account_id and current_user.role != 'Admin'):
        return redirect(request.referrer)
    db.session().delete(thread)
    db.session().commit()
    return redirect(request.referrer)
