import os
from urllib.parse import urlparse
from flask import Flask, render_template, request, session, flash, redirect, url_for
from model import *

app = Flask(__name__)
init_db(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] ="WEB_MOVIE_DUNG_HUY_VY"

@app.route("/")
def home():
    movies = Film.query.all()
    return render_template("index.html", movies=movies)

@app.route('/movie/<title>')
def movie_detail(title):
    pass
    # movies =
    # movie = next((m for m in movies if m['title'] == title), None)
    # if movie:
    #     # Lấy danh sách phim tương tự dựa trên thể loại
    #     similar_movies = [m for m in movies if m['genre'] == movie['genre'] and m['title'] != movie['title']]
    #     return render_template('infor.html', movie=movie, similar_movies=similar_movies)
    # else:
    #     flash("Không tìm thấy phim!", "error")
    #     return redirect(url_for('home'))

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
    return render_template('login_register.html')

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
    return render_template("login_register.html")

@app.route('/search')
def search():
    pass


@app.route("/about/<filmId>")
def about(filmId):
    movie = Film.query.filter_by(id=filmId).all()[0]
    link_movie = movie.url_film
    youtube_link = "https://youtu.be/"
    video_id = link_movie.replace(youtube_link, "", 1)
    return render_template("about.html", video_id=video_id)

@app.route("/add_comment/<filmId>", methods=["POST"])
def add_comment(filmId):
    pass

if __name__ == "__main__":
    app.run(debug=True)