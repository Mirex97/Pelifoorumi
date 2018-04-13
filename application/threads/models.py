from application import db
from sqlalchemy.sql import text

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'),
                           nullable=False)
    #Kuten tag modelissa lukee tämä tarvitsee varmistuksen!
    #tags = db.relationship("Tag", backref='thread', lazy=True)

    comments = db.relationship("Comment", backref='thread', lazy=True, cascade="delete")
    
    #Jos hidden niin luokka ei näy muille paitsi ylläpidolle.
    #Tämän saa tehtyä, että listaukseen ei vain tule piilotettuja osia!
    #Ylläpito tai omistaja voi asettaa luokan piilotetuksi!

    #Ylläpito ei vielä luotu!
    def __init__(self, name):
        self.name = name
        self.hidden = False

    @staticmethod
    def find_my_threads(account_id):
        #wat
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
