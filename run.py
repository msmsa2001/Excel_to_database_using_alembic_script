from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'

db = SQLAlchemy(app)

class Topic(db.Model):
    __tablename__ = "topic_name"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class SubTopic(db.Model):
    __tablename__ = "subtopic_name"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    topic_id = db.Column(
        db.Integer, 
        db.ForeignKey('topic_name.id'),
        )

