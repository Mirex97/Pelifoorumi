from application import db
from sqlalchemy.sql import text

class Section(db.Model):
    __tablename__ = "section"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    threads = db.relationship("Thread", backref='section', lazy=True, cascade="delete")
    

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_threads_with_section(section_id):
        stmt = text("SELECT  Thread.id, Thread.name, Account.username FROM Thread"
                    " LEFT JOIN Account ON Thread.account_id = Account.id"
                    " WHERE (Thread.section_id IS :sectionid)"
                    " GROUP BY Thread.id"
                    " ORDER BY Thread.date_created"
                    " DESC").params(sectionid=section_id)
        #" + str(section_id) + ")"
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "owner":row[2]})
        return response
