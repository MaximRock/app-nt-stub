from app import db, session, Base
from datetime import datetime


class Music(Base):
    __tablename__ = 'music_db'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    musical_style = db.Column(db.String(50), nullable=True)
    group_name = db.Column(db.String(50), nullable=True)
    album = db.Column(db.String(50), nullable=True)
    release_year = db.Column(db.Integer, nullable=True)
    carrier = db.Column(db.String(25), nullable=True)
    description = db.Column(db.String(500), nullable=False)
