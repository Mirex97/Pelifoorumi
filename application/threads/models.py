from application import db
from sqlalchemy.sql import text

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    desc = db.Column(db.String(400), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False)
    pinned = db.Column(db.Boolean, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'),
                           nullable=False)

    tags = db.relationship("Tag_Thread", backref='thread', lazy=True)
    
    comments = db.relationship("Comment", backref='thread', lazy=True, cascade="delete")
    
    def __init__(self, name):
        self.name = name
        self.desc = ""
        self.hidden = False
        self.pinned = False

    @staticmethod
    def search_threads_by_thread(search):
        stmt = text("SELECT Thread.id, Thread.name, Account.username, Section.name FROM Thread"
                    " LEFT JOIN Account ON Account.id = Thread.account_id"
                    " LEFT JOIN Section ON Section.id = Thread.section_id"
                    " WHERE (Thread.name LIKE :search)"
                    " ORDER BY Thread.date_created DESC").params(search='%'+search+'%')
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "username":row[2], "section":row[3]})
        return response;

    @staticmethod
    def search_threads_by_user(user):
        stmt = text("SELECT Thread.id, Thread.name, Account.username, Section.name FROM Thread"
                    " LEFT JOIN Account ON Account.id = Thread.account_id"
                    " LEFT JOIN Section ON Section.id = Thread.section_id"
                    " WHERE Account.username LIKE :user"
                    " ORDER BY Thread.date_created DESC").params(user='%'+user+'%')
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "username":row[2], "section":row[3]})
        return response;

    @staticmethod
    def find_my_threads(account_id):
        stmt = text("SELECT  Thread.id, Thread.name, Section.name FROM Thread"
                    " LEFT JOIN Account ON Account.id = Thread.account_id"
                    " LEFT JOIN Section ON Section.id = Thread.section_id"
                    " WHERE (Thread.account_id = :accountid)"
                    " ORDER BY Thread.date_created DESC").params(accountid=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "section":row[2]})
        return response
