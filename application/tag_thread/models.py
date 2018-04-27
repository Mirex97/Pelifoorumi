from application import db
from sqlalchemy.sql import text

class Tag_Thread(db.Model):
    __tablename__ = "Tag_Thread"
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('Tag.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('Thread.id'), nullable=False)

    @staticmethod
    def check_for_id(tag_id, thread_id):
        stmt = text("SELECT * FROM Tag_Thread"
                    " WHERE (tag_id = :tagid)"
                    " AND (thread_id = :threadid)").params(tagid = tag_id, threadid = thread_id)
        res = db.engine.execute(stmt)
        for row in res:
            return True
        return False
