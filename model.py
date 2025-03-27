from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    video_id = "r6DtZ_6rjJo"  # ID của video YouTube
    return render_template("about.html", video_id=video_id)

if __name__ == "__main__":
    app.run(debug=True)
