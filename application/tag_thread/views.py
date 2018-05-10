from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.tag_thread.models import Tag_Thread

@app.route("/tag/join/<thread_id>", methods=["POST"])
@login_required
def tag_join(thread_id):
    curThread = Thread.query.get(thread_id)
    if not curThread.account_id == current_user.id:
        return redirect(url_for("show_thread", thread_id = thread_id))
    join = Tag_Thread()
    try:
        join.tag_id = request.form['tag_id']
    except:
        return redirect(url_for("show_thread", thread_id = thread_id))
    
    join.thread_id = thread_id
    if Tag_Thread.check_for_id(join.tag_id, join.thread_id):
        return redirect(url_for("show_thread", thread_id = thread_id))
    db.session().add(join)
    db.session.commit()
    return redirect(url_for("show_thread", thread_id = thread_id))

@app.route("/tag/unjoin/<thread_id>/<tag_id>", methods=["GET"])
@login_required
def tag_unjoin(thread_id, tag_id):
    curThread = Thread.query.get(thread_id)
    if not curThread.account_id == current_user.id:
        return redirect(url_for("show_thread", thread_id = thread_id))
    unjoin = Tag_Thread()
    unjoin.tag_id = tag_id
    unjoin.thread_id = thread_id
    if not Tag_Thread.check_for_id(unjoin.tag_id, unjoin.thread_id):
        return redirect(url_for("show_thread", thread_id = thread_id))
    remove = Tag_Thread.get_for_ids(unjoin.tag_id, unjoin.thread_id)
    toremove = Tag_Thread.query.get(remove)
    db.session().delete(toremove)
    db.session.commit()
    return redirect(url_for("show_thread", thread_id = thread_id))
