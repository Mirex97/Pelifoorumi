from flask import render_template, request, redirect, url_for

from application import app, db
from application.threads.models import Thread

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())

@app.route("/threads/new/")
def threads_form():
    return render_template("threads/new.html")
  
@app.route("/threads/<thread_id>/", methods=["POST"])
def show_thread(thread_id):
    return render_template("threads/thread.html", thread = Thread.query.get(thread_id))


@app.route("/threads/", methods=["POST"])
def threads_create():
    t = Thread(request.form.get("name"), request.form.get("owner"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("threads_index"))
