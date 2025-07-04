from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String())

class test1(db.Model):
    clid = db.Column(db.Integer, primary_key=True)
    clname = db.Column(db.String(80), nullable=False)