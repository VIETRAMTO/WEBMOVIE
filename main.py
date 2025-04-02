import os
import datetime
from flask import Flask, render_template, request, session, flash, redirect, url_for, jsonify, json
from model import *


app = Flask(__name__)
COMMENTS_FILE = "static/scripts/movies.json"
  # Đặt tên file JSON lưu bình luận

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] ="WEB_MOVIE_DUNG_HUY_VY"
init_db(app)

@app.route("/")
def home():
    movies = Film.query.all()
    return render_template("index.html", movies=movies)

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

@app.route("/infor/<filmId>")
def infor(filmId):
    movie = Film.query.filter_by(id=filmId).all()[0]
    return render_template("infor.html", movie=movie)

@app.route("/about/<filmId>")
def about(filmId):
    movie = Film.query.filter_by(id=filmId).all()[0]
    link_movie = movie.url_film
    youtube_link = "https://youtu.be/"
    video_id = link_movie.replace(youtube_link, "", 1)
    return render_template("about.html", video_id=video_id)

# Load comments từ file JSON

def load_comments():
    if not os.path.exists(COMMENTS_FILE):
        return []
    with open(COMMENTS_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Lưu bình luận vào file JSON
def save_comment(comment):
    # Kiểm tra nếu thư mục static/scripts chưa tồn tại thì tạo mới
    os.makedirs(os.path.dirname(COMMENTS_FILE), exist_ok=True)

    # Kiểm tra nếu file chưa có thì tạo mới file JSON rỗng
    if not os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)  # Ghi danh sách rỗng vào file

    # Đọc dữ liệu hiện tại
    with open(COMMENTS_FILE, "r", encoding="utf-8") as file:
        comments = json.load(file)

    # Thêm comment mới
    comments.append(comment)

    # Ghi lại vào file
    with open(COMMENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(comments, file, indent=4, ensure_ascii=False)

    print("Comment saved successfully!")

# API hiển thị 3 bình luận gần nhất
@app.route("/get_comments", methods=["GET"])
def get_comments():
    comments = load_comments()
    return jsonify(comments[-3:])  # Trả về 3 bình luận mới nhất

# API thêm bình luận
@app.route("/add_comment/<filmId>", methods=["POST"])
def add_comment(filmId):
    if not session["user_id"]:
        return jsonify({"message":"Chưa Đăng Nhập!"}), 400
    data = request.get_json()
    if not data or "username" not in data or "comment" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_comment = Comment(film_id=filmId,
                          user_id=session['user_id'],
                          content=data["comment"]
                          )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message":"Thêm Bình Luận Thành Công!"}), 201

@app.route("/get_latest_comment", methods=["GET"])
def get_latest_comment():
    if not os.path.exists(COMMENTS_FILE):
        return jsonify({"message": "Chưa có bình luận nào"}), 404

    with open(COMMENTS_FILE, "r", encoding="utf-8") as file:
        comments = json.load(file)

    if not comments:
        return jsonify({"message": "Chưa có bình luận nào"}), 404

    return jsonify(comments[-1])  # Trả về comment mới nhất




if __name__ == "__main__":
    app.run(debug=True)
