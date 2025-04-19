from flask import Flask, render_template, request, session, flash, redirect, url_for
from model import *
import os
from urllib.parse import urlparse

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "WEB_MOVIE_DUNG_HUY_VY"

init_db(app)


@app.route("/")
def home():
    movies_nominated = Film.query.order_by(Film.rating.desc()).limit(10).all()
    movies_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_theater = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_single_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_special = Film.query.order_by(db.func.random()).limit(10).all()
    top_rated = Film.query.order_by(Film.rating.desc()).limit(10).all()
    genres = Genre.query.all()

    return render_template("index.html",
                           movies=[],  # Không hiển thị section lọc/tìm kiếm trên trang chủ
                           movies_nominated=movies_nominated,
                           movies_new=movies_new,
                           movies_theater=movies_theater,
                           movies_single_new=movies_single_new,
                           movies_special=movies_special,
                           top_rated=top_rated,
                           genres=genres)


@app.route('/search')
def search():
    query = request.args.get('q')
    genres = Genre.query.all()

    # Lấy các danh sách phim giống /home
    movies_nominated = Film.query.order_by(Film.rating.desc()).limit(10).all()
    movies_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_theater = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_single_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_special = Film.query.order_by(db.func.random()).limit(10).all()
    top_rated = Film.query.order_by(Film.rating.desc()).limit(10).all()

    if query:
        movies = Film.query.filter(Film.title.ilike(f'%{query}%')).all()
    else:
        movies = []
        flash("Vui lòng nhập từ khóa tìm kiếm!", "error")
        return redirect(url_for('home'))

    return render_template('index.html',
                           movies=movies,
                           genres=genres,
                           movies_nominated=movies_nominated,
                           movies_new=movies_new,
                           movies_theater=movies_theater,
                           movies_single_new=movies_single_new,
                           movies_special=movies_special,
                           top_rated=top_rated)


@app.route('/genre/<genre>')
def getFilm(genre):
    genre_obj = Genre.query.filter_by(genre=genre).first()
    genres = Genre.query.all()

    # Lấy các danh sách phim giống /home
    movies_nominated = Film.query.order_by(Film.rating.desc()).limit(10).all()
    movies_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_theater = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_single_new = Film.query.order_by(Film.release_date.desc()).limit(10).all()
    movies_special = Film.query.order_by(db.func.random()).limit(10).all()
    top_rated = Film.query.order_by(Film.rating.desc()).limit(10).all()

    if not genre_obj:
        flash("Thể loại không tồn tại!", "error")
        return redirect(url_for('home'))

    movies = genre_obj.films

    return render_template('index.html',
                           movies=movies,
                           genres=genres,
                           movies_nominated=movies_nominated,
                           movies_new=movies_new,
                           movies_theater=movies_theater,
                           movies_single_new=movies_single_new,
                           movies_special=movies_special,
                           top_rated=top_rated)


@app.route('/movie/<title>')
def movie_detail(title):
    movie = Film.query.filter_by(title=title).first()
    genres = Genre.query.all()  # Thêm genres để hiển thị dropdown
    if movie:
        similar_movies = movie.genres[0].films[0:5] if movie.genres else []
        return render_template('infor.html', movie=movie, similar_movies=similar_movies, genres=genres)
    else:
        flash("Không tìm thấy phim!", "error")
        return redirect(url_for('home'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['email'] = email
            session['user_id'] = user.id
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for("home"))
        else:
            flash("Sai email hoặc mật khẩu!", "error")
            return redirect(url_for("login"))
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]
        if not email or not name or not password:
            flash("Email, Họ tên, Mật khẩu không được để trống!", "error")
            return redirect(url_for("register"))
        if User.query.filter_by(email=email).first():
            flash("Email đã tồn tại!", "error")
            return redirect(url_for("register"))
        new_user = User(email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        flash("Đăng ký thành công!", "success")
        return redirect(url_for("login"))
    return render_template('login.html')


@app.route("/about/<title>")
def about(title):
    movie = Film.query.filter_by(title=title).first()
    genres = Genre.query.all()  # Thêm genres để hiển thị dropdown
    if movie:
        similar_movies = movie.genres[0].films[0:5] if movie.genres else []
        link_movie = movie.url_film
        youtube_link = "https://youtu.be/"
        video_id = link_movie.replace(youtube_link, "", 1)
        comments = movie.comments
        return render_template("about.html", video_id=video_id, movie=movie, similar_movies=similar_movies,
                               comments=comments, genres=genres)
    else:
        flash("Không tìm thấy phim!", "error")
        return redirect(url_for('home'))


@app.route("/add_comment", methods=["POST"])
def add_comment():
    filmId = request.form['filmId']
    title = request.form['title']
    if 'user_id' not in session:
        flash('Đăng nhập mới được bình luận', 'error')
        return redirect(url_for('about', title=title))
    content = request.form['content']
    comment = Comment(film_id=filmId, user_id=session['user_id'], content=content)
    db.session.add(comment)
    db.session.commit()
    flash('Thêm Bình Luận Thành Công', 'success')
    return redirect(url_for('about', title=title))


@app.route('/logout')
def logout():
    session.clear()
    flash("Đăng xuất thành công!", "success")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)