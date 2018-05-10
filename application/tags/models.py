from application import db
from sqlalchemy.sql import text

class Tag(db.Model):

    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modifed = db.Column(db.DateTime, default=db.func.current_timestamp(),
                             onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    threads = db.relationship("Tag_Thread", backref='tag', lazy=True, cascade='delete')

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_threads_by_tag(tag):
        stmt = text("SELECT DISTINCT thread.id, thread.name, account.username, section.name, thread.date_created FROM thread"
                    " LEFT JOIN account ON account.id = thread.account_id"
                    " LEFT JOIN section ON section.id = thread.section_id"
                    " LEFT JOIN tag_thread ON thread.id = tag_thread.thread_id"
                    " LEFT JOIN tag ON tag.id = tag_thread.tag_id"
                    " WHERE LOWER(tag.name) LIKE LOWER(:tagi)"
                    " ORDER BY thread.date_created DESC").params(tagi = tag)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "username":row[2], "section":row[3]})
        return response

    @staticmethod
    def find_with_tag(tag):
        stmt = text("SELECT * FROM tag WHERE (tag.name = :tagi)").params(tagi = tag)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response

    @staticmethod
    def find_tags_with_thread(thread_id):
        stmt = text("SELECT tag.id, tag.name FROM tag"
                    " LEFT JOIN tag_thread ON tag.id = tag_thread.tag_id"
                    " LEFT JOIN thread ON thread.id = tag_thread.thread_id"
                    " WHERE (thread.id = :threadid)").params(threadid=thread_id)
        #" + str(section_id) + ")"
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response


    @staticmethod
    def find_tags():
        stmt = text("SELECT tag.id, tag.name FROM tag")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response
        

    
