from flask import Flask, render_template
import csv
import os
from urllib.parse import urlparse
import pandas as pd
from flask import Flask, render_template, request, session, flash, redirect, url_for
from model import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] ="WEB_MOVIE_DUNG_HUY_VY"


app = Flask(__name__)
CSV_FILE = 'movies_list.csv'

def load_movies():
    movies = []
    # default_poster = "https://m.media-amazon.com/300x450.png?text=No+Poster"
    #
    # with open(CSV_FILE, mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         poster_url = row.get('Poster', '').strip()
    #         if not validate_poster_url(poster_url):
    #             poster_url = default_poster
    #         movies.append({
    #             'id': row.get('ID', ''),
    #             'title': row.get('Title', 'Untitled'),
    #             'year': row.get('Year', 'N/A'),
    #             'rating': row.get('Rating', '0.0'),
    #             'poster': poster_url,
    #             'genre': row.get('Genre', '')
    #         })
    df = pd.read_csv('movies_list.csv')
    for index, row in df.iterrows():
        movies.append({
                    'title': row["Title"],
                    'poster': row['Poster URL'],
                    'linkvid': row['link vid'],
                    'year':row['Year'],
                    'genre': row['Genre'],  # Thêm thể loại, mặc định là 'N/A' nếu không có
                    'description': row['Plot'],  # Thêm mô tả nếu có
                    'release_date': row['Year'],
                    'actor':row['Actors']
                })

    return movies
@app.route('/movie/<title>')
def movie_detail(title):
    movies = load_movies()
    movie = next((m for m in movies if m['title'] == title), None)
    if movie:
        # Lấy danh sách phim tương tự dựa trên thể loại
        similar_movies = [m for m in movies if m['genre'] == movie['genre'] and m['title'] != movie['title']]
        return render_template('infor.html', movie=movie, similar_movies=similar_movies)
    else:
        flash("Không tìm thấy phim!", "error")
        return redirect(url_for('home'))


@app.route('/')
def home():
    movies = []
    # default_poster = "https://m.media-amazon.com/300x450.png?text=No+Poster"
    #
    # with open(CSV_FILE, mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         poster_url = row.get('Poster', '').strip()
    #         if not validate_poster_url(poster_url):
    #             poster_url = default_poster
    #         movies.append({
    #             'id': row.get('ID', ''),
    #             'title': row.get('Title', 'Untitled'),
    #             'year': row.get('Year', 'N/A'),
    #             'rating': row.get('Rating', '0.0'),
    #             'poster': poster_url,
    #             'genre': row.get('Genre', '')
    #         })
    df = pd.read_csv('movies_list.csv')
    for index, row in df.iterrows():
        movies.append({
            'title': row["Title"],
            'poster': row['Poster URL'],
            "linkvid": row['link vid'],
            'rate':row['IMDB Rating']

        })
    print(movies)
    return render_template('index.html', movies=movies)
@app.route("/about")
def about():
    video_id = load_movies()[0]
    print(video_id)

    return render_template("about.html", video_id=video_id['linkvid'])
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.password==password:
            session['email'] = email
            session['user_id'] = user.Id
            return redirect(url_for("account"))
        else:
            flash("Sai email hoặc mật khẩu!", "error")
            return redirect(url_for("account"))
    return render_template('Login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]
        if not email or not name or not password:
            flash("Email, Họ tên, Mật khẩu không được để trống!", "error")
            return redirect(url_for("account"))
        if User.query.filter_by(email=email).first():
            flash("Email đã tồn tại!", "error")
            return redirect(url_for("account"))
        new_user = User(email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        flash("Đăng ký thành công!", "success")
        return redirect(url_for("account"))
    return render_template("Login.html")


if __name__ == '__main__':
    app.run(debug=True)