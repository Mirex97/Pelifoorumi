from application import db

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    hidden = db.Column(db.Boolean, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    #section_id = db.Column(db.Integer, db.ForeignKey('section.id'),
                           #nullable=False)
    #Kuten tag modelissa lukee tämä tarvitsee varmistuksen!
    #tags = db.relationship("Tag", backref='thread', lazy=True)

    comments = db.relationship("Comment", backref='thread', lazy=True)
    
    #Jos hidden niin luokka ei näy muille paitsi ylläpidolle.
    #Tämän saa tehtyä, että listaukseen ei vain tule piilotettuja osia!
    #Ylläpito tai omistaja voi asettaa luokan piilotetuksi!

    #Ylläpito ei vielä luotu!
    def __init__(self, name):
        self.name = name
        self.hidden = False
