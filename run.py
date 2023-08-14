from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Topic(db.Model):
    __tablename__ = "topic_name"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subtopics = db.relationship('SubTopic', back_populates='topic')  # Corrected the back_populates attribute name

class SubTopic(db.Model):
    __tablename__ = "subtopic_name"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    topic_id = db.Column(
        db.Integer, 
        db.ForeignKey('topic_name.id')
    )
    topic = db.relationship('Topic', back_populates='subtopics')  # Corrected the back_populates attribute name

@app.route('/', methods=['GET'])
def index():
    data = {}

    topics = Topic.query.all()
    for topic in topics:
        data[topic.name] = [{subtopic.name:subtopic.id} for subtopic in topic.subtopics]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
