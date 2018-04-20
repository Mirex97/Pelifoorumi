from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.tag_thread.models import Tag_Thread

@app.route("/tag/join/<thread_id>", methods=["POST"])
@login_required
def tag_join(thread_id):
    join = Tag_Thread()
    join.tag_id = request.form['tag_id']
    join.thread_id = thread_id
    if Tag_Thread.check_for_id(join.tag_id, join.thread_id):
        return redirect(url_for("show_thread", thread_id = thread_id))
    db.session().add(join)
    db.session.commit()
    return redirect(url_for("show_thread", thread_id = thread_id))
