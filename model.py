from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.DateTime, nullable=True)
    poster = db.Column(db.Text, nullable=False)
    url_film = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    genres = db.relationship('Genre', secondary='type_of_film', back_populates="films")

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), unique=True, nullable=False)
    films = db.relationship('Film', secondary='type_of_film', back_populates="genres")

class TypeOfFilm(db.Model):
    __tablename__ = 'type_of_film'
    genreId = db.Column(db.Integer, db.ForeignKey("genre.id"), primary_key=True)
    filmId = db.Column(db.Integer, db.ForeignKey("film.id"), primary_key=True)

class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    film = db.relationship("Film", backref="ratings", lazy=True)
    user = db.relationship("User", backref="ratings", lazy=True)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    film = db.relationship("Film", backref="comments", lazy=True)
    user = db.relationship("User", backref="comments", lazy=True)
