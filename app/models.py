
from app import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as auto_increment=True
    nickname = db.Column(db.String(20))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Chat %r>' % (self.nickname)
