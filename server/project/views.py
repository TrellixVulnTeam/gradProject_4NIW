from operator import methodcaller
from app import app
from flask import (
    json,
    request,
    jsonify,
    current_app as app
)
from .models import Profile, db, profile_schema, profiles_schema, Topics, topics_schema, topic_schema
from sqlalchemy.sql.expression import func, select

@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'msgg': 'Hello World From Project' })

@app.route('/profile', methods=['POST'])
def add_product():
    name = request.json['name']
    scholar_id = request.json['scholar_id']
    url_picture = request.json['url_picture']

    new_profile = Profile(name, scholar_id, url_picture)

    db.session.add(new_profile)
    db.session.commit()

    return profile_schema.jsonify(new_profile)

@app.route('/profile', methods=['GET'])
def get_profiles():
    all_profiles = Profile.query.all()

    result = profiles_schema.dump(all_profiles)

    return jsonify(result)

@app.route('/profile/<id>', methods=['GET'])
def get_profile(id):
    profile = Profile.query.get(id)

    return profile_schema.jsonify(profile)

@app.route('/profile/page/', methods=['GET'], defaults={"page": 1})
@app.route('/profile/page/<int:page>', methods=['GET'])
def get_profile_limit(page):
    temp = Profile.query.paginate(page, per_page=10, error_out=False)
    limit_profiles = temp.items
    prev_page = 0
    if page == 1:
        prev_page = 1
    else:
        prev_page = page-1
    next_page = temp.next_num
    last_page = temp.pages

    result = profiles_schema.dump(limit_profiles)
    result.append(str(prev_page))
    result.append(str(next_page))
    result.append(str(last_page))
    return jsonify(result)

@app.route('/profile/search/<name>', methods=['GET'])
def get_search(name):
    results  = Profile.query.filter(Profile.name.like('%'+name+'%')).all()

    result = profiles_schema.dump(results)
    return jsonify(result)

@app.route('/profile/random', methods=['GET'])
def get_random_profiles():
    results = Profile.query.order_by(func.random()).limit(5)

    result = profiles_schema.dump(results)
    return jsonify(result)

@app.route('/topic', methods=['GET'])
def get_topics():
    # all_topics = Topics.query.distinct(Topics.name)
    all_topics = Topics.query.with_entities(Topics.name).distinct()
    result = topics_schema.dump(all_topics)

    return jsonify(result)

@app.route('/topic/<id>', methods=['GET'])
def get_topic(id):
    topic = Topics.query.get(id)
    return topic_schema.jsonify(topic)



