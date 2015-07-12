
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:lishenzhi1214@localhost:1433/chatroom?charset=utf8'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lishenzhi1214@localhost:3306/chatroom?charset=utf8'
db = SQLAlchemy(app)

from app import views, models
