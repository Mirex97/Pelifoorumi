from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.threads.models import Thread

@app.route("/comments/", methods=["POST"])
@login_required
def comments_create():
    
    form = CommentForm(request.form)
    threadi = Thread.query.get(form.thread_id.data)
    


    if not form.validate():
        return redirect(url_for("show_thread", thread_id = threadi.id))

    comm = Comment(form.message.data)
    comm.account_id = current_user.id
    comm.thread_id = form.thread_id.data

    db.session().add(comm)
    db.session().commit()


    return redirect(url_for("show_thread", thread_id = threadi.id))

#comments_modify
#Nämä vasta seuraavalle viikolle.
#comments_remove
#Full CRUD löytyy käyttäjistä!
