import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class ShareC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recieved_file = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, recieved_file, filename):
        self.recieved_file = recieved_file
        self.filename = filename

    def __repr__(self):
        return f"{self.filename}:{self.date}"