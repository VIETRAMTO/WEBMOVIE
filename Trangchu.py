from flask import Flask, render_template
import csv
import os
from urllib.parse import urlparse
import pandas as pd

app = Flask(__name__)
CSV_FILE = 'movies_list.csv'


def validate_poster_url(url):
    """Validate IMDb/Amazon poster URL"""
    if not url or not isinstance(url, str):
        return False

    parsed = urlparse(url)
    return (parsed.netloc.endswith('media-amazon.com')
            and parsed.path.startswith('/images/M/')
            and any(ext in url.lower() for ext in ['.jpg', '.jpeg', '.png']))


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
                    'poster': row['Poster'],
                    'linkvid': row['link vid']
                })

    return movies


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
            'poster': row['Poster'],
            "linkvid": row['link vid']

        })
    print(movies)
    return render_template('index.html', movies=movies)
@app.route("/about")
def about():
    video_id = load_movies()[0]
    print(video_id)

    return render_template("about.html", video_id=video_id['linkvid'])


if __name__ == '__main__':
    app.run(debug=True)