from application import db
from sqlalchemy.sql import text

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    message = db.Column(db.String(400), nullable=False)
    
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, message):
        self.message = message

    @staticmethod
    def find_comments_with_thread(thread_id):
        stmt = text("SELECT  Comment.id, Account.username, Comment.message, Comment.date_created FROM Comment"
                    " LEFT JOIN Account ON Comment.account_id = Account.id"
                    " WHERE (Comment.thread_id IS :threadid)"
                    " GROUP BY Comment.id"
                    " ORDER BY Comment.date_created"
                    " DESC").params(threadid=thread_id)
        #" + str(section_id) + ")"
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "message":row[2], "date":row[3]})
        return response
