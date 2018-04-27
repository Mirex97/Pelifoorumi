from application import db
from sqlalchemy.sql import text

class Tag(db.Model):

    __tablename__ = "Tag"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modifed = db.Column(db.DateTime, default=db.func.current_timestamp(),
                             onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    threads = db.relationship("Tag_Thread", backref='Tag', lazy=True, cascade='delete')

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_threads_by_tag(tag):
        stmt = text("SELECT DISTINCT Thread.id, Thread.name, Account.username, Section.name FROM Thread"
                    " LEFT JOIN Account ON Account.id = Thread.account_id"
                    " LEFT JOIN Section ON Section.id = Thread.section_id"
                    " LEFT JOIN Tag_Thread ON Thread.id = Tag_Thread.thread_id"
                    " LEFT JOIN Tag ON Tag.id = Tag_Thread.tag_id"
                    " WHERE (Tag.name = :tag)"
                    " ORDER BY Thread.date_created DESC").params(tag = tag)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "username":row[2], "section":row[3]})
        return response

    @staticmethod
    def find_with_tag(tag):
        stmt = text("SELECT * FROM Tag WHERE (Tag.name = :tag)").params(tag = tag)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response
        

    
