from application import db
from sqlalchemy.sql import text

class Section(db.Model):
    __tablename__ = "section"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    priority = db.Column(db.Integer, nullable=False)

    threads = db.relationship("Thread", backref='section', lazy=True, cascade="delete")
    

    def __init__(self, name):
        self.name = name
        self.priority = 0;

    @staticmethod
    def find_sections_by_priority():
        stmt = text("SELECT section.id, section.name, section.priority FROM section"
                    " ORDER BY section.priority")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "priority":row[2]})
        return response

    @staticmethod
    def find_threads_with_section(section_id):
        stmt = text("SELECT  thread.id, thread.name, account.username FROM thread"
                    " LEFT JOIN account ON thread.account_id = account.id"
                    " WHERE (thread.section_id = :sectionid)"
                    " ORDER BY thread.date_created"
                    " DESC").params(sectionid=section_id)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "owner":row[2]})
        return response
