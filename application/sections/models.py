from application import db

class Section(db.Model):
    #Tämä tietokanta pöytä ei vielä käytössä!
    __tablename__ = "section"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    #Tämän avulla listataan kaikki näkyvät palstat!
    #Ylläpito voi vaihtaa tarvittaessa palstan osiota,
    #jos se vahingossa joutuu väärään paikkaan. 
    threads = db.relationship("Thread", backref='section', lazy=True)

    def __init__(self, name):
        self.name = name
