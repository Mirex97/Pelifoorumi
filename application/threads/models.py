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
#Tarvitsee Users pöydästä omistajan nimen!
#Lisäksi tarvitsee Tags luokkaan liitokset!
#Nämä luokat luon vasta myöhemmin.
#Jos hidden -> Ainoastaan omistaja tai ylläpito pääsee käsiksi!
    def __init__(self, name):
        self.name = name
        self.hidden = False
