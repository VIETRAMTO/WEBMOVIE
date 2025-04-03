from flask import Flask, render_template, request, session, flash, redirect, url_for
from model import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] ="WEB_MOVIE_DUNG_HUY_VY"



@app.route("/")
def home():
    return render_template("index.html")

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
if __name__ == "__main__":
    app.run(debug=True)