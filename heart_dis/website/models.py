from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class HeartData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    cp = db.Column(db.Integer)
    trestbps = db.Column(db.Integer)
    chol = db.Column(db.Float)	
    fbs = db.Column(db.Integer)	
    restecg = db.Column(db.Integer)	
    thalach = db.Column(db.Integer)	
    exang = db.Column(db.Integer)	
    oldpeak = db.Column(db.Float)
    slope = db.Column(db.Integer)	
    ca = db.Column(db.Integer)	
    thal = db.Column(db.Integer)
    target = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    history = db.relationship('HeartData')