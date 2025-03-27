from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/infor")
def infor():
    return render_template("infor.html")
@app.route("/about")
def about():
    video_id = "hrUJ3JZ1EMI"  # ID của video YouTube
    return render_template("about.html", video_id=video_id)

if __name__ == "__main__":
    app.run(debug=True)
