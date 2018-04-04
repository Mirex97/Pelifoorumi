from application import db

class Tag(db.Model):
    #Tämä tietokanta pöytä ei vielä käytössä!

    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modifed = db.Column(db.DateTime, default=db.func.current_timestamp(),
                             onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    #Tarvitsee monesta moneen yhteyden threadin ja tagin välillä!
    #Threadillä voi olla useita tägejä ja tägillä voi olla useita threadejä!
    #Tämä tarvitsee vielä varmistuksen toimiiko se näin?
    threads = db.relationship("Thread", backref='tag', lazy=True)

    def __init__(self, name):
        self.name = name
