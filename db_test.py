from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:lishenzhi1214@localhost:1433/chatroom?charset=utf8'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lishenzhi1214@localhost:3306/chatroom?charset=utf8'

db = SQLAlchemy(app)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # SQLAlchemy will automatically set the first Integer PK column that's not marked as a FK as auto_increment=True
    nickname = db.Column(db.String(20))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Chat %r>' % (self.nickname)

db.create_all()
