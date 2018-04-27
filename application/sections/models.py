from application import db
from sqlalchemy.sql import text

class Section(db.Model):
    __tablename__ = "Section"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    priority = db.Column(db.Integer, nullable=False)

    threads = db.relationship("Thread", backref='Section', lazy=True, cascade="delete")
    

    def __init__(self, name):
        self.name = name
        self.priority = 0;

    @staticmethod
    def find_sections_by_priority():
        stmt = text("SELECT Section.id, Section.name, Section.priority FROM Section"
                    " ORDER BY Section.priority")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "priority":row[2]})
        return response

    @staticmethod
    def find_threads_with_section(section_id):
        stmt = text("SELECT  Thread.id, Thread.name, Account.username FROM Thread"
                    " LEFT JOIN Account ON Thread.account_id = Account.id"
                    " WHERE (Thread.section_id = :sectionid)"
                    " ORDER BY Thread.date_created"
                    " DESC").params(sectionid=section_id)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "owner":row[2]})
        return response
