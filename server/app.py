"""
Module Documentation Goes Here
"""
from project import create_app

# Flask App Setup
app = create_app()

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug = True)


# from flask import Flask, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from extensions import db

# DEBUG = True
# app = Flask(__name__)
# app.config.from_object(__name__)
# # db = SQLAlchemy(app)


# #doing datbase stuff
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     location = db.Column(db.String(50))
#     date_created = db.Column(db.DateTime, default=datetime.now)

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     scholar_id = db.Column(db.String(50))
#     url_picture = db.Column(db.String(50))
#     interests = db.relationship('Topics', backref='author')

# class Topics(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60))
#     author_id = db.Column(db.Integer, db.ForeignKey('profile.id'))


# CORS(app, resources={r'/*': {'origins': '*'}})

# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')

# # @app.route('/topics', methods=['GET'])
# # def fetch_topics():

# @app.route('/<name>/<location>')
# def index(name, location):
#     user = User(name=name, location=location)
#     db.session.add(user)
#     db.session.commit()

#     return '<h1>Added new user!</h1>'

# if __name__ == '__main__':
#     db.init_app(app)
#     app.run(host='0.0.0.0', port = 5001, debug = True)
