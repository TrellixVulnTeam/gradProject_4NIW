from . import db

pubs = db.Table('pubs',
        db.Column('profile_id', db.Integer, db.ForeignKey('profile.id')),
        db.Column('publication_id', db.Integer, db.ForeignKey('publications.id'))
    )

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    num_citations = db.Column(db.Integer)
    authors = db.relationship('Profile', secondary=pubs, backref=db.backref('papers', lazy='dynamic')) 

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    scholar_id = db.Column(db.String(50))
    url_picture = db.Column(db.String(50))
    interests = db.relationship('Topics', backref='author')

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    author_id = db.Column(db.Integer, db.ForeignKey('profile.id'))