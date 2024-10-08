from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    released = db.Column(db.Date)
    director = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255))