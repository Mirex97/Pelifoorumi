from application import db
from sqlalchemy.sql import text

class User(db.Model):
    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144))
    role = db.Column(db.String(144), nullable=False)

    comments = db.relationship("Comment", backref='account', lazy=True, cascade="delete")
    threads = db.relationship("Thread", backref='account', lazy=True, cascade="delete")
    

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.role = "default"
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        if self.role == 'Admin':
            return True
        return False

    @staticmethod
    def find_usernames():
        stmt = text("SELECT account.id, account.username, account.role FROM account"
            " GROUP BY account.id"
            " ORDER BY account.username"
            " DESC")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "role":row[2]})
        return response

    @staticmethod
    def find_users_not_me(user_id):
        stmt = text("SELECT account.id, account.username, account.role FROM account"
            " WHERE (account.id != :userid)"
            " GROUP BY account.id"
            " ORDER BY account.username"
            " DESC").params(userid = user_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "role":row[2]})
        return response
        
