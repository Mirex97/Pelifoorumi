from application import db
from sqlalchemy.sql import text

class Comment(db.Model):
    __tablename__ = "comment"

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
        stmt = text("SELECT  comment.id, account.username, comment.message, comment.date_created FROM comment"
                    " LEFT JOIN account ON comment.account_id = account.id"
                    " WHERE (comment.thread_id = :threadid)"
                    " ORDER BY comment.date_created"
                    " DESC").params(threadid=thread_id)
        #" + str(section_id) + ")"
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1], "message":row[2], "date":row[3]})
        return response
