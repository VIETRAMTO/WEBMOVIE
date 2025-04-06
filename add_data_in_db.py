# import pandas as pd
# from model import *
# from main import app
# from datetime import datetime

# df = pd.read_csv("./data/movies_list.csv")
# df['Actors'] = df['Actors'].fillna('')
# actors = set()
# for index, row in df.iterrows():
#     if isinstance(row["Actors"], str):
#         actors.update(row["Actors"].split(', '))

# with app.app_context():
#     for name in actors:
#         if not Actor.query.filter_by(name=name).first():
#             actor = Actor(name=name)
#             db.session.add(actor)
#     db.session.commit()
#     for index, row in df.iterrows():
#         film = Film.query.filter_by(title=row['Title']).first()
#         for name in row["Actors"].split(", "):
#             actor_obj = Actor.query.filter_by(name=name).first()
#             if actor_obj:
#                 film.actors.append(actor_obj)


#     db.session.commit()
