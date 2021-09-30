from . import db, ma

pubs = db.Table('pubs',
        db.Column('profile_id', db.Integer, db.ForeignKey('profile.id')),
        db.Column('publication_id', db.Integer, db.ForeignKey('publications.id'))
    )

#TODO: add abstract column
class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    abstract = db.Column(db.String(500))
    num_citations = db.Column(db.Integer)
    authors = db.relationship('Profile', secondary=pubs, backref=db.backref('papers', lazy='dynamic')) 

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    scholar_id = db.Column(db.String(50), unique=True)
    url_picture = db.Column(db.String(50))
    interests = db.relationship('Topics', backref='author')

    def __init__(self, name, scholar_id, url_picture):
        self.name = name
        self.scholar_id = scholar_id
        self.url_picture = url_picture


class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'scholar_id', 'url_picture')

# #init schema
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    author_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id
class TopicSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'author_id')

# #init schema
topic_schema = TopicSchema()
topics_schema = TopicSchema(many=True)