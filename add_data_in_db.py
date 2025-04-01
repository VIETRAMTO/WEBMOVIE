# KHÔNG CHẠY FILE NÀY, TRÙNG LẶP DỮ LIỆU

# import pandas as pd
# from model import *
# from main import app
# from datetime import datetime

# df = pd.read_csv("./data/movies_list.csv")
# genres = ['Fantasy', 'Animation', 'Family', 'Adventure', 'Mystery', 'History', 'Musical', 'Short', 
#           'Horror', 'Thriller', 'Drama', 'Romance', 'Crime', 'Action', 'Comedy', 'Sci-Fi']

# with app.app_context():
#     for genre in genres:
#         if not Genre.query.filter_by(genre=genre).first():
#             gr = Genre(genre=genre)
#             db.session.add(gr)
    
#     db.session.commit()

#     for index, row in df.iterrows():
#         release_date = datetime.strptime(str(row["Year"]), "%Y").date()
#         film = Film(
#             title=row["Title"],
#             description=row["Plot"],
#             release_date=release_date,
#             poster=row["PosterURL"],
#             url_film=row["VideoUrl"],
#             rating=row["Rating"]
#         )
#         db.session.add(film)
#         for genre in row["Genre"].split(", "):
#             genre_obj = Genre.query.filter_by(genre=genre).first()
#             if genre_obj:
#                 film.genres.append(genre_obj)


#     db.session.commit()
