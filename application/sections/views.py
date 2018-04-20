from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.sections.models import Section
from application.sections.forms import SectionForm

from application.threads.models import Thread
from application.threads.forms import ThreadForm

@app.route("/sections", methods=["GET"])
def section_index():
    sections = Section.find_sections_by_priority()
    return render_template("sections/list.html", sections = sections)

@app.route("/sections/<section_id>/", methods=["GET"])
def show_section(section_id):
    section = Section.query.get(section_id)
    threads = Section.find_threads_with_section(section.id)
    form = ThreadForm()
    form.section_id.data = section.id
    if current_user.is_authenticated == False:
        return render_template("sections/section.html",
                               section = section,
                               threads = threads,
                               form = form)
    
    mythreads = Thread.query.order_by(Thread.date_created.desc()).filter_by(account_id=current_user.id).filter_by(section_id=section_id)
    if current_user.role == 'Admin':
        sform = SectionForm()
        sform.section_id.data = section.id
        return render_template("sections/section.html",
                               section = section,
                               threads = threads,
                               mythreads = mythreads,
                               form = form,
                               sform = sform)
    return render_template("sections/section.html",
                           section = section,
                           threads = threads,
                           mythreads = mythreads,
                           form = form)

@app.route("/sections/new")
@login_required
def section_form():
    if not current_user.role == 'Admin':
        return redirect(url_for("section_index"))
    return render_template("sections/new.html", form = SectionForm())

@app.route("/sections/", methods=["POST"])
@login_required
def section_create():
    form = SectionForm(request.form)
    if not form.validate():
        return render_template("sections/new.html", form = form)
    s = Section(form.name.data)
    s.priority = form.priority.data

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("section_index"))

@app.route("/sections/edit", methods=["POST"])
@login_required
def section_edit():
    form = SectionForm(reguest.form)
    if not form.validate():
        return redirect(url_for("show_section"), section_id = form.section_id)
    s = Section.query.get(section_id)
    s.name = form.name
    s.priority = form.priority
    db.session().commit()
    return redirect(url_for("show_section"), section_id = form.section_id)

@app.route("/sections/remove/<section_id>", methods=["POST"])
@login_required
def section_remove(section_id):
    section = Section.query.get(section_id)
    if (current_user.role != 'Admin'):
        return redirect(url_for("section_index"))
    db.session().delete(section)
    db.session().commit()
    return redirect(url_for("section_index"))

