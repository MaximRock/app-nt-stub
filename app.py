from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

client = app.test_client()

engine = db.create_engine('sqlite:///db.sqlite').engine.connect()

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from models import *

Base.metadata.create_all(bind=engine)


@app.route('/music/all', methods=['GET'])
def get_list():
    music_db = Music.query.all()
    serialized = []
    for music in music_db:
        serialized.append({
            'id': music.id,
            'datetime': music.datetime,
            'musical_style': music.musical_style,
            'group_name': music.group_name,
            'album': music.album,
            'release_year': music.release_year,
            'carrier': music.carrier,
            'description': music.description
        })
    return jsonify(serialized)


@app.route('/music', methods=['POST'])
def update_list():
    new_one = Music(**request.json)
    session.add(new_one)
    session.commit()
    serialized = {
        'id': new_one.id,
        'datetime': new_one.datetime,
        'musical_style': new_one.musical_style,
        'group_name': new_one.group_name,
        'album': new_one.album,
        'release_year': new_one.release_year,
        'carrier': new_one.carrier,
        'description': new_one.description
    }
    return jsonify(serialized)


@app.route('/music/<int:music_id>', methods=['GET'])
def get_list_id(music_id):
    item = Music.query.filter(Music.id == music_id).first()

    serialized = {
        'id': item.id,
        'datetime': item.datetime,
        'musical_style': item.musical_style,
        'group_name': item.group_name,
        'album': item.album,
        'release_year': item.release_year,
        'carrier': item.carrier,
        'description': item.description
    }
    return jsonify(serialized)

@app.route('/music/<int:music_id>', methods=['PUT'])
def update_tutorial(music_id):
    item = Music.query.filter(Music.id == music_id).first()
    params = request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in params.items():
        setattr(item, key, value)
    session.commit()
    serialized = {
        'id': item.id,
        'datetime': item.datetime,
        'musical_style': item.musical_style,
        'group_name': item.group_name,
        'album': item.album,
        'release_year': item.release_year,
        'carrier': item.carrier,
        'description': item.description
    }
    return jsonify(serialized)


@app.route('/music/<int:music_id>', methods=['DELETE'])
def delete_tutorial(music_id):
    item = Music.query.filter(Music.id == music_id).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return '', 204


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
