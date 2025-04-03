import requests
import pandas as pd

API_KEY = "c5f3dbee"  # Thay bằng API Key của bạn
movies_list = [
    "Avatar", "Star War", "Your Name", "Titanic", "The Good Student",
    "Silent Night", "Spider-man", "Thor", "10 Minutes Gone", "6 Days", "Young Detective Dee: Rise of the Sea Dragon",
    "Battlefield: Fall Of The World", "Killer Mountain", "Pee Nak", "Pee Nak 2", "Pee Nak 3", "Pee Nak 4",
    "Arthur Christmas", "Paddington", "BRIDGE TO TERABITHIA", "Ballerina", "The mechanic", "Candle in the Tomb: The Worm Valley",
    "Candle in the Tomb", "the world unseen", "Pandora", "Cosmic Sin", "Mohawk", "Gattaca",
    "Chappie", "Jurassic Triangle", "Jailbreak", "Jabberwock", "Almighty Zeus", "Peace River", "Convict", "Yellow Flowers on the Green Grass",
    "Just Another Dream"
]

# API để lấy dữ liệu phim
def get_movie_data(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return {
                "Title": data.get("Title", "Không có dữ liệu"),
                "Year": data.get("Year", "Không có dữ liệu"),
                "Genre": data.get("Genre", "Không có dữ liệu"),
                "IMDB Rating": data.get("imdbRating", "Không có dữ liệu"),
                "Plot": data.get("Plot", "Không có dữ liệu"),
                "Actors": data.get("Actors", "Không có dữ liệu"),  # Lấy thêm thông tin diễn viên
                "Poster URL": data.get("Poster", "Không có dữ liệu")
            }
    return None

# Lấy dữ liệu của tất cả phim và lưu vào danh sách
movies_data = []
for movie_title in movies_list:
    movie_data = get_movie_data(movie_title)
    if movie_data:
        movies_data.append(movie_data)

# Lưu dữ liệu vào CSV
df = pd.DataFrame(movies_data)
csv_file = "movies_list.csv"
df.to_csv(csv_file, index=False, encoding="utf-8")

print(f"✔ Dữ liệu phim đã được lưu vào {csv_file}")
