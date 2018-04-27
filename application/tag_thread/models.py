from application import db
from sqlalchemy.sql import text

class Tag_Thread(db.Model):
    __tablename__ = "tag_thread"
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

    @staticmethod
    def check_for_id(tag_id, thread_id):
        stmt = text("SELECT * FROM tag_thread"
                    " WHERE (tag_id = :tagid)"
                    " AND (thread_id = :threadid)").params(tagid = tag_id, threadid = thread_id)
        res = db.engine.execute(stmt)
        for row in res:
            return True
        return False
